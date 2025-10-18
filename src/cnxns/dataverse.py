from typing import Generator

import msal  # type: ignore
import requests


def _generate_token(
    base_url: str,
    client_id: str,
    client_secret: str,
    tenant_id: str,
) -> str:
    """
    Returns a token for use with the Microsoft Dataverse OAuth 2.0 REST API.

    Generates a token for use with the Microsoft Dataverse OAuth 2.0 REST API.
    If a cached token exists, returns this instead. Requires an application to
    be registered within Azure Active Directory.

    Args:
        base_url (String): Base URL for Dataverse instance.
        client_id (String): Azure active directory application guid.
        client_secret (String): A secret string that the application uses to
            prove its identity.
        tenant_id (String): Azure active directory directory guid.

    Returns:
        String: authorization token.
    """

    scope = f"{base_url}/.default"
    endpoint = f"https://login.microsoftonline.com/{tenant_id}"

    app = msal.ConfidentialClientApplication(
        client_id,
        authority=endpoint,
        client_credential=client_secret,
    )

    token_array = None

    # TODO: fix token caching:
    #    token_array= app.acquire_token_silent(scope, account=None)

    if not token_array:
        token_array = app.acquire_token_for_client(scopes=scope)

    return token_array["access_token"]


def query_api(
    client_id: str,
    client_secret: str,
    tenant_id: str,
    base_url: str,
    api_url: str,
    query: str,
    chunksize: int,
) -> Generator:
    """
    Returns a dictionary of data from a Microsoft Dataverse database.

    Calls the Microsoft Dataverse OAuth 2.0 REST API and appends the results
    to a list. If response is >5k rows, a new URL is returned and the process
    is repeated. If any of the API calls fails, the loop is broken and the list
    is returned wtih any results returned so far.

    Args:
        client_id (String): Azure active directory application guid.
        client_secret (String): A secret string that the application uses to
            prove its identity.
        tenant_id (String): Azure active directory directory guid.
        base_url (String): Base URL for Dataverse instance.
        api_url (String): The URL for the Dataverse API instance.
        query (String): The query to send to the api.
        chunksize (Integer): The size of each chunk to read-in.

    Yields:
        Generator: A generator of paginated JSON results.
    """

    token = _generate_token(
        base_url,
        client_id,
        client_secret,
        tenant_id,
    )

    odata = "odata.include-annotations"
    annotations = "OData.Community.Display.V1.FormattedValue"

    request_headers = {
        "Authorization": f"Bearer {token}",
        "OData-MaxVersion": "4.0",
        "OData-Version": "4.0",
        "Accept": "application/json",
        "Content-Type": "application/json; charset=utf-8",
        "Prefer": f"odata.maxpagesize={chunksize}, {odata}={annotations}",
    }

    url = f"{base_url}/{api_url}{query}"

    while url is not None:
        response = requests.get(url, headers=request_headers)
        response.raise_for_status()
        result = response.json()
        url = result.get("@odata.nextLink", None)
        yield result["value"]
