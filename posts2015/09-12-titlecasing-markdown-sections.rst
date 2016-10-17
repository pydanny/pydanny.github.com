========================================
Titlecasing Markdown Headers with Python
========================================

:date: 2015-09-12 09:00
:tags: python, markdown, ppoftw
:category: python
:slug: titlecasing-markdown-headers-with-python


.. image:: https://pydanny.com/static/title-case.png
   :name: Markdown
   :align: center
   :alt: Markdown
   :target: https://www.pydanny.com/static/title-case.png


Recently I've been writing a lot of Markdown. While not as sophisticated as ReStructuredText, it's simplicity is nice for accelerated writing. The problem is that I like to put section headings in *titlecase*.

What do I mean by titlecase?

::

    go to the room

becomes::

    Go to the Room

See how verb 'Go' and the noun 'Room' have their first letter capitalized? And the 'small words', specifically 'to' (preposition) and 'the' (definate article) are not? That's how title casing works (at least in English). That's what I like to see in my section headings.

In theory one could just use Python's ``str.title()`` method to perform this transformation. However, that method is too global in reach. We would end up with::

    Go To The Room  # 'to' and 'the' have titlecase, when they should not.

So how do I programmatically (i.e. quickly) ensure that dozens of files scattered across multiple directories have section headers that are accurately titlecased?

Accurately Titlecasing Programmatically
=======================================

The solution to this is a handy library called titlecase_. Empowered by this tool I wrote the following script that allows me to transforms all my markdown files to have titlecased section headings.

.. _titlecase: https://pypi.python.org/pypi/titlecase

.. code-block:: python

    """
    Titlecases all markdown section headers in a directory.
    Confirmed to work with Python 2.7, 3.3, and 3.4.

    Usage:

      python titlemd.py a-directory/
      python titlemd.py  # defaults to '.'
    """

    import fnmatch
    import os
    import sys

    try:
      from titlecase import titlecase
    except ImportError:
      print("Please install titlecase")

    def main(location):
      for root, dirs, files in os.walk(location):
          for item in fnmatch.filter(files, "*.md"):
              file_path = os.path.join(root, item)
              print(file_path)

              # Open the file and read the lines as a list
              with open(file_path) as f:
                  lines = f.readlines()

              with open(file_path, 'w') as f:
                  # Loop through the list of lines and titlecase
                  # any line beginning with '#'.
                  for line in lines:
                      if line.strip().startswith('#'):
                          line = titlecase(line)
                      f.write(line)

    if __name__ == "__main__":
      try:
          main(sys.argv[1])
      except IndexError:
          main('.')
