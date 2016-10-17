========================================================
Pretty Formatting JSON in the Django Admin
========================================================

:date: 2016-05-26 17:00
:tags: python, django, cheatsheet, ppoftw, postgresql
:category: Django
:slug: pretty-formatting-json-django-admin

Recently I was writing code to interact with a third-party API. The API changes frequently, especially the data contained in responses. However, that data has to be saved and periodically needs to be audited. I wanted a data model flexible enough to handle these periodic changes without a lot of anguish, yet queryable. Since the API serves out queryable JSON, this made it a no-brainer for using  ``django.contrib.postgres``'s JSONField.

After a little bit of work, I had data samples to play with. Quickly my admin filled with chunks of JSON that looked something like this:

.. code-block:: bash

    {"field_12": 8, "field_16": 4, "field_6": 14, "field_7": 13, "field_18": 2, "field_2": 18, "field_4": 16, "field_15": 5, "field_9": 11, "field_3": 17, "field_8": 12, "field_11": 9, "field_17": 3, "field_10": 10, "field_0": 20, "field_1": 19, "field_13": 7, "field_5": 15, "field_14": 6}

Kind of illegible, right? And that's a simple, flat example with just 20 keys. Imagine if this were a nested dictionary with 100 or 200 fields. For reference, that's the kind of data that I had that makes this kind of display nigh useless.

So I cooked up this quick fix:

.. code-block:: python

    import json
    from pygments import highlight
    from pygments.lexers import JsonLexer
    from pygments.formatters import HtmlFormatter

    from django.contrib import admin
    from django.utils.safestring import mark_safe

    from .models import APIData


    class APIDataAdmin(admin.ModelAdmin):
        readonly_fields = ('data_prettified',)

        def data_prettified(self, instance):
            """Function to display pretty version of our data"""

            # Convert the data to sorted, indented JSON
            response = json.dumps(instance.data, sort_keys=True, indent=2)

            # Truncate the data. Alter as needed
            response = response[:5000]

            # Get the Pygments formatter
            formatter = HtmlFormatter(style='colorful')

            # Highlight the data
            response = highlight(response, JsonLexer(), formatter)

            # Get the stylesheet
            style = "<style>" + formatter.get_style_defs() + "</style><br>"

            # Safe the output
            return mark_safe(style + response)

        data_prettified.short_description = 'data prettified'

    admin.site.register(APIData, APIDataAdmin)

The field remains the same, but we also get a display of nicely formatted data:

.. raw:: html

    <img alt="Admin Pretty JSON" class="align-center img-responsive" id="admin-pretty-json" src="https://www.pydanny.com/static/admin-pretty-json.png">

Much better!

There may be a package out there that does this already, perhaps even using a JavaScript library like hightlight.js instead of pygments. If not, it shouldn't be hard to create one using `Cookiecutter Django Package`_. Let me know if you package this and I'll add it to this blog post.

----

See you at PyCon!
-----------------

I'll be at PyCon with `Audrey Roy Greenfeld`_. You can easily find us at the Cookiecutter_ booth during the main conference days or at the `Cookiecutter sprint`_. Stop by and say hi!

.. _`Audrey Roy Greenfeld`: https://twitter.com/audreyr
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`Cookiecutter sprint`: https://us.pycon.org/2016/community/sprints/#cookiecutter


.. _`Cookiecutter Django Package`: https://www.pydanny.com/how-to-create-installable-django-packages.html
