===========================================
CSS Hacking to make my code samples legible
===========================================

:date: 2012-05-11 08:30
:tags: python, django, css, usability
:category: python

I've been very happy with Pelican_ as a blog engine so far, and haven't even moved off the sample theme. There's just been one problem: Myself and others have had a lot of trouble reading the code snippets.

.. _Pelican: http://pelican.readthedocs.org/

I didn't have time to cook up a full Pelican theme, so instead I just hacked the local CSS files. What I did was a hack, and next week when I have time I'll do a proper Pelican theme.

In the meantime, enjoy!

.. code-block:: python

    from random import shuffle

    class Meal(object):
        def __init__(self):
            self.food_type = ['Beef', 'Fish', 'Vegetarian', 'Chicken']
            shuffle(self.food_type)

