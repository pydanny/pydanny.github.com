======
README
======

:date: 2012-02-17 00:30
:tags: python, blog
:category: blog


What I did to get it running::

    pip install pelican
    git clone git://github.com/pydanny/pydanny.github.com.git

How I push up entries and pages and themes::
    
    pelican . -o . -s settings.py
    git commit -am "blogging here"
    git push