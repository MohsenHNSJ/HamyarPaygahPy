============================
Contributing to This Project
============================

..
    Don't render this section in ReadTheDocs, as it is not needed there.

.. only:: never

    .. contents::
        :local:
        :depth: 2

* `Source Code`_
* Documentation_
* `Issue Tracker`_
* `Code of Conduct`_

Purpose
-------

This document defines the rules and expectations for contributing to this project.
Participation in contributions, including but not limited to issues, pull requests,
documentation, or other code submissions, constitutes acceptance of these terms.

Contributions are voluntary and made at the contributor's own risk.
The maintainers reserve exclusive authority over all contributions.

General Guidelines
------------------

All contributions must:

* Follow the coding, formatting, and documentation standards defined in the project.
* Be submitted in accordance with the branching and pull request process, if applicable.
* Be relevant, constructive, and in good faith.
* Comply with applicable laws and the `Code of Conduct`_.

Submissions that do not meet these criteria may be rejected without explanation.

Security and Sensitive Issues
-----------------------------

**Do not submit security vulnerabilities through issues or pull requests.**
All security-related concerns must be reported according to `SECURITY.md`_.

Failure to follow security reporting procedures may result in immediate rejection of the submission
and/or reporting to relevant authorities.

Scope of Contributions
----------------------

The maintainers reserve the right to:

* Accept, reject, or modify contributions at their sole discretion.
* Define which versions or branches are supported for contributions.
* Disregard contributions that are outside the intended scope or violate security or conduct policies.

No commitment is made to merge contributions, respond to submissions, or provide ongoing support.

No Compensation or Liability
----------------------------

Contributors acknowledge and agree that:

* No compensation or credit is guaranteed beyond attribution in commits or documentation.
* All contributions are provided **“as is”**.
* Maintainers and the developer disclaim all liability for any damages, losses, or consequences
  arising from submitted contributions.

Reporting Issues
----------------

General issues unrelated to security may be reported through `Issue Tracker`_.
Reports must be relevant, clear, and reproducible to be considered.

When filing an issue, make sure to answer these questions:

* Which operating system and Python version are you using?
* Which version of this project are you using?
* What did you do?
* What did you expect to see?
* What did you see instead?
* Any details about your local setup that might be helpful in troubleshooting
* An effective way to get your bug fixed is to provide a test case, and/or steps to reproduce the issue.

Security-sensitive reports must **only** follow the `SECURITY.md`_ reporting process.


Fixing Issues
-------------

Look through the `Issue Tracker`_ for bugs. Anything tagged with :code:`bug` and :code:`help wanted` is open to whoever wants to fix it.

Request Features
----------------

Request features on the `Issue Tracker`_.

If you are proposing a new feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to add.

Implement Features
------------------

Look through the `Issue Tracker`_ for features. Anything tagged with :code:`enhancement` and :code:`help wanted` is open to whoever wants to Add it.

Development Environment
-----------------------

Use `VS Code`_ `Dev Containers`_ extension and clone this repository.

Requirements will be installed automatically

Poetry_ manages virtual environments and dependencies for this project.

pre-commit_ manages linters, static analysis, and other tools for this project.

Install pre-commit_ hooks after cloning, run:

.. code-block:: sh

    pre-commit install

Using pre-commit_ ensures PRs match the linting requirements of the codebase.

Install vcxsrv_ on your local machine to enable GUI applications
from the dev container.

Open vcxsrv_ and configure it with the following settings:

* Multiple windows
* Start no client
* Disable access control

Or load it with ``config.xlaunch`` file from ``.devcontainer/vcxsrv/`` directory.

Possible issues
---------------

If you encounter an error about not setting :code:`user.name` and :code:`user.email` for committing with git:

* Run the following commands on your **local machine** terminal to set-up your git connection

.. code-block:: sh

    git config --global user.name "YOUR_USER_NAME"

    git config --global user.email "YOUR_EMAIL"


* Rebuild the container

If you encounter an error about not having the permission to .git/object for committing with git:
:code:`insufficient permission for adding an object to repository database .git/objects`

* Run the following commands on dev container terminal:

.. code-block:: sh

    sudo chmod -R a+rwX .

    sudo find . -type d -exec chmod g+s '{}' +

* Check the output of shared repository:

.. code-block:: sh

    git config core.sharedRepository

