=======================================
pytest: no-boilerplate testing (part 3)
=======================================

:date: 2014-01-17 12:00
:tags: python, django, testing, ppoftw
:category: book
:slug: pytest-no-boilerplate-testing-3

In my previous `blog post`_ I covered writing exception-based assertions and fixtures. Today I'm going to close things out by demonstrating how to change the behavior of pytest_ and how to integrate it with **Django** and ``setup.py``.

Changing the Behavior of **pytest**
===================================

When **pytest** is called, either via the command-line or by ``pytest.main()``, it `looks for a configuration file`_ called either ``pytest.ini``, ``tox.ini``, and ``setup.cfg``. If it finds a configuration file, it follows standard practices for those things. In the following example, I demonstrating searching for tests inside of all Python files while ignoring the **_build** directories:

.. code-block:: ini

    # pytest.ini (or tox.ini or setup.cfg)
    [pytest] # You must put pytest-related controls in a 'pytest' block
    python_files=*.py  # Run tests against all python modules
    norecursedirs = _build # Don't look inside of _build directories

Changing **pytest** Behavior Dynamically
-----------------------------------------

This is pretty nice, but if I need to ignore certain Python modules like ``setup.py``? I can do this by creating a ``conftest.py`` module and defining a ``collect_ignore`` variable.

.. code-block:: python

    # conftest.py
    collect_ignore = ["setup.py", "conftest.py"]
    
The ``conftest.py`` module can actually be defined per directory. So if test behavior needs to change in different packages, just create additional ``conftest.py`` modules. It's simple to do, but really powerful.

The ``conftest`` module is capable of a lot of other things. Right now there doesn't seem to be a page that documents it in full, so I'm considering submitting a documentation pull request. In the meantime, I live off the ``conftest.py`` `search results`_.

**pytest** is Plug-In Driven
----------------------------

One feature I really like about **pytest** is that much of it's default capabilities are driven by about 20 plug-ins. It's a sign of maturity that not only does it have plug-ins, but that most of the time this feature is transparent. You can add new plug-ins to your project in a `number of ways`_, including ``pip`` installation from PyPI_. For locally defined plug-ins I prefer to rely on explicit ``conftest.py`` declarations:

.. code-block:: python
    
    # conftest.py
    collect_ignore = ["setup.py", "conftest.py"]
    pytest_plugins = ["dream_plugin", "dream.utils.testplugin"]
    
There are a lot of `third-party pytest plug-ins`_, which brings me to the next major section: Integration with other tools and frameworks.

.. _`third-party pytest plug-ins`: https://pypi.python.org/pypi?%3Aaction=search&term=pytest-&submit=search

Django Integration is Just a Plug-In Away
==========================================

If you want to use **pytest** instead of **Django**'s test runner and also get the power of function-based tests, fixture functions, improved test discover, and all the stuff I haven't covered, then check out and/or ``pip`` install `pytest-django`_. My *admittedly brief* usage on some of my existing projects demonstrates that my existing **unittest**-style tests work.

Twisted (and more) Integration is Just a Plug-In Away
------------------------------------------------------

The same goes for Twisted_ thanks to `pytest-twisted`_. There is also a Pyramid_ plug-in that was just released_. I'm not sure if it needs it, but I guess there will be Flask_ plug-in soon.

Integration With ``setup.py``
=============================

Fortunately, the documentation for **pytest** covers both adding a new `setup.py command-classes for pytest`_ and `actual integration`_. That's useful, but what I've found even more useful is the `setup.py that Jeff Knupp wrote for his Sandman project`_. 

**Note:** If you aren't experienced with writing Python packages and readying them for **PyPI**, I recommend you read `Jeff Knupp's blog post on open sourcing projects`_. Amongst other things, it has an in-depth discussion about integration of **pytest** with ``setup.py``. Anything I would write on the subject of ``setup.py`` integration would be just a cheap knock-off of Jeff's excellent work.

Summary
=======

Tests are an important part of any project. While they increase the stability of a project, that unfortunately can come at the cost of the boredom of writing tests. Fortunately, **pytest** goes a long way to alleviating that boredom while also empowering Python code authors with lots of additional useful tools. I'm delighted to have finally discovered **pytest**. In the short time I've used **pytest**, it's saved me days, if not weeks, of tedious work.


.. _`Jeff Knupp's blog post on open sourcing projects`: http://www.jeffknupp.com/blog/2013/08/16/open-sourcing-a-python-project-the-right-way/
.. _`setup.py that Jeff Knupp wrote for his Sandman project`: https://github.com/jeffknupp/sandman/blob/develop/setup.py

.. _`setup.py command-classes for pytest`: http://pytest.org/latest/goodpractises.html#integrating-with-distutils-python-setup-py-test
.. _`actual integration`: http://pytest.org/latest/goodpractises.html#integration-with-setuptools-test-commands


.. _`pytest-django`: https://pypi.python.org/pypi/pytest-django

.. _`blog post`: http://pydanny.com/pytest-no-boilerplate-testing-3.html
.. _pytest: http://pytest.org/
.. _`looks for a configuration file`: http://pytest.org/latest/customize.html#how-test-configuration-is-read-from-configuration-ini-files
.. _`search results`: http://pytest.org/latest/search.html?q=conftest&check_keywords=yes&area=default
.. _`number of ways`: http://pytest.org/latest/plugins.html#plugin-discovery-order-at-tool-startup
.. _PyPI: https://pypi.python.org/pypi/
.. _`pytest-twisted`: https://pypi.python.org/pypi/pytest-twisted
.. _Twisted: http://twistedmatrix.com/
.. _Pyramid: http://www.pylonsproject.org/
.. _released: https://pypi.python.org/pypi/pytest_pyramid
.. _Flask: http://flask.pocoo.org/