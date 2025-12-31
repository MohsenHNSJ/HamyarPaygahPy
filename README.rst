=============
Hamyar Paygah
=============

..
    Badges section

.. list-table::
    :stub-columns: 1

    * - Package
      - |version| |status| |supported-python-versions| |poetry| |release-to-pypi| |implementation| |wheel| |pydantic-badge|
    * - Quality Assurance
      - |sonar-quality-gate| |sonar-reliability| |sonar-maintainability| |sonar-technical-debt| |sonar-bugs| |sonar-code-smells|
    * - Stats
      - |contributors| |stars| |issues| |pull-requests| |sonar-lines-of-code| |repository-size|
    * - Tests
      - |nox| |codspeed| |pre-commit-ci| |types| |codecov| |scorecard|
    * - Security
      - |synk| |sonar-security| |sonar-vulnerabilities| |openssf|
    * - Linters
      - |ruff| |pre-commit| |megalinter| |mypy| |pylint|
    * - Activity
      - |maintenance| |commit-activity|
    * - Documentation
      - |documentation|
    * - License
      - |license|


Overview
--------

Hamyar Paygah is an application designed for
**Emergency Medical Services (EMS) overseers**
to gather and review information from EMS servers.

This project is intended as **internal tooling** for authorized
EMS personnel only.


Status
------

**Development Status:** Alpha

This software is under active development and is not considered stable.
Features, behavior, data handling, and interfaces may change at any time
without notice.


Audience
--------

This project is intended exclusively for:

- Authorized Emergency Medical Services overseers
- Internal operational or supervisory use within EMS organizations

It is **not** intended for public use, consumer use, or deployment in
uncontrolled environments.


Technology Stack
----------------

- Python 3.13
- Tkinter (GUI framework)

The project is built and packaged by GitHub workflows and distributed as
a Windows executable (``.exe``).


Installation
------------

Prebuilt Windows executable files are produced by the project's build process.

No installation via package managers is currently supported.
Source builds and alternative distribution methods are not guaranteed
to function or remain supported.


Usage
-----

Usage documentation is **not yet available**.

Functionality, interfaces, and workflows are subject to change during
the Alpha phase. No guarantees are made regarding correctness,
completeness, or fitness for any particular operational purpose.


Lawful Use Only
---------------

This application is intended
**solely for lawful, authorized, and ethical use**.

The developer explicitly **does not authorize, support, or condone** any use of
this software for:

- Unauthorized access to systems or data
- Surveillance, profiling, or monitoring beyond legal authority
- Collection, exposure, or misuse of personal or sensitive information
- Any activity that violates privacy rights, organizational policy,
  or applicable local or international law

Any misuse, abuse, or unlawful deployment of this application is the
sole responsibility of the user.


Security
--------

Security vulnerabilities **must not** be reported through public issues.

Please refer to ``SECURITY.md`` for instructions on responsible vulnerability
reporting.


Contributing
------------

Contributions are subject to strict rules and discretionary acceptance.

Please read ``CONTRIBUTING.rst`` before submitting issues or pull requests.
Participation is a privilege, not a right.


Code of Conduct
---------------

All project-related interactions are governed by the project's
``CODE_OF_CONDUCT.rst``.


Legal Notice
------------

Use of this software is subject to important legal limitations and disclaimers.

Please read ``DISCLAIMER.rst`` before using, modifying, or distributing
this software.


License
-------

This project is licensed under the MIT License.

See the ``LICENSE`` file for full license text and terms.


..
    Badges


.. |codecov| image:: https://codecov.io/gh/MohsenHNSJ/HamyarPaygahPy/graph/badge.svg?token=NTP4DX8ZPK
    :target: CodeCov_
    :alt: Coverage status

.. |codspeed| image:: https://img.shields.io/badge/CodSpeed-Performance_Monitored-blue?logo=github
    :target: CodSpeed_
    :alt: CodSpeed

.. |commit-activity| image:: https://img.shields.io/github/commit-activity/m/MohsenHNSJ/HamyarPaygahPy?logo=git
    :target: `Commit Activity`_
    :alt: GitHub commit activity

.. |contributors| image:: https://img.shields.io/github/contributors/MohsenHNSJ/HamyarPaygahPy.svg
    :target: Contributors_
    :alt: Contributors

.. |documentation| image:: https://readthedocs.org/projects/unofficial-tabdeal-api/badge/?version=latest
    :target: Read-The-Docs_
    :alt: Documentation Status