* If the output of last command is empty or doesn't include :code:`group` , :code:`true` or :code:`1`, run the following:

.. code-block:: sh

    git config core.sharedRepository group

* Finally, fix the root cause by following the answer from stackoverflow_.

Documenting Code
----------------

Whenever possible, please add docstrings to your code.

This project follows the `google-style docstrings`_ format.

To confirm docstrings are valid, build the docs by running :code:`nox -t docs`

Good docstrings include information like:

* If the intended use-case doesn't appear clear, what purpose does this function serve? When should someone use it?
* What happens during errors/edge-cases.
* When dealing with physical values, include units.

Testing
-------

The pytest_ framework provides unit testing for this project.

Ideally, all new code is paired with new unit tests to exercise that code.

If fixing a bug, consider writing the test first to confirm the existence of the bug, and to confirm that the new code fixes it.

Unit tests should only test a single concise body of code.

Run the full test suite:

.. code-block:: sh

    nox -t test

Lint using Ruff_:

.. code-block:: sh

    nox -t fix

Typecheck using MyPy_:

.. code-block:: sh

    nox -t type

Build and live-preview documentation:

.. code-block:: sh

    nox -t preview

Run pre-commit_ hooks:

.. code-block:: sh

    nox -t pre-commit

List the available Nox_ sessions:

.. code-block:: sh

    nox --list

Unit tests are located in the *tests* directory,
and are written using the pytest_ testing framework.

Coding style
------------

In an attempt to keep consistency and maintainability in the code-base,
here are some high-level guidelines for code that might not be enforced by linters:

* Use f-strings.
* Keep/cast path variables as :code:`pathlib.Path` objects. Don't use :code:`os.path`.
  For public-facing functions, cast path arguments immediately to :code:`Path`.
* Avoid deeply nested code. Techniques like returning early and breaking up a complicated function into smaller functions results in easier-to-read and test code.
* Consider if you are double-name-spacing and how modules are meant to be imported.
  for example, it might be better to name a function :code:`read` instead of :code:`image_read` in the module :code:`my_package/image.py`.
  Consider the module name-space and check if it's flattened in :code:`__init__.py`.

Pull Requests
-------------

Open a `pull request`_ and target the ``dev`` branch to submit changes to this project.

Don't target the ``main`` branch, as it's reserved for releases.

Your pull request needs to meet the following guidelines for acceptance:

* The Nox test suite must pass without errors and warnings.
* Include unit tests. This project maintains high code coverage.
* If your changes add capability, update the documentation accordingly.

Feel free to submit early, iteration and improvement can happen as needed.

It's recommended to open an issue before starting work on anything.
This will allow a chance to discuss your approach with the owners and confirm it fits the project's direction.

Amendments
----------

This contributing policy may be updated or replaced at any time without notice.
Continued contributions constitute acceptance of the current version.


..
    Links
.. _Issue Tracker: https://github.com/MohsenHNSJ/HamyarPaygahPy/issues
.. _Source Code: https://github.com/MohsenHNSJ/HamyarPaygahPy
.. _VS Code: https://code.visualstudio.com/
.. _Dev Containers : https://containers.dev/
.. _pre-commit: https://pre-commit.com/
.. _Poetry: https://python-poetry.org/
.. _SECURITY.md: https://github.com/MohsenHNSJ/HamyarPaygahPy/blob/main/SECURITY.md
.. _stackoverflow: https://stackoverflow.com/questions/6448242/git-push-error-insufficient-permission-for-adding-an-object-to-repository-datab/6448326#6448326
.. _google-style docstrings: https://sphinxcontrib-napoleon.readthedocs.io/en/latest/#google-vs-numpy
.. _pytest: https://docs.pytest.org/en/stable/
.. _Ruff: https://docs.astral.sh/ruff/
.. _MyPy: https://www.mypy-lang.org/
.. _Nox: https://nox.thea.codes/en/stable/index.html
.. _pull request: https://github.com/MohsenHNSJ/HamyarPaygahPy/pulls
.. _vcxsrv: https://github.com/marchaesen/vcxsrv

..
    Ignore-in-readthedocs
.. _Documentation: https://hamyarpaygahpy.readthedocs.io/en/latest/
.. _Code of Conduct: https://github.com/MohsenHNSJ/HamyarPaygahPy/blob/main/CODE_OF_CONDUCT.rst
