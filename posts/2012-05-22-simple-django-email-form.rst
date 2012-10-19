====================================
Simple Django email form using CBV
====================================

:date: 2012-05-22 09:30
:tags: python, django, howto, django-CBVs
:category: django

Here's a simple ``FormView`` Class Based Views for Django_. Here is a sample of how to do one as a simple email form. There is no CAPTCHA in this example, that's the topic of a future blog post.

.. _Django: http://djangoproject.com

This version requires the following packages ``pip`` installed into your ``virtualenv``. 

* ``django-crispy-forms`` so we can do Python driven layouts.
* ``django-floppyforms`` so we get HTML5 elements for free.

They also need to be added to your list of INSTALLED_APPS:

.. code-block:: python

    INSTALLED_APPS += (
        'crispy_forms',
        'floppyforms',        
    )

In myapp.forms.py:

.. code-block:: python

    from crispy_forms.helper import FormHelper
    from crispy_forms.layout import Submit
    import floppyforms as forms

    class ContactForm(forms.Form):

        name = forms.CharField(required=True)
        email = forms.EmailField(required=True)
        subject = forms.CharField(required=True)
        message = forms.CharField(widget=forms.Textarea)

        def __init__(self, *args, **kwargs):
            self.helper = FormHelper()
            self.helper.add_input(Submit('submit', 'Submit'))
            super(ContactForm, self).__init__(*args, **kwargs)

In myapp.views.py:

.. code-block:: python

    from django.conf import settings
    from django.core.mail import send_mail
    from django.views.generic import FormView

    from myapp.forms import ContactForm

    class ContactFormView(FormView):

        form_class = ContactForm
        template_name = "myapp/email_form.html"
        success_url = '/email-sent/'

        def form_valid(self, form):
            message = "{name} / {email} said: ".format(
                name=form.cleaned_data.get('name'), 
                email=form.cleaned_data.get('email'))
            message += "\n\n{0}".format(form.cleaned_data.get('message'))
            send_mail(
                subject=form.cleaned_data.get('subject').strip(),
                message=message,
                from_email='contact-form@myapp.com',
                recipient_list=[settings.LIST_OF_EMAIL_RECIPIENTS],
            )
            return super(ContactFormView, self).form_valid(form)
            
In templates/myapp/email_form.html:

.. code-block:: html

    {% extends 'base.html' %}
    {% load crispy_forms_tags %}

    {% block title %}Send an email{% endblock %}

    {% block content %}
        <div class="row">
            <div class="span6">
                <h1>Send an email</h1>
                {% crispy form form.helper %}
            </div>
        </div>
    {% endblock %}

    {% block extrajs %}
    <script src="{{ STATIC_URL }}js/jquery-1.7.1.min.js"></script>
    <script type="text/javascript">
    $(function() {
        $('#id_name').focus()
    });
    </script>
    {% endblock %}

Tomorrow's blog post
====================

In tomorrow's post I'll show how to add CAPTCHA into your project to help reduce spam messages.

Want to learn more?
===================

If you live in the Los Angeles area and want to learn more about Django, everything from the basics to setting up a Content Management System or E-Commerce system, check out our Django (and Python_) training at `Cartwheel Academy`_.

.. _Python: http://python.org
.. _`Cartwheel Academy`: https://academy.cartwheelweb.com