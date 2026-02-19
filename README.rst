=============
Hamyar Paygah
=============

..
    Badges section

.. list-table::
    :stub-columns: 1

    * - Package
      - |poetry| |dev-release| |stable-release|
    * - Quality Assurance
      - |sonar-quality-gate| |sonar-reliability| |sonar-maintainability| |sonar-technical-debt| |sonar-bugs| |sonar-code-smells|
    * - Stats
      - |contributors| |stars| |issues| |pull-requests| |sonar-lines-of-code| |repository-size|
    * - Tests
      - |nox| |codspeed| |pre-commit-ci| |codecov| |scorecard|
    * - Security
      - |synk| |sonar-security| |sonar-vulnerabilities| |openssf| |openssf-baseline|
    * - Linters
      - |ruff| |pre-commit| |megalinter| |mypy| |pylint|
    * - Activity
      - |commit-activity|
    * - Documentation
      - |documentation|


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
- Qt (GUI framework)

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

.. |documentation| image:: https://hamyarpaygahpy.readthedocs.io/en/latest/?version=latest
    :target: Read-The-Docs_
    :alt: Documentation Status

.. |issues| image:: https://img.shields.io/github/issues/MohsenHNSJ/HamyarPaygahPy
    :target: Issues-link_
    :alt: GitHub Issues

.. |megalinter| image:: https://github.com/MohsenHNSJ/HamyarPaygahPy/actions/workflows/mega-linter.yml/badge.svg?branch=main
    :target: MegaLinter-Status_
    :alt: MegaLinter status

.. |mypy| image:: https://img.shields.io/badge/MyPy-Checked-blue
    :target: mypy-docs_
    :alt: Checked with MyPy

.. |nox| image:: https://img.shields.io/badge/%F0%9F%A6%8A-Nox-D85E00.svg
    :target: Nox_
    :alt: Nox

.. |openssf| image:: https://www.bestpractices.dev/projects/11675/badge
    :target: openssf-status_
    :alt: Open Source Security Foundation Best Practices Badge

.. |openssf-baseline| image:: https://www.bestpractices.dev/projects/11675/baseline
    :target: openssf-status_
    :alt: Open Source Security Foundation Baseline Badge

.. |poetry| image:: https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json
    :target: poetry-website_
    :alt: Poetry

.. |pre-commit| image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit
    :target: Pre-commit_
    :alt: pre-commit

.. |pre-commit-ci| image:: https://results.pre-commit.ci/badge/github/MohsenHNSJ/HamyarPaygahPy/main.svg
    :target: Pre-commit-ci_
    :alt: pre-commit.ci status

.. |pull-requests| image:: https://img.shields.io/github/issues-pr/MohsenHNSJ/HamyarPaygahPy
    :target: `Pull Requests`_
    :alt: GitHub Pull Requests

.. |pylint| image:: https://img.shields.io/badge/linting-pylint-yellowgreen
    :target: pylint-website_
    :alt: Linting with Pylint

.. |dev-release| image:: https://github.com/MohsenHNSJ/HamyarPaygahPy/actions/workflows/dev_release_executable.yml/badge.svg
    :target: `Dev Release`_
    :alt: Development Release

.. |stable-release| image:: https://github.com/MohsenHNSJ/HamyarPaygahPy/actions/workflows/release_executable.yml/badge.svg
    :target: `Stable Release`_
    :alt: Stable Release

.. |repository-size| image:: https://img.shields.io/github/repo-size/MohsenHNSJ/HamyarPaygahPy?color=BE81F7
    :alt: Repository Size

.. |ruff| image:: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json&style=flat-square
    :target: Ruff_
    :alt: Ruff

.. |scorecard| image:: https://api.scorecard.dev/projects/github.com/MohsenHNSJ/HamyarPaygahPy/badge
    :target: scorecard-rating_
    :alt: OpenSSF Scorecard

.. |sonar-bugs| image:: https://sonarcloud.io/api/project_badges/measure?project=MohsenHNSJ_HamyarPaygahPy&metric=bugs
    :target: sonar-qube-page_
    :alt: SonarQube Bugs

.. |sonar-code-smells| image:: https://sonarcloud.io/api/project_badges/measure?project=MohsenHNSJ_HamyarPaygahPy&metric=code_smells
    :target: sonar-qube-page_
    :alt: SonarQube Code Smells

