=====================================
Markup Language Faceoff: Lists
=====================================

:date: 2015-05-14 10:00
:tags: python, LaTeX, RestructuredText, markdown, faceoff, django
:category: python
:slug: markup-language-faceoff-lists

Today I want to talk about lists. Not for shopping, not the programming data type, but the display of items in both unordered and ordered fashion. Specifically this:

* Item A

* Item B

  #. First Numbered Inner Item

  #. Second Numbered Inner Item

* Item C

In other words, lists of bullets and numbers. This article explores some of the different tools used by the programming world to render display lists, specifically **HTML**, **reStructuredText**, **Markdown**, and **LaTeX**.

HTML
====

If you view the HTML_ source of this web page, you'll find this:

.. _HTML: http://en.wikipedia.org/wiki/HTML

.. code-block:: html

    <ul class="simple">
    <li>Item A</li>
    <li>Item B<ol class="arabic">
    <li>First Numbered Inner Item</li>
    <li>Second Numbered Inner Item</li>
    </ol>
    </li>
    <li>Item C</li>
    </ul>

Or more clearly:

.. code-block:: html

    <ul class="simple">
        <li>Item A</li>
        <li>Item B
            <ol class="arabic">
                <li>First Numbered Inner Item</li>
                <li>Second Numbered Inner Item</li>
            </ol>
        </li>
        <li>Item C</li>
    </ul>

This works, but is incredibly verbose. **HTML** requires closing tags on every element. Working with lists in HTML becomes tedious quickly. Which is why so many people use WYSIWYG_ tools or mark up languages like **reStructuredText** and **Markdown**, as it expedites creation of lists (and many other things).

.. _WYSIWYG: http://en.wikipedia.org/wiki/WYSIWYG

reStructuredText
==================

This blog is written in reStructuredText_ and transformed into **HTML**. Let's see the markup for this blog post:

.. _reStructuredText: http://en.wikipedia.org/wiki/ReStructuredText

.. code-block:: rst

    * Item A

    * Item B

      #. First Numbered Inner Item

      #. Second Numbered Inner Item

    * Item C

Notice the extra lines between bullets and numbers? A quirk of **reStructuredText** is that you have to put those in nested lists in order to make things display correctly. Also, 2 spaces indentation generates a different result than 4 spaces. I have no idea why this behavior exists, but I admit to finding both quirks annoying.

One thing to note about **reStructuredText** is that it's pretty much Python only. Outside the Python world if you are writing plaintext markup then odds are you are using **Markdown**.

Markdown
==================

Markdown_ does lists really well. Terse and no weird quirks:

.. code-block:: rst

    * Item A
    * Item B
      1. First Numbered Inner Item
      1. Second Numbered Inner Item
    * Item C

Another nice feature about **Markdown** is that it's in use everywhere. GitHub, Stack Overflow, my favorite tablet writing app, and a lot more.

.. _Markdown: http://en.wikipedia.org/wiki/Markdown

Markdown vs. reStructuredText
==============================

Why don't I switch from **reStructuredText** to **Markdown**? Here are my reasons against switching:

#. Force of habit.
#. PyPI_ requires it to display package long descriptions nicely on Package pages.
#. Sphinx_ is based on it.
#. **reStructuredText** has one concrete standard, with extensions that people add. Markdown has many standards, which may or may not have shared features.
#. I can use Pandoc_ to help transform **reStructuredText** to **Markdown**.

.. _Sphinx: http://en.wikipedia.org/wiki/Sphinx_(documentation_generator)
.. _PyPI: http://pypi.python.org/pypi
.. _Pandoc: http://pandoc.org


LaTeX
=====

Finally, let's discuss LaTeX_. While not a markup language it bears mentioning, and I'll explain why later in this section.

Up to about 8-10 years ago **LaTeX** was used in a lot of technical writing, including the Python core documentation. That ended with the rise of mark up languages, relegating **LaTeX** to the world of academics, mathematicians and computer scientists - anywhere complex equations need to be specified.

