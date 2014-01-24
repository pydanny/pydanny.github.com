=========================================================
awesome-slugify: Human-readable URL slugs from any string
=========================================================

:date: 2014-01-21 12:00
:tags: python, django, unicode, i18n, ppoftw
:category: python
:slug: awesome-slugify-human-readable-url-slugs-from-any-string

*note: The introduction mentions Django and Plone. However, this is not an article about Django or Plone.*

Introduction
=============

Years ago, when I was working with Plone_ at NASA_, one thing I dreaded was when content editors would copy-and-paste from Microsoft Word into the title bar. All kinds of funny characters would appear in the title bar and URL. I would have to go into the database (ZODB) and fix things. Things didn't get better until `Reed O'Brien`_ turned on a title validator (probably in ``Plone.i18n``).

.. _`Reed O'Brien`: https://github.com/reedobrien
.. _Plone: http://plone.org
.. _NASA: http://nasa.gov

When we started using Django_, one thing that made it nice was the presence of it's `slugify()`_ function and template filter. Inspired by the newspaper industry, this function it easier on both content editors and software engineers. In any case, using ``slugify()`` we completed a number of projects, with `NASA Science`_ being the only public one I worked on.

.. _Django: https://www.djangoproject.com
.. _`slugify()`: https://docs.djangoproject.com/en/dev/ref/utils/#module-django.utils.text
.. _`NASA Science`: http://science.nasa.gov/

As much as the ``slugify()`` function was useful, there were problems. As I discovered time and time again over the years, it didn't handle unicode_. Or rather, it handled them by simply vanishing non-ASCII unicode characters. For example:

.. _unicode: https://en.wikipedia.org/wiki/Unicode

.. code-block:: python

    >>> from django.utils.text import slugify
    >>> slugify(u"straße") # German for road
    u"strae"

If you read German, you'll know that the default Django ``slugify()`` function is converting the word 'road' to nonsense. For sites dealing with internationalization, this won't do. So over three years ago while at Mozilla_, Pinterest_ engineer `Dave Dash`_ created `unicode-slugify`_. From then on we could do this:

.. _`Dave Dash`: https://twitter.com/davedash
.. _Pinterest: http://pinterest.com

.. _Mozilla: http://www.mozilla.org/
.. _`unicode-slugify`: https://pypi.python.org/pypi/unicode-slugify

.. code-block:: python

    >>> from slugify import slugify
    >>> slugify(u"straße") # Again with the German word for road
    u"straße"
    
What If I'm Not Using Django?
------------------------------

While a very nice tool, this package is dependent on Django's internal machinery to operate, which is a problem for non-Django users. While we could use Python's `unicodedata library to resolve unicode to slugs`_, wouldn't it be nice if there was a nicely packaged/tested solution?

.. _`unicodedata library to resolve unicode to slugs`: http://flask.pocoo.org/snippets/5/

Fortunately, such a nicely packaged/tested solution exists, and it's awesome!

.. image:: https://s3.amazonaws.com/pydanny/awesome_slugify_django.jpg
   :name: Django Slug
   :align: center
   :alt: An Awesome Django slug


Introducing awesome-slugify
===========================

Created and maintained by `Dmitry Voronin`_, `awesome-slugify`_ is easy to use and **100% independent from Django**. You call it thus:

.. _`Dmitry Voronin`: https://github.com/dimka665
.. _`awesome-slugify`: https://pypi.python.org/pypi/awesome-slugify

.. code-block:: python

    >>> import slugify
    >>> slugify.slugify(u"straße") # Yet again the German for road
    u'strasse'
    
Works! Hooray! 

However, please note that unlike the Django-only **unicode-slugify** package which preserves the non-ASCII characters, **awesome-slugify** transformed the German 'ß' into an ASCII substitution of 'ss'. This is similar to how the popular `python-slugify`_ package works. While this behavior of translating unicode to ASCII might work for English-only sites, it's not so useful for the rest of the world. Fortunately, **awesome-slugify** also provides the incredibly useful ``slugify_unicode()`` function:

.. _`python-slugify`: https://pypi.python.org/pypi/python-slugify

.. code-block:: python

    >>> import slugify
    >>> slugify.slugify_unicode(u"straße") # What is it with German Roads?
    u'stra\xdfe'
    >>> slugify.slugify_unicode(u"straße") == u"straße"
    True

Using awesome-slugify
---------------------

Rather than describe **awesome-slugify** in paragraph format, here is working test code (`using pytest which I described before`_) that explains what we can do:

.. _`using pytest which I described before`: http://pydanny.com/pytest-no-boilerplate-testing.html

