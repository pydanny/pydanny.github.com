========================================================
How To Create Installable Django Packages
========================================================

:date: 2015-11-12 09:00
:tags: python, python3, django, cheatsheet, ppoftw,
:category: Django
:slug: how-to-create-installable-django-packages.rst
:status: draft

Ever want to quickly create an installable Django package to submit to PyPI_ and `Django Packages`_? One that goes beyond the basics described in the `Django tutorial`_? Specifically, a package that includes:

.. _`Django tutorial`: https://docs.djangoproject.com/en/1.8/intro/reusable-apps/

* Configuration in place: Travis, editorconfig, gitignore, etc.
* Read the Docs-ready Sphinx docs.
* Test runner so you don't need a example/test project (Although those can be useful).
* Static files ready to go.
* A base DTL/Jinja2 template ready to go.
* Lots more!

Well, assuming I'm in a virtualenv here's how I do it:

.. code-block:: bash

    (env) $ pip install cookiecutter
    (env) $ cookiecutter Cloning into 'cookiecutter-pypackage'...
    remote: Counting objects: 183, done.
    remote: Compressing objects: 100% (100/100), done.
    remote: Total 183 (delta 87), reused 161 (delta 70)
    Receiving objects: 100% (183/183), 29.36 KiB | 0 bytes/s, done.
    Resolving deltas: 100% (87/87), done.
    Checking connectivity... done
    full_name (default is "Your name")? Daniel Roy Greenfeld
    email (default is "you@example.com")? pydanny@example.com
    github_username (default is "yourname")? pydanny
    project_name (default is "dj-package")? cheese
    repo_name (default is "dj-package")? cheese
    app_name (default is "djpackage")? cheese
    ... snip for brevity

See how it asks my full name? Well, at this point, Cookiecutter_ begins to ask a number of questions. These questions are actually specified in the `cookiecutter.json`_ file for `cookiecutter-djangopackage`_.

Once you've answered everything that cookiecutter-djangopackage wants, it generates your project. Let's go check. It should have generated something like this:

.. code-block:: bash

    $ tree cheese
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
    ├── cheese
    │   ├── __init__.py
    │   ├── models.py
    │   ├── static
    │   │   ├── css
    │   │   │   └── cheese.css
    │   │   ├── img
    │   │   │   └── .gitignore
    │   │   └── js
    │   │       └── cheese.js
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

Now, instead of monkeying around with how to setup my project, I'm ready to write the code.



.. _PyPI: pypi.python.org/pypi
.. _`Django Packages`: https://wwww.djangopackages.com
.. _`cookiecutter.json`: https://github.com/pydanny/cookiecutter-djangopackage/blob/master/cookiecutter.json
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
