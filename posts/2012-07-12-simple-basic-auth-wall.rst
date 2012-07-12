===========================
Simple HTTP Basic Auth Wall
===========================

:date: 2012-07-09 12:00:00
:tags: python, django, wsgi
:category: python

I have a client who wanted their entire unlaunched public content site quickly but temporarily blocked for a short period of time. He wanted a universal password so he could send the site to reviewers, done quickly, and nothing else. In a few days the site will launch, and even if someone got through the authentication, nothing bad will happen except for an early visitor. So we determined this was a job for a very simple `Basic access authentication`_ implementation.

.. _`Basic access authentication`: https://en.wikipedia.org/wiki/Basic_access_authentication

I asked around and `Jacob Kaplan-Moss`_ gave me this awesome snippet using barrel_ that I pasted right into the bottom of the Django_ 1.4-style application's ``wsgi.py`` file.

.. _Django: http://djangoproject.com
.. _barrel: http://pypi.python.org/pypi/barrel
.. _`Jacob Kaplan-Moss`: http://jacobian.org/

.. code-block:: python

    # Add to the bottom of your wsgi.py file
    # Don't forget to add barrel to your requirements!
    from barrel import cooper

    REALM = "PRIVATE"
    USERS = [('spam', 'eggs')]

    application = cooper.basicauth(users=USERS, realm=REALM)(get_wsgi_application())


This took all of 5 minutes to implement and launch. The result is that the first time you visit the site the login prompt appears. If you enter 'spam' and 'eggs' then you can see the site fine.

It worked and the customer was happy. 

Will this block a concerted penetration attempt? Of course not. If the site has/had critical or identifying information it would be implemented with HTTPS_. Implementing a Django site with HTTPS is something I've done many times now, but this use case was 'do it fast, easy, and make it temporary'.

**Moral of the story:** Pay attention to your requirements.

**Note :** As this is just adding in some WSGI middleware, this should work without much modification in Flask, Pyramid, and other WSGI compliant web frameworks.

.. _HTTPS: https://en.wikipedia.org/wiki/HTTPS