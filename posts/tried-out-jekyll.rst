================
Tried out Jekyll
================

:date: 2012-02-09 10:20
:tags: ruby, blog
:category: blog

Why move my blog?
=================

I've had issues with Blogger for some time.  After my fiancee, Audrey Roy, moved her blog to https://github.com/mojombo/jekyll, I was impressed enough to give it a try.

Why did it impress me?

Code highlighting made easy
===========================

I don't have to hand-craft HTML code to get google prettify in a post. I just stick in a simple macro of 'highlight python' called like a Django templatetag and I get:

.. code-block:: python

    name = 'Daniel Greenfeld'
    for letter in name.split():
        print(letter)


This issue alone sums up why I don't do more blog posts with code.

I don't want to maintain my own blog site
=========================================

A couple times I rolled out a blog on a site I stood up, but didn't really feel like maintaining a site. I want someone else to do it. When I write, I want someone else to worry about the details. I want to focus on writing and nothing else.

I want to be able to write without connection
======================================================

I need an internet connection to get my blogger posts to format right. With Jekyll, I can just type away.

Ability to publish via git
===========================

My https://pydanny-event-notes.rtfd.org has really exploded in my own usage and continued because it uses the same patterns I use in software development. I'm used to the pattern of using Git to push up content, so why use naked HTML? Sure, there are RST-to-HTML processors that I could use to generate that HTML, but they always require an some amount of manual correction. Jekyll, and it's alternatives,let me just write.