.. code-block:: python
    
    # -*- coding: utf-8 -*-
    # test_awesome_slugify.py
    from __future__ import unicode_literals
    import pytest
    from slugify import slugify, slugify_unicode

    def test_simple():
        txt = "This is basic functionality!!!    "
        assert slugify(txt) == "This-is-basic-functionality"
    
    def test_remove_special_characters():
        txt = "special characters (#?@$%^&*) are also ASCII"
        assert slugify(txt) == "special-characters-are-also-ASCII"
    
    def test_basic_accents_and_backslash_escapes():
        txt = 'Where I\'ve gone before'
        assert slugify(txt) == "Where-Ive-gone-before"
    
    @pytest.fixture
    def accents():
        return u'Àddîñg áçćèńtš tô Éñgłïśh íš śīłłÿ!'
    
    def test_accents(accents):
        assert slugify(accents) == "Adding-accents-to-English-is-silly"
    
    def test_keep_accents(accents):
        assert slugify_unicode(accents) == \
                            'Àddîñg-áçćèńtš-tô-Éñgłïśh-íš-śīłłÿ'

    def test_keep_accents_lower(accents):
        # Because awesome-slugify doesn't lower() while slugify, we
        #   have to do it ourselves. I'm torn if I like this or hate it
        assert slugify_unicode(accents).lower() == \
                            'àddîñg-áçćèńtš-tô-éñgłïśh-íš-śīłłÿ'
                            
    def test_musical_notes():
        txt = "Is ♬ ♫ ♪ ♩ a melody or just noise?"
        assert slugify(txt) == "Is-a-melody-or-just-noise"
        assert slugify_unicode(txt) == "Is-a-melody-or-just-noise"
        
    def test_chinese():
        txt = "美国" # Chinese for 'America'
        assert slugify(txt) == "Mei-Guo"
        assert slugify_unicode(txt) ==  "美国" 

    def test_separator():
        txt = "Separator is a word I frequently mispell."
        result = slugify(txt, separator="_", capitalize=False)
        assert result == "Separator_is_a_word_I_frequently_mispell"
        
    if __name__ == "__main__":
        pytest.main()
        
Easy to use as any good ``slugify()`` function! 

Restricting the length of a returned slug
------------------------------------------

When using **awesome-slugify**'s ``slugify()`` and ``slugify_unicode()`` functions, the ``max_length`` argument acts in an interesting fashion. On very short strings it removes longer words to make things fit. As the author of **awesome-slugify** is Russian, and the Russian language, as far as I know, doesn't have prepositions (words like 'the' and 'a') this makes sense.

Let's take a look, shall we?

.. code-block:: python

    # -*- coding: utf-8 -*-
    # test_awesome_slugify_max_length.py
    import pytest
    from slugify import slugify, slugify_unicode
        
    def test_max_length_tiny():
        # Removes the longer words to fit smaller words in.
        txt = "$ is a special character, as is #."
        assert slugify(txt, max_length=10) == "is-a-as-is"

    def test_max_length_medium():
        # Keeps in prepositions, but removes meaningful words.
        txt = "$ is a special character, as is #."
        assert slugify(txt, max_length=15) == "is-a-special-as"

    def test_max_length_realistic():
        # Long enough that long words are not removed from the string in favor 
        #   of shorter words.
        txt = """This sentence illuminates the method that this package
                    handles truncation of longer strings.
        """
        assert slugify(txt, max_length=50) == \
            "This-sentence-illuminates-the-method-that-this-of"
            
    # The next few tests cover how the max_length argument handles truncation
    #   inside of a word. When working with longer word languages, like German,
    #   understanding how your chosen slugify() function works is important.
            
    def test_truncating_word():
        # This demonstrates taking a long German word and truncating it.
        txt = u"Rindfleischetikettierungsüberwachungsaufgabenübertragungsgesetz"
        assert slugify(txt, max_length=40) == \
                    "Rindfleischetikettierungsuberwachungsauf"
        assert slugify_unicode(txt, max_length=40) == \
                    u"Rindfleischetikettierungsüberwachungsauf"
                    
    def test_truncating_varying_letter_size():
        # Truncating unicode slugs is challenging. For example, the German 
        #   letter 'ß' is 'ss' in English. Should a slugify's max_length
        #   argument use the German or the English length? In the case of 
        #   awesome-slugify, it uses the length of English letter for both the 
        #   slugify() and slugify_unicode() functions.
        txt = u"straße" # I really can't stop using German roads.
        assert slugify(txt, max_length=5) == "stras"
        assert slugify_unicode(txt, max_length=5) == u"straß"
            
    if __name__ == "__main__":
        pytest.main()
        
What's Next?
==============

As demonstrated, **awesome-slugify** covers many common use cases. Nevertheless, in `my next blog post`_ I cover how to write custom language ``slugify()`` translation functions using **awesome-slugify**.

**Update 2013/01/23** Thanks to `flying-sheep`_, I Changed 'equivalent' to 'substitution' in describing the unicode-to-ASCII translation. This is because 'ss' is not a precise translation of 'ß'.

.. _`flying-sheep`: http://www.reddit.com/user/flying-sheep

.. _`my next blog post`: http://pydanny.com/awesome-slugify-human-readable-url-slugs-from-any-string-2.html


.. _pip: http://www.pip-installer.org/