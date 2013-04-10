================================================
Annotated History of My Most Used Shell Commands
================================================

:date: 2013-4-10 09:00
:tags: python, twoscoops, book
:category: python
:slug: 20130410-history-of-my-most-used-shell-commands

An oldie, but a goodie. This timeI annotate it with reasons as to why things are used so much. If you blog, post your own! 

For reference, anything after a "#" is an annotation. ::

    $ history | awk '{a[$2]++ } END{for(i in a){print a[i] " " i}}'|sort -rn |head -n 20
    166 git     # I am a software developer.
    138 make    # Building the book takes 5 to 8 commands depending on format.
    68 touch    # Readying the book for kindle requires adding a lot of new files.
    51 python   # I am a Python developer and often use the shell.
    21 open     # Opening PDFs and Mobi to see how the book build works.
    12 rm       # I hate bad files.
    10 cd       # Intrigued that this isn't higher.
    9 kindled/kindlegen # Converting the book to .mobi format.
    7 heroku    # Support for clients.
    6 vim       # Sometimes I use it to keep my street cred up.
    5 bpython   # I like this shell. 
    3 source    # Activating virtualenv without virtualenvwrapper. Long story...
    3 cp        # Files need to be copied, right?
    3 gondor    # More client support.
    2 import    # I have no idea.
    1 wget      # Fetching files from the internets.
    1 pip       # More client support.
    1 ls        # How is this not higher?
    1 ssh       # Some projects are not on PaaS.

Interesting how much of my very recent shell experience is focused on the book_.

Speaking of books, today's reading is Jeff Knupp's `Writing Idiomatic Python 3.3`_ (Python 2.7 edition also available_)

.. _book: https://django.2scoops.org/
.. _`Writing Idiomatic Python 3.3`: http://www.amazon.com/Writing-Idiomatic-Python-3-3-ebook/dp/B00B5VXMRG/ref=tmm_kin_title_0?ie=UTF8&qid=1365610132&sr=8-1&tag=cn-001-20
.. _available: http://www.amazon.com/Writing-Idiomatic-Python-2-7-3-ebook/dp/B00B5KG0F8/ref=la_B00BBE1MDI_1_2_title_1_kin?ie=UTF8&qid=1365610777&sr=1-2&tag=cn-001-20