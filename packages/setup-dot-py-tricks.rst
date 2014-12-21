===============
setup.py tricks
===============

:date: 2014-12-19 12:00
:tags: python, ppoftw
:category: python
:slug: python-dot-py-tricks

.. image:: http://pydanny.com/static/setup.png
   :name: Setup.py tricks
   :align: center
   :alt: Setup.py tricks

Seasons greetings!

Before I begin, I want to make very clear that most of what I'm about to explain are **'tricks'**. They aren't "best practices",  and in at least one case, is possibly inadvisable.

Speaking of inadvisable practices, at some point I'll write a **'setup.py traps'** blog post, which are things I believe you should never, ever do in a **setup.py** module.

Tricks
=========

These are tricks I have to make package management in python_ a tiny bit easier. Before you attempt to implement them, I recommend you have at least basic experience with creating new packages. Two ways to learn about python packaging are the `New Library Sprint`_ (beginner friendly) and the `Python Packaging User Guide`_ (more advanced).

.. _`New Library Sprint`: http://audreyr.gitbooks.io/new-library-sprint/content/
.. _`Python Packaging User Guide`: https://python-packaging-user-guide.readthedocs.org

'python setup.py publish'
--------------------------

This is where it all started. One day I was looking at some of `Tom Christie's code`_ and discovered the `python setup.py publish`_ command inside the **setup.py** module of **Django Rest Framework**. It goes something like this:

.. code-block:: python

    # setup.py
    import os
    import sys

    # I'll discuss version tricks in a future blog post.
    version = "42.0.0"

    if sys.argv[-1] == 'publish':
        os.system("python setup.py sdist upload")
        os.system("python setup.py bdist_wheel upload")
        print("You probably want to also tag the version now:")
        print("  git tag -a %s -m 'version %s'" % (version, version))
        print("  git push --tags")
        sys.exit()

    # Below this point is the rest of the setup() function

What's awesome about this is that using this technique I don't have to look up the somewhat cryptic **python setup.py sdist upload** command, or the actually cryptic **python setup.py bdist_wheel upload**. Instead, when it's time to push one of my packages to PyPI_, I just type:

.. code-block:: bash

    $ python setup.py publish

Much easier to remember!

'python setup.py tag'
-----------------------

The problem with Tom Christie's **python setup.py publish** command is that it forces me to type out the **git tag** command. Okay, let's be honest, it forces me to copy/paste the output of my screen. Therefore, all on my very own, I 'invented' the **python setup.py tag** command:


.. code-block:: python

    # setup.py

    if sys.argv[-1] == 'tag':
        os.system("git tag -a %s -m 'version %s'" % (version, version))
        os.system("git push --tags")
        sys.exit()

Pretty nifty, eh? Now I don't have to remember so many cryptic git commands. And I get to shorten the `python setup.py publish` command:

.. code-block:: python

    if sys.argv[-1] == 'publish':
        os.system("python setup.py sdist upload")
        os.system("python setup.py bdist_wheel upload")
        sys.exit()

When I need to do a version release, I commit my code then type:

.. code-block:: bash

    $ python setup.py publish
    $ python setup.py tag

Why don't I combine the commands? Well, you aren't supposed to put things like 'RC1' or '-alpha' in your PyPI version names. By seperating the commands I have finer grained control over my package releases. I'm encouraged to place alpha, beta, and release candidates in git tags, rather than formal PyPI releases.

'python setup.py test'
------------------------

I'm fairly certain some of my readers are going to have a seriously problem with this trick. In fact, depending on the the response of those who manage Python's packaging infrastructure, it might be moved to my forthcoming 'traps' blog post.

Alrighty then...

I like `py.test`_. I've `blogged about the use of py.test`_. I try to use it everywhere. Yet, I'm really not a fan of how we're supposed tie it into **python setup.py test**. The precise moment I get uncomfortable with **py.test** is when it makes me add special classes into **setup.py**.

.. _`py.test`: http://pytest.org
.. _`blogged about the use of py.test`: http://www.pydanny.com/pytest-no-boilerplate-testing.html

Fortunately, there is another way:

.. code-block:: python

    if sys.argv[-1] == 'test':
        test_requirements = [
            'pytest',
            'flake8',
            'coverage'
        ]
        try:
            modules = map(__import__, test_requirements)
        except ImportError as e:
            err_msg = e.message.replace("No module named ", "")
            msg = "%s is not installed. Install your test requirments." % err_msg
            raise ImportError(msg)
        os.system('py.test')
        sys.exit()

Which means I get to use **py.test** and **python setup.py test** with a trivial addition of code:

.. code-block:: bash

    $ python setup.py test

In theory, one could run **pip install** on the missing requirements, or call them from a requirements file. However, since these are 'tricks', I like to keep things short and sweet. If I get enough positive results for this one I'll update this example to include calling of **pip** for missing requirements.

**note**: This doesn't mean I'm not using tox_. In fact, I use tox to call my version of **python setup.py test**.

What about subprocess?
=========================

There are those who will ask, "Why aren't you using the subprocess_ library for these shell commands?"

My answer to that question is, "Because if I need a nuclear weapon to kill a rabbit maybe I'm overdoing things." For these simple tricks, the **os.system()** function is good enough.

Why not just use a Makefile?
============================

While I code primarily on Mac OSX and Linux, most of my open source packages are used Windows. Thanks to AppVeyor_, I'm testing more and more of them in that environment. In fact, I'll probably be modifying these "tricks" to work better for Windows users.

Traps!
======

Stay tuned for my 'traps' blog post to come out early in 2015.

Updates
========

* 2014/12/21 - Added a note about using tox.
* 2014/12/21 - Added a note about Makefile and Windows

.. _tox: https://pypi.python.org/pypi/tox
.. _subprocess: https://docs.python.org/2/library/subprocess.html
.. _`_version.py`: https://github.com/eventbrite/eventbrite-sdk-python/blob/master/eventbrite/_version.py
.. _`Bartek Ogryczak`: https://github.com/vartec

.. _`Tom Christie's code`: https://github.com/tomchristie
.. _`python setup.py publish`: https://github.com/tomchristie/django-rest-framework/blob/971578ca345c3d3bae7fd93b87c41d43483b6f05/setup.py#L61-L67
.. _PyPI: https://pypi.python.org/pypi
.. _python: http://python.org
.. _AppVeyor: http://appveyor.com