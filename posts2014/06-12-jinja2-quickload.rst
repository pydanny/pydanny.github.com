===========================
Jinja2 Quick Load Function
===========================

:date: 2014-06-12 09:00
:tags: python, jinja2
:category: python
:slug: jinja2-quick-load-function

It seems like that for every few weeks I find myself needing to generate something out of a template while working outside a framework. For this task, my preferred solution is Jinja2_. I've used Jinja2 to generate HTML, code, and text. If I were brave enough I would even say I've used it to generate XML (*While my preferred xml tool is great for parsing, even lxml is not so much fun for XML generation*).

I frequently use this snippet of code to render templates. Since I'm tired of digging through my code to find it, I'm placing it here for personal reference.

.. code-block:: python

    from jinja2 import FileSystemLoader, Environment

    def render_from_template(directory, template_name, **kwargs):
        loader = FileSystemLoader(directory)
        env = Environment(loader=loader)
        template = env.get_template(template_name)
        return template.render(**kwargs)

Sample usage:

.. code-block:: python

    >>> from simple_script import render_from_template
    >>> data = {
    ...     "date": "June 12, 2014",
    ...     "items": ["oranges", "bananas", "steak", "milk"]
    ... }
    >>> render_from_template(".", "shopping_list.html", **data)

I've thought about packaging this up with `cookiecutter-pypackage`_ and placing it on PyPI_, but I think it might be overkill.

**Update 2014/06/12:** Fixed cookiecutter link thanks to https://github.com/dirn

.. _Jinja2: http://jinja.pocoo.org/
.. _`cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
.. _PyPI: https://pypi.python.org/pypi