========================================================
How To Create Installable Django Packages
========================================================

:date: 2015-11-20 18:30
:tags: python, python3, django, cheatsheet, ppoftw, djangopackages
:category: Django
:slug: how-to-create-installable-django-packages

.. image:: http://www.pydanny.com/static/django-package-470x246.png
  :name: Django Package Ecosystem: cookiecutter-djangopackage
  :align: center
  :alt: Django Package Ecosystem: cookiecutter-djangopackage
  :target: http://www.pydanny.com/how-to-create-installable-django-packages.html

What I mean by an "installable Django package": a reusable component that can be shared across Django projects, allowing us to combine our own efforts with others. Some examples include:

* `django-test-plus`_
* `django-crispy-forms`_
* `dj-stripe`_
* `dj-spam`_

.. _`django-crispy-forms`: https://www.djangopackages.com/packages/p/django-crispy-forms/
.. _`django-test-plus`: https://www.djangopackages.com/packages/p/django-test-plus/
.. _`dj-stripe`: https://www.djangopackages.com/packages/p/dj-stripe/
.. _`dj-spam`: https://www.djangopackages.com/packages/p/dj-spam/

Ever want to quickly create a similarly installable Django package to submit to PyPI_ and `Django Packages`_? One that goes beyond the basics described in the `Django tutorial`_? Specifically, a package that includes:

.. _`Django tutorial`: https://docs.djangoproject.com/en/1.8/intro/reusable-apps/

* Test runner so you don't need a example/test project (Although those can be useful).
* The important configuration in place: Travis, editorconfig, gitignore, etc.
* The important documentation in place: Readme, License, Read the Docs-ready Sphinx docs, etc.
* Static files ready to go.
* A base DTL/Jinja2 template ready to go.
* All those other fiddly bits not included in ``django-admin.py startapp`` that are hard to remember.

Well, here's how I do it.

Introducing cookiecutter-djangopackage
======================================

First, get Cookiecutter_.  Trust me, it's awesome:

.. code-block:: bash

    $ pip install cookiecutter

Now run it against this repo:

.. code-block:: bash

    $ cookiecutter https://github.com/pydanny/cookiecutter-djangopackage.git

You'll be prompted to enter some values. Enter them. Then an installable Django package will be built for you.

**Warning**: ``app_name`` must be a valid Python module name or you will have issues on imports.

Enter the new package (in my case, I called it 'newpackage') and look around. Open up the ``AUTHORS.rst``, ``setup.py``, or ``README.rst`` files and you'll see your input inserted into the appropriate locations.

Speaking of the ``README.rst``, that file includes instructions for putting the new package on PyPI_ and `Django Packages`_.

.. code-block:: bash

    newpackage
    ├── .editorconfig
    ├── .gitignore
    ├── .travis.yml
    ├── AUTHORS.rst
    ├── CONTRIBUTING.rst
    ├── HISTORY.rst
    ├── LICENSE
    ├── MANIFEST.in
    ├── Makefile
    ├── README.rst
    ├── newpackage
    │   ├── __init__.py
    │   ├── models.py
    │   ├── static
    │   │   ├── css
    │   │   │   └── newpackage.css
    │   │   ├── img
    │   │   │   └── .gitignore
    │   │   └── js
    │   │       └── newpackage.js
    │   └── templates
    │       └── cheese
    │           └── base.html
    ├── docs
    │   ├── Makefile
    │   ├── authors.rst
    │   ├── conf.py
    │   ├── contributing.rst
    │   ├── history.rst
    │   ├── index.rst
    │   ├── installation.rst
    │   ├── make.bat
    │   ├── readme.rst
    │   └── usage.rst
    ├── requirements-test.txt
    ├── requirements.txt
    ├── requirements_dev.txt
    ├── runtests.py
    ├── setup.cfg
    ├── setup.py
    ├── tests
    │   ├── __init__.py
    │   └── test_models.py
    └── tox.ini

Now, instead of monkeying around for awhile doing copy/paste package setup, I'm immediately ready to write code.

Summary
=============

``cookiecutter-djangopackage`` does a lot, but even with its tight focus on package creation it could do more. Some of the things I would love to see included in the future:

* Option for Appveyor CI support
* Option to replace ``django.test`` with ``py.test``.
* Generation of model boilerplate, admin, and CRUD views.
* More in the `issue tracker`_.

Try it out and let me know what you think. I'm open to new ideas and receiving pull requests.

.. _`issue tracker`: https://github.com/pydanny/cookiecutter-djangopackage/issu
.. _PyPI: pypi.python.org/pypi
.. _`Django Packages`: https://wwww.djangopackages.com
.. _`cookiecutter.json`: https://github.com/pydanny/cookiecutter-djangopackage/blob/master/cookiecutter.json
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
