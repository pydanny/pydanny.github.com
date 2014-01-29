=========================================================
Tablib: Turning Data into Tables
=========================================================

:date: 2014-01-28 12:00
:tags: python, ppoftw
:category: python
:slug: tablib-turning-data-into-tables
:status: draft

Over the years I've had to do the following many, many times:

* Take oddly shaped data and organize it into a table-style format.
* Export the newly formatted data into one (or more) of JSON, CSV, HTML, Excel, and more.

For years, my solution was to create custom transformation code. This usually worked well enough, until I needed to export data into more than one format. This would force me to extend my code, more often than not turning existing elegant code into something unseemly and tasting of spaghetti_.

Then I discovered Tablib_.

Introducing Tablib
==================

**Tablib**, created and maintained by `Kenneth Reitz`_ (of requests_ fame), at it's heart does just two things:

* Provides an easy, pythonic_ way to construct and manipulate tabular datasets.
* Provides six export formats for these datasets. These include JSON, CSV, TSV, HTML, YAML, Excel. It's actually seven formats if you count Python dictionaries (**dict**) as an export.

Quick Tablib Tutorial
=======================

To set the stage, I'm going to introduce **tablib** quickly. 

Creating and Manipulating Datasets
----------------------------------

As mentioned above, the first thing tablib does is allow us to manage datasets.  Using the pytest_ library (described previously), let's put **tablib** through it's paces.

.. code-block:: python
    
    # -*- coding: utf-8 -*-
    # test_tablib.py
    from __future__ import unicode_literals
    import pytest
    import tablib

    @pytest.fixture
    def words():
        """Fixture we'll use in many places of this article"""
        return (
            (u"road", u"straße"),
            (u"ice cream", u"Eis"),
        )

    def test_basic_dataset_creation(words):
    
        # create a tablib dataset
        data = tablib.Dataset()

        # Iterate through our words
        for word in words:
        
            # The .append() method accepts a flat iterable as it's first argument.
            data.append(word)
            
        assert data.dict[0] == [u'road', u'straße']
        
You might wonder, why does the assertion at the end of that code example behave as if the **dict** export is a list of strings? Well, that's because once you add headers to your data, **tablib** returns a list of **dict**. Well, actually it's a list of `collections.OrderedDict`_, but that's fine with me:

.. code-block:: python

    # continued from test_tablib.py above
    from collections import OrderedDict
    
    @pytest.fixture
    def data(words):
        """Common dataset fixture. Shortened to 'data' to aid with formatting
        issues. No one likes 80+ characters on a line of code. ;)"""
        
        data = tablib.Dataset()
        for word in words:
            data.append(word)
        return data
    
    def test_dataset_export_dict(data):
        
        # Add headers as a list of strings
        data.headers = ('English', 'German')
        
        # The dict export now returns a list of OrderedDict
        assert data.dict[0] == {u'English': u'road', \
                                        u'German': u'straße'}
        assert isinstance(data.dict, list)
        assert isinstance(data.dict[0], OrderedDict)

**Tablib** also allows us to add new columns:

.. code-block:: python

    # continued from previous example

    def test_dataset_add_column(data):
        
        data.headers = ('English', 'German') # Add headers as a list of strings
        
        # Assert that an individual row has two columns (English, German)
        assert len(data.dict[0]) == 2
        
        # The .append_col method accepts a header argument. In this case, 'French'
        data.append_col([u'route', u'crème glacée'], header='French')
        
        # Assert individual rows have three columns: (English, German, French)
        for row in data.dict:
            assert len(row) == 3
            
        # Assert that the new column exists
        assert data.dict[0] == {u'English': u'road', \
                                        u'French': u'route', \
                                        u'German': u'straße'}

As you can see, since the **dict** property returns built-in Python objects (a **list** of **OrderedDict**), we can slice and dice to our heart's content.

Exporting Datasets
------------------

The easy exports of tablib are really nice. We don't have to load a serializer or do any heavy lifting to get started. You just call properties on datasets. I'll demonstrate in code:

.. code-block:: python

    # continued from previous example

    def test_exports(data):
        """All of these assertions will be forced to wrap."""
        
        data.headers = ('English', 'German')

        # JSON - fails because the new tablib isn't released yet
        assert data.json == u'[["road", "straße"], ["ice cream", "eis"]]'
        
        # HTML
        print data.html
        assert data.html == u'''<table>
    <tr><td>road</td>
    <td>straße</td></tr>
    <tr><td>ice cream</td>
    <td>eis</td></tr>
    </table>'''
    
        # CSV - Should have 3 records.
        assert len(data.csv.splitlines()) == 3

        # TSV - Should have 3 records.
        assert len(data.tsv.splitlines()) == 3
        
        # Checking TSV columns. There should be 2.
        record = data.tsv.splitlines()[0]
        assert len(record.split("\t")) == 2
        
        # YAML - Tablib comes bundled with the pure Python version of pyyaml.
        #   For increased performance, install pyyaml from PyPI.
        assert len(data.yaml.splitlines()) == 3
        
If you want to know more about **tablib** provides, it's been nicely documented_. In the meantime, now that we've got that down, lets move on to a practical use case. 

The Generic SQLAlchemy Translation Function
============================================

TODO: Write this portion

* TODO: Use tablib to export using fields determined by SQLAlchemy's query.column_descriptions
* TODO: Write function that accepts a queryset and an export format then does all the work.

.. _documented: http://docs.python-tablib.org/

.. _`collections.OrderedDict`: http://docs.python.org/2/library/collections.html#collections.OrderedDict
.. _requests: https://pypi.python.org/pypi/requests
.. _spaghetti: https://en.wikipedia.org/wiki/Spaghetti_code
.. _Tablib: http://docs.python-tablib.org/
.. _pythonic: https://en.wikipedia.org/wiki/Python_(programming_language)#Features_and_philosophy
.. _`Kenneth Reitz`: https://twitter.com/kennethreitz
.. _pytest: https://pypi.python.org/pypi/pytest