|PyPI version| |Build Status|

~ UNDER CONSTRUCTION ~

project_cli
===========

A commandline interface for creating structured Python projects.


Installation
''''''''''''

::

   pip install project_cli


Usage
'''''

::

    python -m project_cli

If you trust ``project_cli`` to make the right decisions, you can say 'yes' to all prompts:

::

    python -m project_cli -y


Detailed information
''''''''''''''''''''
Here is an example project structure created by this tool for a runnable project:

::

    > proj_name
        __init__.py
        __main__.py
    > tests
        __init__.py
        context.py
        test_main.py
    README.rst
    setup.py

You can run your app as follows:

::

    python -m proj_name


You can run tests as follows:

::

    python -m unittest discover tests

You can also install your project in your own pip repository (or in a virtual environment) to make it runnable anywhere on your system:

::

    pip install -e .

Note: the ``-e`` flag is optional. It will keep your pip repository synchronized with your source code.

Meta
''''
Ramon Hagenaars - ramon.hagenaars@gmail.com

This structure was inspired by `Kenneth Reitz <https://github.com/kennethreitz/samplemod>`_.

.. |PyPI version| image:: https://badge.fury.io/py/project-cli.svg
   :target: https://badge.fury.io/py/project-cli

.. |Build Status| image:: https://travis-ci.org/ramonhagenaars/project-cli.svg?branch=master
   :target: https://travis-ci.org/ramonhagenaars/project-cli
