<a name="readme-top"></a>

<h1 align="center">THIS PROJECT IS IN ALPHA AND MAY INTRODUCE BREAKING CHANGES</h1>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<br />
<div align="center">
  <a href="https://github.com/philipbudden/cnxns">
    <img src=".logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Cnxns</h3>

  <p align="center">
    A lightweight, extensible library that simplifies interaction with heterogeneous data systems. It standardises connections, authentication, and data transfer into consistent, Pandas‑friendly workflows, enabling seamless integration across databases and APIs without the overhead of system‑specific code.
    <br />
    <a href="https://github.com/philipbudden/cnxns/issues">Report Bug</a>
    ·
    <a href="https://github.com/philipbudden/cnxns/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About the Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
    </li>
    <li>
      <a href="#usage">Usage</a>
      <ul>
        <a href="#dbms">dbms</a>
        <ul>
          <li><a href="#supports">Supports</a></li>
          <li><a href="#pre-requisites">Pre-requisites</a></li>
          <li><a href="#example">Example</a></li>
        </ul>
      </ul>
      <ul>
        <a href="#m365">m365</a>
        <ul>
          <li><a href="#supports">Supports</a></li>
          <li><a href="#pre-requisites">Pre-requisites</a></li>
          <li><a href="#example">Example</a></li>
        </ul>
      </ul>
    </li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About the Project

This library provides a unified interface for interacting with diverse data systems, eliminating the need to manage the intricacies of individual platforms. By abstracting connection handling, authentication, data retrieval, and writing operations into simple, consistent functions, it enables developers and data engineers to focus on analysis and integration rather than boilerplate code.

Whether working with traditional databases or modern API endpoints, the library standardises workflows into familiar patterns such as reading into Pandas DataFrames, chunked processing for large datasets, and seamless write‑back operations. Built with extensibility in mind, new data systems can be added without disrupting existing usage, ensuring the library evolves alongside your environment.

Designed for clarity, maintainability, and scalability, this library is a practical foundation for projects that demand reliable access to heterogeneous data sources.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started
```shell
pip install cnxns
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage

### dbms

The dbms module provides a streamlined interface for interacting with SQL-based data systems through SQLAlchemy. It abstracts connection setup, data ingestion, and write-back operations into concise, reusable functions that integrate seamlessly with Pandas. With built-in support for chunked reading and writing, it enables efficient handling of large datasets while maintaining clarity and consistency across varied database backends.

#### Supports

- Microsoft SQL Server
- MySQL/MariaDB

#### Pre-requisites
- Either:
  - ODBC Driver X for SQL Server (tested with 18)
  - MySQL ODBC X driver (tested with 9.4)

#### Example
```python
from cnxns import dbms as db

e = db.dbms_cnxn(
    dbms = "mssql",
    server = "localhost",
    uid = "sa",
    pwd = "YourStrong@Passw0rd",
    database = "dev",
)

df = db.dbms_reader(
    e,
    query = "SELECT TOP(1000) * FROM myAwesomeTable",
)

print(df)

for chunk in db.dbms_read_chunks(
    e,
    table_name = "myAwesomeTable",
    chunksize = 1000,
):

  db.dbms_writer(
      e,
      df,
      "myAwesomeTableSnapshot",
      if_exists="append",
  )
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### m365
The m365 module abstracts authentication and data access workflows for Microsoft 365 APIs, streamlining interactions with services like Graph and Dataverse. It handles token generation via MSAL and Azure AD app registration, enabling secure, reusable access patterns. With built-in support for chunked queries and JSON response handling, it simplifies integration into data pipelines and analytical workflows while maintaining flexibility across varied Microsoft 365 endpoints.

#### Supports
- Dataverse REST API
- Microsoft 365 Graph API

#### Pre-requisites
- An application registered in Azure Active Directory. You will need:
  - Tennant ID
  - Client ID
  - Client Secret

#### Example
```python
from cnxns.api import m365

result = m365.query_api(
    client_id="A123",
    client_secret="B234",
    tenant_id="C345",
    base_url="https://myamazingcompany.crm.dynamics.com",
    api_url="api/data/v9.0",
    query="/accounts?$select=accountid,versionnumber",
    chunksize=1000,
)
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [SQLAlchemy](https://pypi.org/project/sqlalchemy/)
* [msal](https://pypi.org/project/msal/)
* [pandas](https://pypi.org/project/pandas/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/philipbudden/cnxns.svg?style=for-the-badge
[contributors-url]: https://github.com/philipbudden/cnxns/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/philipbudden/cnxns.svg?style=for-the-badge
[forks-url]: https://github.com/philipbudden/cnxns/network/members
[stars-shield]: https://img.shields.io/github/stars/philipbudden/cnxns.svg?style=for-the-badge
[stars-url]: https://github.com/philipbudden/cnxns/stargazers
[issues-shield]: https://img.shields.io/github/issues/philipbudden/cnxns.svg?style=for-the-badge
[issues-url]: https://github.com/philipbudden/cnxns/issues
[license-shield]: https://img.shields.io/github/license/philipbudden/cnxns.svg?style=for-the-badge
[license-url]: https://github.com/philipbudden/cnxns/blob/main/LICENSE
[linkedin-url]: https://www.linkedin.com/company/pobl-group
[python-url]: https://www.python.org/
