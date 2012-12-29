===========================
New Year's Python Meme 2012
===========================

:date: 2012-12-28 18:00
:tags: meme, python, django, holidays
:category: python

Tarek Ziade has a habit of ending the year with a Python-themed meme. I've matched his meme the times he previousstarted it, and as you can tell from the title of this blog post I'm matching him yet again.

1. What’s the coolest Python application, framework or library you have discovered in 2012?
===================================================================================================

This question took some thought. It was a toss-up between these three choices:

* Django Class Based Views (CBVs) allow developers do amazing things with Django, but needed some polish (`improved documentation`_, `missing functionality`_) to be able to shine.
* ReportLab_ for generating PDF allowed me to create some `impressive results`_, but the API needed updating. The other Python PDF libraries might be better, but getting images to work trivially in them 
* If I didn't completely agree with `Armin Ronacher on the subject`_, I might have gone with a combination of PyMongo_, MongoEngine_, and MongoKit_. Just like Armin, I've learned through working with schemaless databases to know that schemas are awesome.

The winner?

    **Django Class Based Views**

In 2012 what I managed to accomplish with Django CBVs was incredible. From early self-instructional work I did for `django-mongonaut`_, to client efforts and personal projects where I honed my craft, plus examples `I blogged about`_ or helped get into Django core, it made for a great year. Also I wasn't just productive personally, I helped increased the productivity of others around the world.

And you ain't seen nothing yet!

2. What new programming technique did you learn in 2012?
========================================================

I thought I understood multiple inheritance.

I really did.

However, since the start of this year I've delved really deep into it, only to discover just how much I didn't know. While that didn't do my ego any favors, it was a nice refreshing reminder not to get arrogant about one's skills.



3. Which open source project did you contribute to the most in 2012? What did you do?
=======================================================================================

The answer to this is **Django**.

After using Django professionally for 2.5 years, I finally began contributing to the core framework at the DjangoCon Eu 2012 sprints. I joined a group of other dedicated people who decided to improve the `Django CBV documentation`_, our goal being setting a new standard for documentation. I'm not sure if we set a new bar in documentation, but we did improve on the existing material.

I branched out into some other areas of core Django development with mixed results, which played out that way because I just didn't have the time to do more.


4. Which Python blog or website did you read the most in 2012?
==============================================================

As always, http://planet.python.org.

5. What are the three top things you want to learn in 2013?
===========================================================

1. Really advanced Python as taught by Raymond Hettiger or David Beazley.
2. I really want to learn Twisted_.
3. How to do an `Aú sem Mão`_.

.. _NumPy: http://www.numpy.org/
.. _SciPy: http://www.scipy.org/
.. _Twisted: http://twistedmatrix.com/
.. _`Aú sem Mão`: http://en.wikipedia.org/wiki/A%C3%BA#A.C3.BA

6. What is the top software, application or library you wish someone would write in 2013?
=========================================================================================

I've got a couple:

* A Python SDK that produces results that work perfectly for both modern iOS and Android. Think Corona SDK but with Python.
* A modern PyGame release that installs trivially on Mac OS X.


Want to do your own list? here's how:
=====================================

* copy-paste the questions and answer to them in your blog
* tweet it with the `#2012pythonmeme`_ hashtag

.. _ReportLab: http://reportlab.org
.. _MongoKit: http://namlook.github.com/mongokit/
.. _PyMongo: http://api.mongodb.org/python/
.. _MongoEngine: http://mongoengine.org/
.. _`missing functionality`: http://django-braces.readthedocs.org/
.. _`improved documentation`: https://docs.djangoproject.com/en/1.5/topics/class-based-views/
.. _`impressive results`: http://www.petcheatsheets.com/
.. _`Armin Ronacher on the subject`: http://lucumr.pocoo.org/2012/12/29/sql-is-agile/
.. _`django-mongonaut`: https://github.com/pydanny/django-mongonaut/blob/master/mongonaut/views.py
.. _`I blogged about`: http://pydanny.com/tag/django-CBVs.html
.. _`Django CBV documentation`: https://docs.djangoproject.com/en/1.5/topics/class-based-views/
.. _`#2012pythonmeme`: https://twitter.com/search/realtime?q=%232012pythonmeme&src=typd