LaTeX belongs in this article because it is so commonly used with markup. In fact, as far as I can tell, in order to render **reStructuredText** and **Markdown** content into the PDF format, the most common approach is:

#. Use a script to transform the markup into **LaTeX**.
#. Use a tool like XeTeX_ to render the **LaTeX** into PDF.

Why the extra step? Why not just go directly from markup to PDF? Well, the content in **reStructuredText** and **Markdown** have to be formatted in order for them to be displayed, or they will just look like plaintext markup. When they are converted to **HTML**, the browser does the formatting for us. When they are translated to PDF, LaTeX is a very common choice. That is because **LaTeX** isn't a markup language, but a typesetting tool. Unlike **reStructuredText** and **Markdown** which are designed for ease of use, **LaTeX** is designed to make documents look good.

Here is how I define my sample list in **LaTeX**

.. _LaTeX: http://en.wikipedia.org/wiki/LaTeX
.. _XeTeX: http://en.wikipedia.org/wiki/XeTeX

.. code-block:: latex

    \begin{itemize}
        \item Item A
        \item Item A
            \begin{itemize}
                \item First Numbered Inner Item
                \item Second Numbered Inner Item
            \end{itemize}
        \item Item C
    \end{itemize}

Halfway between the markup languages and HTML in verbosity, **LaTeX** lists are of medium difficulty to write. If this example makes **LaTeX** look easy, please realize that while lists are easy to understand, other structures like **LaTeX** tables_ can quickly get out of hand. **LaTeX**'s reputation for being an arcane tool is a well deserved one.

.. _tables: http://en.wikibooks.org/wiki/LaTeX/Tables

Modifying Generated LaTeX
====================================

Several book authors, including ourselves, have written books using **reStructuredText** or **Markdown**, generated the **LaTeX**, then modified the **LaTeX** before rendering the PDF. The approach is seductive: You get the ease of a markup language combined with the formatting precision of **LaTeX**.

Or do you?

The problem my wife and I have faced is that the combination of **LaTeX** packages and tools we've assembled for ourselves to write books like `Two Scoops of Django`_ is very, very different than what is rendered via docutils_' ``rst2latex`` or Sphinx ``make latex``. We've tried to write migration scripts, but have found that we end up spending too much of our time on formatting. That's why we have stuck with hand-crafted artisan **LaTeX**.

.. _docutils: https://pypi.python.org/pypi/docutils
.. _`Two Scoops of Django`: twoscoopspress.com/products/two-scoops-of-django-1-8

That isn't to say it isn't possible. In fact, Matt Harrison has released_ a number handsome_ Python_ books_ following this path (**reStructuredText** to **LaTeX**). I'm certain there are **Markdown** books that follow this path too.

.. _released: http://www.amazon.com/Brief-Introduction-Python-Testing-Harrison-ebook/dp/B00AY4VE8E/?tag=mlinar-20
.. _handsome: http://www.amazon.com/Guide-Learning-Iteration-Generators-Python/dp/1492333514/ref=sr_1_7?tag=mlinar-20
.. _Python: http://www.amazon.com/Treading-Python-1-Foundations/dp/1475266413/ref=sr_1_2?tag=mlinar-20
.. _books: http://www.amazon.com/Treading-Python-2-Intermediate/dp/149055095X/ref=sr_1_1?tag=mlinar-20

Closing Thoughts
================

For better or for worse, lists of bullets and numbers are a foundation of how we communicate via the written medium. They allow for terse communication of ideas and thought, but that same terseness can mean we skip over details. Interestingly enough, the very tools that we use to create lists can color our ability and desire to use them.

.. image:: http://pydanny.com/static/320px-Naseby_musket_balls.jpg
   :name: Naseby musket balls
   :align: center
   :alt: Naseby musket balls
   :target: https://www.flickr.com/photos/26724339@N00/3025221901/

Old-fashioned bullets, specifically matchlock musket balls, alleged to have been found at the site of the Battle of Naseby.

From the collection of Northampton Museum and Art Gallery.