.. |sonar-lines-of-code| image:: https://sonarcloud.io/api/project_badges/measure?project=MohsenHNSJ_HamyarPaygahPy&metric=ncloc
    :target: sonar-qube-page_
    :alt: SonarQube Lines of Code

.. |sonar-maintainability| image:: https://sonarcloud.io/api/project_badges/measure?project=MohsenHNSJ_HamyarPaygahPy&metric=sqale_rating
    :target: sonar-qube-page_
    :alt: SonarQube Maintainability Rating

.. |sonar-quality-gate| image:: https://sonarcloud.io/api/project_badges/measure?project=MohsenHNSJ_HamyarPaygahPy&metric=alert_status
    :target: sonar-qube-page_
    :alt: SonarQube Quality Gate

.. |sonar-qube| image:: https://sonarcloud.io/images/project_badges/sonarcloud-dark.svg
    :target: sonar-qube-page_
    :alt: SonarQube Cloud

.. |sonar-reliability| image:: https://sonarcloud.io/api/project_badges/measure?project=MohsenHNSJ_HamyarPaygahPy&metric=reliability_rating
    :target: sonar-qube-page_
    :alt: SonarQube Reliability Rating

.. |sonar-security| image:: https://sonarcloud.io/api/project_badges/measure?project=MohsenHNSJ_HamyarPaygahPy&metric=security_rating
    :target: sonar-qube-page_
    :alt: SonarQube Security Rating

.. |sonar-technical-debt| image:: https://sonarcloud.io/api/project_badges/measure?project=MohsenHNSJ_HamyarPaygahPy&metric=sqale_index
    :target: sonar-qube-page_
    :alt: SonarQube Technical Debt

.. |sonar-vulnerabilities| image:: https://sonarcloud.io/api/project_badges/measure?project=MohsenHNSJ_HamyarPaygahPy&metric=vulnerabilities
    :target: sonar-qube-page_
    :alt: SonarQube Vulnerabilities

.. |stars| image:: https://img.shields.io/github/stars/MohsenHNSJ/HamyarPaygahPy?style=social
    :target: Stars_
    :alt: Stars

.. |synk| image:: https://img.shields.io/badge/Synk-white?logo=snyk&color=4C4A73
    :target: synk-website_
    :alt: Analyzed with Synk

..
    Links
..
    Badges-links

.. _CodeCov: https://codecov.io/gh/MohsenHNSJ/HamyarPaygahPy
.. _CodSpeed: https://codspeed.io/MohsenHNSJ/HamyarPaygahPy?utm_source=badge
.. _Commit Activity: https://github.com/MohsenHNSJ/HamyarPaygahPy/graphs/commit-activity
.. _Contributors: https://github.com/MohsenHNSJ/HamyarPaygahPy/graphs/contributors
.. _Issues-link: https://github.com/MohsenHNSJ/HamyarPaygahPy/issues
.. _MegaLinter-Status: https://github.com/MohsenHNSJ/HamyarPaygahPy/actions?query=workflow%3AMegaLinter+branch%3Amain
.. _Nox: https://github.com/wntrblm/nox
.. _synk-website: https://snyk.io/
.. _Stars: https://github.com/MohsenHNSJ/HamyarPaygahPy/stargazers
.. _mypy-docs: https://mypy.readthedocs.io/en/stable/
.. _Pre-commit: https://github.com/pre-commit/pre-commit
.. _pylint-website: https://github.com/pylint-dev/pylint
.. _Ruff: https://github.com/astral-sh/ruff
.. _poetry-website: https://python-poetry.org/
.. _Read-The-Docs: https://hamyarpaygahpy.readthedocs.io/en/latest/?badge=latest
.. _Pull Requests: https://github.com/MohsenHNSJ/HamyarPaygahPy/pulls
.. _Pre-commit-ci: https://results.pre-commit.ci/latest/github/MohsenHNSJ/HamyarPaygahPy/main
.. _openssf-status: https://www.bestpractices.dev/projects/11675/
.. _scorecard-rating: https://scorecard.dev/viewer/?uri=github.com/MohsenHNSJ/HamyarPaygahPy
.. _Dev Release: https://github.com/MohsenHNSJ/HamyarPaygahPy/actions
.. _Stable Release: https://github.com/MohsenHNSJ/HamyarPaygahPy/actions
.. _sonar-qube-page: https://sonarcloud.io/summary/new_code?id=MohsenHNSJ_HamyarPaygahPy
