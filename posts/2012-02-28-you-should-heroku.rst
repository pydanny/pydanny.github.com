====================================
You should Heroku
====================================

:date: 2012-02-28 12:45
:tags: python, django, heroku
:category: python

In mid-November me and my fiancee, `Audrey Roy`_ began our startup. We had been frustrated with trying to do on-line product research and came up with an idea to take the lessons learned from `Django Packages`_ / `Open Comparison`_ and apply them to a commercial effort. The result has been `Consumer Notebook`_, and it's been a steadily growing success.

.. _`Audrey Roy`: http://audreymroy.com
.. _`Consumer Notebook`: http://consumernotebook.com
.. _`Django Packages`: http://djangopackages.com
.. _`Open Comparison`: http://opencomparison.org

We've been bootstrapping the project. That means supporting it with consulting and grinding away on it during our free time. That means 12-16 hour days of Python, Django, and Javascript coding, marketing, system administration, graphic design, communicating with users and vendors, and a thousand other tasks. Since we've had to explore new techniques for making things work on the backend and front end, that means we've needed to have a robust system that is trivial to deploy and certain to never go down. Which, of course, requires serious sys admin skills.

The Big Problem
===============

.. pull-quote::

    **I hate system administration work.**

Sys admin is boring. I find it tedious and dull. Devops doesn't make it easier/faster, it just makes it possible to do it at a large scale. 

Fortunately for me, my fiancee likes to the sys admin side of things. However, she's got serious programming skills in Python/Javascript, understands CSS, is an excellent illustrator, and has a good business skills to boot. Which means **I needed Audrey not to be doing sys admin**.

Solution: Platform as a Service
===============================

Platform as a Service, or PaaS_, is where someone else does the majority of work involved in system administration. There are now `dozens of companies edging into the Python capable PaaS space`_. We've been leery of using any of them but finally settled on `Heroku`_ after a long period of evaluation.

.. _PaaS: http://en.wikipedia.org/wiki/PaaS
.. _`Heroku`: http://heroku.com
.. _`dozens of companies edging into the Python capable PaaS space`: http://www.quora.com/What-is-the-Heroku-equivalent-for-Django-applications-Edit-Question-not-relevant-anymore-as-Heroku-now-supports-Django

Why Heroku?
===============================

We choose Heroku for a number of reasons:

#. We competed in a Los Angeles area Hacking contest with `Randall Degges`_. He was responsible for the sys admin and went with Heroku. He got it up and it was out of the way for the competition. He spent his time coding, adding features, and fixing templates instead of tweaking nobs on something in the cloud. We saw other people not deliver products at the contest because of this issue.
#. Heroku doesn't lock you in. If I wanted to, I could take all the pieces out in about 10 minutes, then go old school and host it myself on my own closet server.
#. Heroku has very good PostGreSQL_ support. Our web framework is Django_, which has an ORM that works best with PostGreSQL.
#. Heroku has staff. At least seventy of them. Odds are they would have people around 24/7 to deal with issues.
#. The add-on system means they've got many other people adding great new features. Want MongoDB_? No problem! How about something to `handle video`_? You got it!
#. Heroku scales up trivially. If we get an upswell of users, I just type ``heroku ps:scale web=50`` and I've got 50 web server things handling the load.
#. When I think of Heroku I think of Puffer Fish. Which is awesome because Puffer Fish are awesome.

.. _PostGreSQL: http://devcenter.heroku.com/categories/heroku-postgres
.. _Django: http://djangoproject.com

.. image:: http://farm6.staticflickr.com/5303/5776592544_fb15a2902a_m.jpg
   :name: Puffer Fish
   :align: center
   :target: http://www.flickr.com/photos/saspotato/5776592544/

Creative Commons: Some rights reserved by Saspotato_

.. _Saspotato: http://www.flickr.com/photos/saspotato/5776592544/

Things that we really liked about using Heroku
----------------------------------------------

As we progressed down the journey of building our site, we discovered even more nice features about Heroku. Here are some of the things that really make me smile:

#. `Releases`_ and especially `rollbacks`_ means we deploy with a lot more confidence.
#. `Logging`_ and other diagnostic add-ons like Sentry_ and `New Relic`_ means we know what's going on. 
#. During one huge data migration effort I scaled up the workers so a 6 hour task became a 5 minute task. Cost was less then 10 cents for workers instead of me losing hours of labor.
#. In case we go viral, we don't have to worry about load balancers and all that high performance stuff.

