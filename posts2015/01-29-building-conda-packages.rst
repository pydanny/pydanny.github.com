======================================================
Building Conda Packages for Multiple Operating Systems
======================================================

:date: 2015-01-29 18:00
:tags: python, pypi, python3, conda, cookiecutter, binstar, packaging, howto
:category: python
:slug: building-conda-packages-for-multiple-operating-systems

On the Cookiecutter_ project, recently we added conda_ to the open source packaging systems we officially support (You can find Cookiecutter on PyPI_, homebrew_, and apparently some Linux distros).

.. _Cookiecutter: https://github.com/audreyr/cookiecutter


Creating a conda recipe from a PyPI package
-------------------------------------------

Prequisites:

* A `conda binary`_ installed.
* A package deployed to PyPI_ (in our case, https://pypi.python.org/pypi/cookiecutter/0.9.1).

.. _homebrew: https://github.com/Homebrew/homebrew/blob/master/Library/Formula/cookiecutter.rb
.. _PyPI: https://pypi.python.org/pypi/cookiecutter
.. _conda: http://conda.pydata.org/
.. _`conda binary`: http://conda.pydata.org/miniconda.html#miniconda

Once those are ready, create a conda recipe for Cookiecutter.

.. code-block:: bash

    $ conda skeleton pypi cookiecutter

This will create a conda recipe, which is a directory named ``cookiecutter`` that contains several text files.

Inside the new ``cookiecutter`` recipe directory, find the ``meta.yaml`` file and change the appropriate sections to have this content:

.. code-block:: yaml

    source:
        # Change to match the most recent release
        git_tag: 0.9.1
        git_url: https://github.com/audreyr/cookiecutter.git

    package:
        name: cookiecutter
        version: {{ environ['GIT_DESCRIBE_TAG'] }}

    build:
        number: {{ environ.get('GIT_DESCRIBE_NUMBER', 0) }}

        # Note that this will override the default build string with the Python
        # and NumPy versions
        string: {{ environ.get('GIT_BUILD_STR', '') }}


Building a conda package
------------------------

Use the conda recipe to build a package for my operating system (in this case, Mac OS X):

.. code-block:: bash

    $ conda build cookiecutter

This creates a Cookiecutter conda package at ``~/miniconda/conda-bld/osx-64/cookiecutter-0.9.1_BUILDNUM.tar.bz2``.

**Note:** The official conda recipe for **cookiecutter** is at https://github.com/conda/conda-recipes/tree/master/cookiecutter.

Converting the conda package to other systems
---------------------------------------------

Let's convert that to Windows and Linux systems:

.. code-block:: bash

    $ conda convert ~/miniconda/conda-bld/osx-64/cookiecutter-0.9.1_BUILDNUM.tar.bz2 -p all

This creates five new directories, each with a new package. It looks something like this:

.. code-block:: bash

    $ ls
    linux-32
    linux-64
    osx-64
    win-32
    win-64

Each one of these directories contains a conda build also named ``cookiecutter-0.9.1_BUILDNUM.tar.bz2``.

**Note:** I never left the Mac OSX operating system, yet I have packages that are pretty much garaunteed to work on Windows and Linux. That said, Cookiecutter is pure python and it's dependencies already have conda packages. I haven't tried this yet on anything that includes compiling C or C++, much less Fortran.

Uploading conda packages to Binstar
------------------------------------

With these packages created, it's time to upload them to binstar_, the primary conda package index.

First, `register your binstar account`_.

.. _`register your binstar account`: https://binstar.org/account/register

Then use conda to install the binstar client:

.. code-block:: bash

    $ conda install binstar

Finally, start uploading the new packages:

.. code-block:: bash

    $ binstar upload linux-32/cookiecutter-0.9.1-BUILDNUM.tar.bz2
    $ binstar upload linux-64/cookiecutter-0.9.1-BUILDNUM.tar.bz2
    $ binstar upload osx-64/cookiecutter-0.9.1-BUILDNUM.tar.bz2
    $ binstar upload win-32/cookiecutter-0.9.1-BUILDNUM.tar.bz2
    $ binstar upload win-64/cookiecutter-0.9.1-BUILDNUM.tar.bz2

.. _binstar: http://binstar.org

`Check out the results of my work`_ or take a look right below at what's on binstar_:

.. image:: http://pydanny.com/static/packages.png
   :name: packages
   :align: center
   :target: https://binstar.org/search?q=cookiecutter
   :height: 138
   :width: 500

.. _`Check out the results of my work`: https://binstar.org/pydanny/cookiecutter

Try installing Cookiecutter with conda!
----------------------------------------

If you have **conda** installed, you should be able to get Cookiecutter thus:

.. code-block:: bash

    $ conda config --add channels https://conda.binstar.org/pydanny
    $ conda install cookiecutter

Summary
--------

Writing about how to package software is hard, so figuring this out was a `bit of detective work`_. I think that's going to change, as the company behind conda, `Continuum Analytics`_ has stated their intentions to improve conda's documentation. Furthermore, just as many `for-python cookiecutter templates`_ include carefully researched ``setup.py`` modules for use with ``distutils``, in 2015 I think we'll begin to see many of these templates include carefully research conda recipes and instructions.

Many thanks go to `Fernando Perez`_ for inspiring me to actually delve into conda. `Travis Swicegood`_ gave me some useful pointers. Last, but not least, none of this would have been figured out without the help of `Wes Turner`_.

Updates
-------

* 2015/01/31 - Fixed a broken binstar link thanks to Russ Ferriday.
* 2015/01/30 - Wes Turner corrected a couple typos in the conda command statements.

.. _`Travis Swicegood`: https://twitter.com/tswicegood
.. _`Fernando Perez`: https://twitter.com/fperez_org
.. _`Wes Turner`: https://twitter.com/westurner
.. _`Continuum Analytics`: http://www.continuum.io/
.. _`for-python cookiecutter templates`: https://github.com/audreyr/cookiecutter#python
.. _`bit of detective work`: https://github.com/audreyr/cookiecutter/issues/232#issuecomment-71552905