.. |implementation| image:: https://img.shields.io/pypi/implementation/unofficial-tabdeal_api?logo=python
    :alt: PyPI - Implementation

.. |issues| image:: https://img.shields.io/github/issues/MohsenHNSJ/unofficial_tabdeal_api
    :target: Issues-link_
    :alt: GitHub Issues

.. |license| image:: https://img.shields.io/pypi/l/unofficial-tabdeal-api
    :target: `MIT License`_
    :alt: License

.. |maintenance| image:: http://unmaintained.tech/badge.svg
    :target: Unmaintained_
    :alt: No Maintenance Intended

.. |megalinter| image:: https://github.com/MohsenHNSJ/unofficial_tabdeal_api/actions/workflows/mega-linter.yml/badge.svg?branch=main
    :target: MegaLinter-Status_
    :alt: MegaLinter status

.. |mypy| image:: https://img.shields.io/badge/MyPy-Checked-blue
    :target: mypy-docs_
    :alt: Checked with MyPy

.. |nox| image:: https://img.shields.io/badge/%F0%9F%A6%8A-Nox-D85E00.svg
    :target: Nox_
    :alt: Nox

.. |openssf| image:: https://www.bestpractices.dev/projects/10685/badge
    :target: openssf-status_
    :alt: Open Source Security Foundation Best Practices Badge

.. |poetry| image:: https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json
    :target: poetry-website_
    :alt: Poetry

.. |pre-commit| image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit
    :target: Pre-commit_
    :alt: pre-commit

.. |pre-commit-ci| image:: https://results.pre-commit.ci/badge/github/MohsenHNSJ/unofficial_tabdeal_api/main.svg
    :target: Pre-commit-ci_
    :alt: pre-commit.ci status

.. |pull-requests| image:: https://img.shields.io/github/issues-pr/MohsenHNSJ/unofficial_tabdeal_api
    :target: `Pull Requests`_
    :alt: GitHub Pull Requests

.. |pydantic-badge| image:: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/pydantic/pydantic/main/docs/badge/v2.json
    :target: pydantic_
    :alt: Pydantic

.. |pylint| image:: https://img.shields.io/badge/linting-pylint-yellowgreen
    :target: pylint-website_
    :alt: Linting with Pylint

.. |release-to-pypi| image:: https://github.com/MohsenHNSJ/unofficial_tabdeal_api/actions/workflows/release-packge.yml/badge.svg
    :target: `Release to PyPI`_
    :alt: Release to PyPI status

.. |repository-size| image:: https://img.shields.io/github/repo-size/MohsenHNSJ/unofficial_tabdeal_api?color=BE81F7
    :alt: Repository Size

.. |ruff| image:: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json&style=flat-square
    :target: Ruff_
    :alt: Ruff

.. |scorecard| image:: https://api.scorecard.dev/projects/github.com/MohsenHNSJ/unofficial_tabdeal_api/badge
    :target: scorecard-rating_
    :alt: OpenSSF Scorecard

.. |sonar-bugs| image:: https://sonarcloud.io/api/project_badges/measure?project=MohsenHNSJ_unofficial_tabdeal_api&metric=bugs
    :target: sonar-qube-page_
    :alt: SonarQube Bugs

.. |sonar-code-smells| image:: https://sonarcloud.io/api/project_badges/measure?project=MohsenHNSJ_unofficial_tabdeal_api&metric=code_smells
    :target: sonar-qube-page_
    :alt: SonarQube Code Smells

.. |sonar-lines-of-code| image:: https://sonarcloud.io/api/project_badges/measure?project=MohsenHNSJ_unofficial_tabdeal_api&metric=ncloc
    :target: sonar-qube-page_
    :alt: SonarQube Lines of Code

.. |sonar-maintainability| image:: https://sonarcloud.io/api/project_badges/measure?project=MohsenHNSJ_unofficial_tabdeal_api&metric=sqale_rating
    :target: sonar-qube-page_
    :alt: SonarQube Maintainability Rating

.. |sonar-quality-gate| image:: https://sonarcloud.io/api/project_badges/measure?project=MohsenHNSJ_unofficial_tabdeal_api&metric=alert_status
    :target: sonar-qube-page_
    :alt: SonarQube Quality Gate

.. |sonar-qube| image:: https://sonarcloud.io/images/project_badges/sonarcloud-dark.svg
    :target: sonar-qube-page_
    :alt: SonarQube Cloud

