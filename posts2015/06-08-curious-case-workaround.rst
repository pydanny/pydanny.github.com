=======================================
Why Doesn't Python Have Switch/Case?
=======================================

:date: 2015-06-09 18:00
:tags: python, django, howto
:category: python
:slug: why-doesnt-python-have-switch-case

.. image:: http://pydanny.com/static/aliens.png
   :name: Aliens
   :align: center
   :alt: Aliens
   :target: http://www.pydanny.com/static/aliens.png

Unlike every other programming language I've used before, Python does not have a switch or case statement. To get around this fact, we use dictionary mapping:

.. code-block:: python

    def numbers_to_strings(argument):
        switcher = {
            0: "zero",
            1: "one",
            2: "two",
        }
        return switcher.get(argument, "nothing")

This code is analogous to:

.. code-block:: javascript

    function(argument){
        switch(argument) {
            case 0:
                return "zero";
            case 1:
                return "one";
            case 2:
                return "two";
            default:
                return "nothing";
        };
    };

While the Python code is often more terse than the standard method of handling cases, I could argue it is more arcane. When I first started Python it felt weird and distracting. Over time it grew on me, the use of a dictionary key being the identifier in a switch becoming more and more habitual.

Dictionary Mapping for Functions
================================

In Python we can also include functions or lambdas in our dictionary mapping:

.. code-block:: python

    def zero():
        return "zero"

    def one():
        return "one"

    def numbers_to_functions_to_strings(argument):
        switcher = {
            0: zero,
            1: one,
            2: lambda: "two",
        }
        # Get the function from switcher dictionary
        func = switcher.get(argument, lambda: "nothing")
        # Execute the function
        return func()

While the code inside ``zero()`` and ``one`` are simple, many Python programs use dictionary mappings like this to dispatch complex procedures.

Dispatch Methods for Classes
============================

If we don't know what method to call on a class, we can use a dispatch method to determine it at runtime.

.. code-block:: python

    class Switcher(object):
        def numbers_to_methods_to_strings(self, argument):
            """Dispatch method"""
            # prefix the method_name with 'number_' because method names
            # cannot begin with an integer.
            method_name = 'number_' + str(argument)
            # Get the method from 'self'. Default to a lambda.
            method = getattr(self, method_name, lambda: "nothing")
            # Call the method as we return it
            return method()

        def number_0(self):
            return "zero"

        def number_1(self):
            return "one"

        def number_2(self):
            return "two"

Pretty nifty, right?


The Official Answer
===================

The `official answer`_ says, "You can do this easily enough with a sequence of ``if... elif... elif... else``". And that you can use dictionary mapping for functions and dispatch methods for classes.

Arguably the official answer doesn't explain anything except for workarounds. In other words, a "non-answer". In my opinion, what the official answer is really trying to say is, "Python doesn't need a case statement."

Really?
=======

Yup. But there's more. I've heard people I respect say that switch/case statements in code can be really hard to debug.

Personally I find that argument breaks down as soon as you run into gigantic nested dictionaries used for mapping of code branches. Think about it, a 100+ element nested dictionary is just as hard to debug as a nested switch and case block with 100+ cases.

Maybe Dictionary Mapping Runs Faster?
=====================================

Moot as Python doesn't have a case statement. Talking about benchmarks from other languages is pointless as what is faster in one language is not always faster in another. Let's move on.

The Significant Advantage of Python's Approach
==============================================

Every once in a while I walk into a scenario where Python's approach just works better than a switch/case statement. This is when at runtime I need to add or remove potential items from the mapping. When this occurs, my years of practice of writing dictionary mappings and dispatch methods pays off. I have insights now that I never had back in the day when I relied on switch/case statements.

Closing Thoughts
=================

To me, that Python forced me to accumalate lots of practical experience with mappings is a blessing in disguise. The constraint of not having switch/case statements allowed me to create approaches and ideas I may not have developed with it.

Intentional or not, Python's lack of switch/case has been a social construct that made me a better coder.

Enough so that I think this accidental social construct is a better answer than the official one of 'Do this instead!'

Or... as Tim Lesher puts it, I'm suffering from Stockholme Syndrome:

.. raw:: html

    <blockquote class="twitter-tweet" lang="en"><p lang="en" dir="ltr"><a href="https://twitter.com/pydanny">@pydanny</a> I think they call that &quot;Stockholm Syndrome&quot;.</p>&mdash; Tim Lesher (@tlesher) <a href="https://twitter.com/tlesher/status/608331276307808256">June 9, 2015</a></blockquote>
    <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

----

The reference book I co-authored with `Audrey Roy Greenfeld`_ on Django best practices, `Two Scoops of Django 1.8`_, is now available in both print paperback and PDF formats.

.. _`Two Scoops of Django 1.8`: http://twoscoopspress.com/products/two-scoops-of-django-1-8


.. _`official answer`: https://docs.python.org/2/faq/design.html#why-isn-t-there-a-switch-or-case-statement-in-python
.. _`Audrey Roy Greenfeld`: http://www.codemakesmehappy.com