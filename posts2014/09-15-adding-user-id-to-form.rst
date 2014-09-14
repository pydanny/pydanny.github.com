=======================================
Adding extra attributes to Django forms
=======================================

:date: 2014-09-15 10:30
:tags: python, django, howto, class-based-views, forms
:category: django
:slug: adding-extra-attributes-to-forms
:status: draft

Sometimes in the ``clean()``, ``clean_FOO`` or ``save()`` methods of a Django form, you need to have additional attributes available. A sample case for this is having ``user_id`` available. This is a simple example of how to do it in Class-Based Views.

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

This **should** work with `django-vanilla-views`_.

As always, `http://ccbv.co.uk`_ is a great resource for deliving into Django forms.

.. _`django-vanilla-views`: http://django-vanilla-views.org
.. _`http://ccbv.co.uk`: http://ccbv.co.uk