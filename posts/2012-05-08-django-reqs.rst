=================================
Django Requirements for a project
=================================

:date: 2012-05-09 08:00
:tags: python, django
:category: Django

Today I'm starting a new project. I'm working as fast as I can and hope to launch on Friday. What are my package dependencies?

`Django==1.4`_
==============

Unlike my last quick project which was Flask, this effort really falls into Django's sweet spot. I need sessions, forms, templates, and models to do things in a pattern that falls into Django's sweet spot.

.. _`Django==1.4`: http://pypi.python.org/pypi/Django/1.4

`psycopg2==2.4.5`_
==================

I need transactions and hard-type validation in the database, which means PostGreSQL. If I didn't need transactions or the hard-type validation I would consider MongoDB instead.

.. _`psycopg2==2.4.5`: http://pypi.python.org/pypi/psycopg2

`django-debug-toolbar==0.9.4`_
===============================

Because not using this tool is insane.

.. _`django-debug-toolbar==0.9.4`: http://pypi.python.org/pypi/django-debug-toolbar


`django-extensions==0.8`_
==========================

Because I never want to write my own ``BaseTimeStampModel`` ever again. :-)

.. _`django-extensions==0.8`: http://pypi.python.org/pypi/django-extensions

`South==0.7.5`_
================

Django gives you the freedom to migrate data in the way you want. The way I want to do it is via South.

.. _`South==0.7.5`: http://pypi.python.org/pypi/South

`django-registration==0.8.0`_
==============================

Normally `django-social-auth`_ is my go-to tool for registration, but in this case I need simple username/password registration. This is a very solid tool, but you do have to make your own templates or find someone's fork that has a copy of templates that match.

.. _`django-social-auth`: http://pypi.python.org/pypi/django-social-auth

.. _`django-registration==0.8.0`: http://pypi.python.org/pypi/django-registration

`django-floppyforms==0.4.7`_
==============================

An excellent tool for making your forms HTML5-ish out of the box. 

.. _`django-floppyforms==0.4.7`: http://pypi.python.org/pypi/django-floppyforms

`django-crispy-forms==1.1.3`_
=============================

The child of my own django-uni-forms, this will let me render forms super fast, and do layout customizations if I need them.

.. _`django-crispy-forms==1.1.3`: http://pypi.python.org/pypi/django-crispy-forms

`django-heroku-postgresify==0.2`_
==================================

This tool makes getting the PostGreSQL settings out of Heroku trivial.

.. _`django-heroku-postgresify==0.2`: http://pypi.python.org/pypi/django-heroku-postgresify

`django-heroku-memcacheify==0.1`_
==================================

This tool makes getting the memcache settings for Heroku trivial.

.. _`django-heroku-memcacheify==0.1`: http://pypi.python.org/pypi/django-heroku-memcacheify


`gunicorn==0.14.2`_
====================

All the cool kids who play in devops swear by Gunicorn. I use it because Heroku seems to recommend it for Django deployments.

.. _`gunicorn==0.14.2`: http://pypi.python.org/pypi/gunicorn

----

Installing the above packages
=============================

Never copy/paste these libraries directly into your projects. If you do that, you'll end up hating yourself later as your local instances become unmaintained forks of the real project. Also, unless you are really careful in your copy/pasting, you'll be in violation of various open source licenses. Odds are the FOSS police aren't going to find you, but I can assure you that when you bring in one of the authors of these packages to help you fix a problem he/she is going to be mighty annoyed at the lack of attribution.

Do it the right way: do proper Python dependency management.

Create a ``requirements.txt`` file and install them as proper dependencies. The file should contain the following text::

    Django==1.4
    South==0.7.5   
    django-crispy-forms==1.1.3
    django-debug-toolbar==0.9.4
    django-extensions==0.8
    django-floppyforms==0.4.7
    django-registration==0.8.0
    django-heroku-memcacheify==0.1
    django-heroku-postgresify==0.2
    django-registration==0.8.0    
    gunicorn==0.14.2
    psycopg2==2.4.5

Once you have that, you install them thus in your virtualenv_::

    pip install -r requirements.txt

Now that I have all this, it's time to code!

.. _virtualenv: http://pypi.python.org/pypi/virtualenv

----

.. image:: http://farm5.staticflickr.com/4027/4358842735_38991c0944.jpg
   :name: Blizzard of 2010
   :align: center
   :target: http://www.flickr.com/photos/pydanny/4358842735/
