=======================================
The Easy Form Views Pattern Controversy
=======================================

:date: 2013-05-10 12:00:00
:tags: python, django, howto
:category: django

This isn't a controversy 'per se', except perhaps in the feverish depths of my brain.

In the summer of 2010 `Frank Wiles`_ of Revsys_ exposed me to what I later called the "**Easy Form Views**" pattern when creating Django form function views. I used this technique in a variety of places, including `Django Packages`_ and the documentation for django-uni-form (which is rebooted as `django-crispy-forms`_). At DjangoCon 2011 `Miguel Araujo`_ and I opened our `Advanced Django Forms Usage`_ talk at DjangoCon 2011 with this technique. It’s a pattern that reduces the complexity of using forms in Django function-based views by flattening the form handling code. 

.. _`Django Packages`: https://www.djangopackages.com
.. _`django-crispy-forms`: https://github.com/maraujop/django-crispy-forms

How the Easy Form Views pattern works
======================================

Normally, function-based views in Django that handle form processing look something like this:

.. code-block:: python

    def my_view(request, template_name="my_app/my_form.html"):

        if request.method == 'POST':
            form = MyForm(request.POST)
            if form.is_valid():
                do_x() # custom logic here
                return redirect('home')
        else:
            form = MyForm()
        return render(request, template_name, {'form': form})

In contrast, the Easy Form Views pattern works like this:

.. code-block:: python

    def my_view(request, template_name="my_app/my_form.html"):

        form = MyForm(request.POST or None)
        if form.is_valid():
            do_x() # custom logic here
            return redirect('home')
        return render(request, template_name, {'form': form})

The way this works is that the ``django.http.HttpRequest`` object has a POST attribute that defaults to an empty dictionary-like object, even if the request’s method is equal to "GET". Since we know that `request.POST` exists in every Django view, and os at least as an empty dictionary-like object, we can skip the ``request.method == 'POST'`` by doing a simple boolean check on the ``request.POST`` dictionary.

In other words:

* If ``request.POST`` dictionary evaluates as ``True``, then instantiate the form bound with ``request.POST``.
* If ``the request.POST`` dictionary evaluates as ``False``, then instantiate an unbound form.

Great! Faster to write and shallower code! What could possibly be wrong with that?

The Controversy
===============

Before you jump to convert all your function based forms to this pattern, consider the following argument raised against it by a good friend:

.. epigraph::

    This one of those things where "empty dictionary and null both evaluate as false" can bite you.

    There's a difference between "There is no POST data", and "This wasn't a POST".

    -- by `Russell Keith-Magee`_ (paraphrased)

The problem he is talking about is data besides ``multipart/form-data`` or ``application/x-www-form-urlencoded`` would still end up in the ``request.POST`` dictionary-like attribute.

Getting bit by the Easy Form Views method
====================================================

Here's how it happens:

**Before Django 1.5** HTTP methods such as DELETE or PUT would see their data placed into Django's ``request.POST`` attribute. The form would fail, but it might not be clear to the developer or user why. HTTP GET and POST methods work as expected.

**For Django 1.5 (and later)** if a non-POST comes in then the form fails because request.POST is empty. HTTP GET and POST methods also work as expected.

Conclusion
==========

Going forward, I prefer to use Django's class-based views or `Django Rest Framework`_ which make the issue of this pattern moot. When I do dip into function-based views handling classic HTML forms, I'm leery of using this pattern anymore. Yes, it is an edge case, but to inaccurately paraphrase Russell, "edge cases are where you get bit".

What I'm not going to do is rush to change existing views on existing projects.  That's because personally I've yet to run into an actual problem with using this pattern. As they say, "*If it ain't broke, don't fix it.*" While I'm not saying my code isn't broken, I'm also aware that 'fixing' things that aren't reporting errors is a dangerous path to tread.

.. _gists: https://gist.github.com
.. _`Django Rest Framework`: http://djangorestframework.com
.. _`Frank Wiles`: http://twitter.com/fwiles
.. _Revsys: http://revsys.com
.. _`Miguel Araujo`: http://tothinkornottothink.com/
.. _`Advanced Django Forms Usage`: http://lanyrd.com/2011/djangocon-us/shbrd/
.. _`Russell Keith-Magee`: http://cecinestpasun.com/