.. |sonar-reliability| image:: https://sonarcloud.io/api/project_badges/measure?project=MohsenHNSJ_unofficial_tabdeal_api&metric=reliability_rating
    :target: sonar-qube-page_
    :alt: SonarQube Reliability Rating

.. |sonar-security| image:: https://sonarcloud.io/api/project_badges/measure?project=MohsenHNSJ_unofficial_tabdeal_api&metric=security_rating
    :target: sonar-qube-page_
    :alt: SonarQube Security Rating

.. |sonar-technical-debt| image:: https://sonarcloud.io/api/project_badges/measure?project=MohsenHNSJ_unofficial_tabdeal_api&metric=sqale_index
    :target: sonar-qube-page_
    :alt: SonarQube Technical Debt

.. |sonar-vulnerabilities| image:: https://sonarcloud.io/api/project_badges/measure?project=MohsenHNSJ_unofficial_tabdeal_api&metric=vulnerabilities
    :target: sonar-qube-page_
    :alt: SonarQube Vulnerabilities

.. |stars| image:: https://img.shields.io/github/stars/MohsenHNSJ/unofficial_tabdeal_api?style=social
    :target: Stars_
    :alt: Stars

.. |status| image:: https://img.shields.io/pypi/status/unofficial-tabdeal-api.svg
    :target: package-url_
    :alt: Status

.. |supported-python-versions| image:: https://img.shields.io/pypi/pyversions/unofficial-tabdeal-api?logo=python
    :target: package-url_
    :alt: Python Version

.. |synk| image:: https://img.shields.io/badge/Synk-white?logo=snyk&color=4C4A73
    :target: synk-website_
    :alt: Analyzed with Synk

.. |types| image:: https://img.shields.io/pypi/types/unofficial-tabdeal-api
    :alt: PyPI - Types

.. |version| image:: https://img.shields.io/pypi/v/unofficial-tabdeal-api.svg?logo=pypi
    :target: package-url_
    :alt: PyPI

.. |wheel| image:: https://img.shields.io/pypi/wheel/unofficial-tabdeal-api
    :alt: PyPI - Wheel


..
    Links
..
    Badges-links

.. _CodeCov: https://codecov.io/gh/MohsenHNSJ/HamyarPaygahPy
.. _CodSpeed: https://codspeed.io/MohsenHNSJ/HamyarPaygahPy?utm_source=badge
.. _Commit Activity: https://github.com/MohsenHNSJ/HamyarPaygahPy/graphs/commit-activity
.. _Contributors: https://github.com/MohsenHNSJ/HamyarPaygahPy/graphs/contributors

.. _Issues-link: https://github.com/MohsenHNSJ/unofficial_tabdeal_api/issues
.. _MegaLinter-Status: https://github.com/MohsenHNSJ/unofficial_tabdeal_api/actions?query=workflow%3AMegaLinter+branch%3Amain
.. _Nox: https://github.com/wntrblm/nox
.. _openssf-status: https://www.bestpractices.dev/projects/10685
.. _package-url: https://pypi.org/project/unofficial-tabdeal-api/
.. _poetry-website: https://python-poetry.org/
.. _Pre-commit: https://github.com/pre-commit/pre-commit
.. _Pre-commit-ci: https://results.pre-commit.ci/latest/github/MohsenHNSJ/unofficial_tabdeal_api/main
.. _Pull Requests: https://github.com/MohsenHNSJ/unofficial_tabdeal_api/pulls
.. _pydantic: https://pydantic.dev
.. _pylint-website: https://github.com/pylint-dev/pylint
.. _Read-The-Docs: https://unofficial-tabdeal-api.readthedocs.io/en/latest/?badge=latest
.. _Release to PyPI: https://github.com/MohsenHNSJ/unofficial_tabdeal_api/actions
.. _Ruff: https://github.com/astral-sh/ruff
.. _scorecard-rating: https://scorecard.dev/viewer/?uri=github.com/MohsenHNSJ/unofficial_tabdeal_api
.. _sonar-qube-page: https://sonarcloud.io/summary/new_code?id=MohsenHNSJ_unofficial_tabdeal_api
.. _Stars: https://github.com/MohsenHNSJ/unofficial_tabdeal_api/stargazers
.. _synk-website: https://snyk.io/
.. _Unmaintained: http://unmaintained.tech/
.. _mypy-docs: https://mypy.readthedocs.io/en/stable/

..
    Ignore-in-readthedocs
.. _MIT License: https://github.com/MohsenHNSJ/HamyarPaygahPy/blob/main/LICENSE
