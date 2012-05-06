===========
My new blog
===========

:date: 2012-02-17 00:30
:tags: python, blog



What I did to get it running::

    pip install pelican
    git clone git://github.com/pydanny/pydanny.github.com.git

My settings.py file::

    AUTHOR = 'Daniel Greenfeld'
    DISQUS_SITENAME = 'pydanny'
    GITHUB_URL = 'https://github.com/pydanny'
    GOOGLE_ANALYTICS='UA-18066389-2'
    SITEURL = 'http://pydanny.github.com'
    SITENAME = 'pydanny'
    SOCIAL = (('twitter', 'http://twitter.com/pydanny'),
              ('github', 'https://github.com/pydanny'),
              ('facebook', 'http://www.facebook.com/daniel.greenfeld'),)
    TAG_FEED = 'feeds/%s.atom.xml'
    THEME='notmyidea'
    TWITTER_USERNAME = 'pydanny'

How I push up entries and pages and themes::
    
    pelican . -o . -s settings.py
    git commit -am "blogging here"
    git push
    
Results!
========

http://pydanny.github.com