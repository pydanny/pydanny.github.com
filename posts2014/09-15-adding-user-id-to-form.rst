=========================================
Adding Django form instance attributes
=========================================

:date: 2014-09-15 10:30
:tags: python, django, howto, class-based-views, forms
:category: django
:slug: adding-django-form-instance-attributes

Sometimes in the ``clean()``, ``clean_FOO`` or ``save()`` methods of a Django form, you need to have additional form instance attributes available. A sample case for this is having ``user_id`` available. This is a simple example of how to do it in Class-Based Views.

Assuming this form:

.. code-block:: python

    from django import forms

    from .models import MyModel


    class MyForm(forms.ModelForm):

        class Meta:
            model = MyModel

        def __init__(self, user_id, *args, **kwargs):
            super(MyForm, self).__init__(*args, **kwargs)

            # set the user_id as an attribute of the form
            self.user_id = user_id

Now that the form is defined, the view needs to inject the form with the user id:

.. code-block:: python

    from django.views.generic import UpdateView

    # this assumes that django-braces is installed
    from braces.views import LoginRequiredMixin

    from .forms import MyForm
    from .models import MyModel


    class MyUpdateView(LoginRequiredMixin, UpdateView):
        model = MyModel
        form_class = MyForm
        success_url = "/someplace/"

        def get_form_kwargs(self):
            """This method is what injects forms with their keyword
                arguments."""
            # grab the current set of form #kwargs
            kwargs = super(MyUpdateView, self).get_form_kwargs()
            # Update the kwargs with the user_id
            kwargs['user_id'] = self.request.user.pk
            return kwargs

Additional Notes
=================

You can use this technique with:

* ``forms.Form``
* ``forms.ModelForm``
* ``CreateView``
* ``FormView``
* ``UpdateView``

As always, `http://ccbv.co.uk`_ is a great resource for deliving into Django forms.

While this technique is used by ``django-braces`` through the ``UserFormKwargsMixin`` and ``UserKwargModelFormMixin`` mixins, it's useful to know how to do it outside that very useful tool. The reason being that attaching the ``user`` object or ``user_id`` is just one option out of many.

django-vanilla-views
====================

This should also work with `django-vanilla-views`_, but I haven't tested it yet.

.. image:: http://pydanny.com/static/form-attributes.png
   :name: Vanilla and Strawberry forms
   :align: center
   :target: https://twitter.com/audreyr


See you at BarCamp Django SF!
=============================

On October 4th and 5th I'll be at `BarCamp Django SF`_ if you want to talk about Django, Python, or have me teach you how to do cartwheels.







.. _`BarCamp Django SF`: http://pydanny.com/barcamp-django-sf.html

.. _`django-vanilla-views`: http://django-vanilla-views.org
.. _`http://ccbv.co.uk`: http://ccbv.co.uk