.. _MongoDB: https://addons.heroku.com/mongolab
.. _`handle video`: https://addons.heroku.com/pandastream
.. _`Randall Degges`: http://rdegges.com/
.. _`Rollbacks`: http://devcenter.heroku.com/articles/releases#rollback
.. _`Releases`: http://devcenter.heroku.com/articles/releases
.. _`Logging`: http://devcenter.heroku.com/articles/logging
.. _Sentry: https://addons.heroku.com/sentry
.. _`New Relic`: https://addons.heroku.com/newrelic

What does that mean?
=====================

It means I'm doing the deployments. I'm the sys admin. And I'm happy with my role because it takes minutes out of my day. Me and Audrey team up on everything else and the results so far have been great. If you've ever worked with me, the fact that `Consumer Notebook`_ is administered and deployed by me is going to be a shock. 

We've been able to really focus on development of the project. And when I mean development, I mean a lot of things. I mean:

* Python
* Django
* HTML
* CSS 
* JavaScript
* Data Modeling
* `Documenting the API`_
* Marketing: `blogging on Consumer Notebook`_, `Tweeting`_, and working with other groups
* Trying out `public tickets`_
* Iterating through the user experience by communicating to users
* All the boring legal and business stuff
 
.. _`public tickets`: https://github.com/consumernotebook/tickets/issues
.. _`blogging on Consumer Notebook`: http://insidertips.consumernotebook.com/
.. _Tweeting: https://twitter.com/consumernotebk
.. _`Documenting the API`: http://api.consumernotebook.com/

What you don't see is anything about sys admin issues. That's because what could have been a huge sink in time and resources is pretty much gone. We deploy staging servers with a bit of code I copy/pasted from a bash history into a Fabric script:

.. code-block:: python

    from fabric.api import local

    commands = """
    heroku create --stack cedar
    heroku addons:add memcache
    heroku config:add S3_KEY=HAHAHAHAHAHA S3_SECRET=NOTGIVINGITOUT
    heroku addons:add redistogo
    heroku addons:add sendgrid:starter
    heroku addons:add mongolab:starter
    heroku addons:add sentry:test
    heroku addons:add pgbackups
    heroku addons:add custom_domains:basic
    heroku addons:add zerigo_dns:basic
    heroku domains:add staging.consumernotebook.com
    heroku addons:add ssl:piggyback
    git push heroku master
    heroku scale web=1
    heroku addons:add heroku-postgresql:ronin
    heroku pg:wait
    """

    def build_staging():
        for command in commands.strip().split('\n'):
            local(command)

How awesome is that?

How much does Heroku really cost?
=================================

You can do Heroku for free. A lot of people do. More power to them.

But let's face it, beyond a certain point, every PaaS, including Heroku, is going to be more expensive then getting your own EC2, Rackspace, Dreamhost, or Linode hosted server. For a fraction of the cost, you can provision a server, install all the bits, configure the database, http server, load balancers, and even write Chef/Puppet/Fabric scripts so you can do it repeatedly at scale. Cheap!

So why pay more for Heroku? Why not just do it ourselves? For example, right now we're on dedicated PostGreSQL hosting which Heroku charges us $200/month. That's a lot, right? 

.. pull-quote::

    **Wrong.**

Right now we're seeing a 50% increase in visits every day. So if we ran our own servers, Chef/Puppet/Fabric or not, odds are we would be spending at least 10 hours a month doing server work. And I can assure you that when we consult that we make more than $20/hour.

.. pull-quote::

    **$200 < 10 hours of us doing consulting work to bootstrap the project.**

Until you hit a certain point, these days the real cost of servers is labor. If you're a developer and you think going with a cheap hosting provider is the way to go, think again. Think about the hours you're losing monkeying around with servers and databases instead of getting code done.

Heroku saves us money.

The Takeaway
============

One of the problems Django and other Python web frameworks has had is the difficulty of deployment. I can't tell you how many projects I didn't do because the thought of handling the sys admin side of things. Let's face it, one of the great ongoing successes for PHP is that deploying the majority of sites is trivial.

With the rise of devops we've seen a lot of developers across languages and frameworks dive into **Chef** and **Puppet**. It's been sadly amusing watching people much around with these great tools to make the deployment of 1-2 servers 'easier', when the real benefit of those tools has been to do things at scale. Things like deployments of fifty servers at once or deployment abstractions for hundreds of people (my fancy talk for PaaS).

In any case, things have changed. Deploying Python web apps is as trivial as deploying PHP code. It started with Google App Engine and `host of really good competitors`_.

For developers I see great times ahead.

.. http://insidertips.consumernotebook.com/images/robot-300x281.png
.. _`host of really good competitors`: http://www.quora.com/What-is-the-Heroku-equivalent-for-Django-applications-Edit-Question-not-relevant-anymore-as-Heroku-now-supports-Django