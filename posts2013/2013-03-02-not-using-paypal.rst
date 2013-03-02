========================
We are not using PayPal
========================

:date: 2013-03-02 9:00
:tags: twoscoops, python, django, paypal, rant
:category: book
:slug: we-are-not-using-paypal


In January `Audrey Roy`_ and I launched a book_ about Django called `Two Scoops of Django: Best Practices for Django 1.5`_. We decided to not use PayPal. Here's why:


Open Source Events Get Burned By PayPal
=======================================

PayPal has a long, sordid history of freezing the accounts of Python related conferences and events around the world. In fact, this article was born out of the fact `DjangoCon Europe 2013 had its PayPal account frozen`_. In the past, `DjangoCon Europe 2012`_, Plone Conferences 2008, 2011, and at least one PyCon Australia dealt with the same PayPal problem (DjangoCon 2013 was forewarned and took measures to protect itself). We also have unconfirmed reports of other Python and Django events also running into problems with PayPal freezing accounts. Going with just confirmed conferences having issues with PayPal, this is a combined total of assets in excess of over US$100,000 dollars.

It's not just a Python issue either, it's an issue that `strikes other open source languages and tools`_. It's at the point now where `conference organizers don't trust PayPal`_ and make a point telling each other to use alternative payment gateways.

.. _`conference organizers don't trust PayPal`: http://aralbalkan.com/3898/

Fear, Shame, and PayPal
=========================

The terrifying thing to consider is that I suspect that the number of technical conferences affected by PayPal freezes is much, much larger. My reasoning is that **most conferences keep quiet about it** because **they're afraid that raising a fuss will annoy PayPal's anti-fraud division**. Let's also face the fact that **most people feel ashamed when bank accounts they are responsible for get frozen**, so probably don't publicize the issue.

.. _`strikes other open source languages and tools`: http://conferencesburnedbypaypal.tumblr.com/

The usual way conferences deal with these lockouts is conference organizers beg and borrow from friends, family, take second mortgages, local banking institutions, and pray that PayPal will eventually free their account. When you deal with a hostile, inaccessible payment gateway who won't let you provide for the hundreds or even thousands of people who paid you their hard earned money, it's the only way to get by.


The 'Needs' of PayPal's Anti-Fraud Division
===========================================

While I could respect the needs of PayPal's anti-fraud division when dealing with non-fungible products like ticket sales, it's **simply unacceptable** that prominent conferences for open source projects are treated this way. 

The software represented by these conferences drives the modern e-commerce world, including the myriad of systems that use PayPal to process sales. Yet PayPal continues to burn open source conferences year after year, and we've never heard of any conference outreach by their so-called 'developer evangelists' when a conference's account is frozen.

Legal recourse against PayPal is folly
=======================================

Ask any lawyer and they'll basically say against PayPal you have no options. PayPal has an army of lawyers and in most places isn't a bank, meaning your course of action is constrained from the beginning by your agreeing to PayPal's Terms of Service (TOS). Also, in the United States, their TOS prevents you from joining a class action lawsuit against them. Whether or not that TOS clause is enforceable in court, the fact that it's in their TOS greatly reduces any faith I might have had in them because it paints a picture of a company hostile to my needs.

In talking to authors and entrepreneurs, we've just heard (and read) too many horror stories. For merchants of non-fungible goods such as digital goods like the e-book I co-authored, PayPal seems even less trustworthy. 

Which means using PayPal places us at an unacceptable risk. We simply don't have the deep pockets to deal with PayPal freezing our funds for sales lost from a more reliable distribution system such as Stripe_ that powers our sales through _Gumroad.

.. _Stripe: https://stripe.com
.. _Gumroad: https://gumroad.com

It's Wrong to Use PayPal
=========================

Considering PayPal's unacceptable behavior in regards to the open source community I love and merchants who try to work in their system, I feel it's wrong to support PayPal. Audrey agrees, and so our policy of not using PayPal to sell the book is set.

.. _Amazon: https://amazon.com

PayPal is at Risk
===================

There was a day when Microsoft had what seemed to be an unassailable lock on the commercial software world. On many levels, Microsoft is a shadow of it's former self, and I contend it wasn't just Apple's competition. Instead, Microsoft's contempt for their own customers and the developer community hurt them just as much.

PayPal is on the same path of self-destruction. The've gone from the `scrappy company`_ helping people grow their business to the monolithic overlord that kills businesses and well-meaning events.

PayPal's demise won't happen this year, or the next, but every time they damage their customer base and the developer community it's another nail in the coffin. I submit that unless PayPal changes it's ways, within 5 years PayPal will be a shadow of it's former self as the army of growing competitors such as Stripe_, `Balanced Payments`_, wepay_, and Payoneer_ expands their availability and options around the world.

.. _wepay: https://www.wepay.com/
.. _Payoneer: https://www.payoneer.com/
.. _`Balanced Payments`: https://www.balancedpayments.com/

.. _`scrappy company`: http://www.amazon.com/The-PayPal-Wars-Battles-Planet/dp/0977898431/?tag=cn-001-20

What PayPal Can Do for Conferences
===================================

PayPal does have to worry about ticket sales for bogus events, since that  separates people from their money, but identifying real conferences is easy:

1. PayPal developer evangelists and community managers need to track every valid developer event in the world. It's the job of people in these roles to have the connections and subject matter expertise to identify real events from fake ones.
2. PayPal needs to sponsor these events. Why? See point #3.
3. PayPal's anti-fraud division needs to be informed that any PayPal sponsored event is off-limits.

What PayPal Can Do for Small Business
=====================================

PayPal has it's developer evangelists, community managers, and marketing departments working hard. However, at the end of the day, if you treat your customers with disrespect and a lack of trust, none of that matters. Bad press and market forces will see their revenues drop as customers will migrate to solutions that are more trustworthy and less antagonistic.

I believe that PayPal needs to revise how it's anti-fraud division communicates with people who have frozen accounts. They need to change the adversarial pose they take with their own customers to one that is collaborative. 

Note
========

This issue made me very angry. To help me calm down in order to write this article I found `this book`_ recommended by my friend Randall Degges.

If you are into Django, Python, or programming in general, check out the book I co-authored at https://django.2scoops.org/!

----

.. _`this book`: http://www.amazon.com/gp/product/0807012394/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=0807012394&linkCode=as2&tag=cn-001-20



.. _`DjangoCon Europe 2013 had its PayPal account frozen`: http://blog.djangocircus.com/post/43806402173/back-on-track
.. _`DjangoCon Europe 2012`: http://2012.djangocon.eu/


.. _tutorial: https://us.pycon.org/2013/schedule/presentation/11/
.. _`PyCon US`: https://us.pycon.org/2013/

.. _tutorials: https://us.pycon.org/2013/registration/register/
.. _LaTeX: http://www.latex-project.org/
.. _book: http://django.2scoops.org
.. _`Two Scoops of Django: Best Practices for Django 1.5`: http://django.2scoops.org
.. _`Audrey Roy`: http://audreymroy.com