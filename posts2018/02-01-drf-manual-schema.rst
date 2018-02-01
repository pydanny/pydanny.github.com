=======================================================
Implemementing Manual Schema with Django REST Framework
=======================================================

:date: 2018-02-01 20:00
:tags: python, django, django-rest-framework, cheatsheet, howto, coreapi
:category: django
:description: Implementing a manual schema in Django REST Framework
:slug: manual-schema-django-rest-framework

.. image:: https://raw.githubusercontent.com/pydanny/pydanny.github.com/master/static/drf.png
   :align: center
   :alt: BitCoin and Two Scoops of Django!
   :target: https://www.pydanny.com/manual-schema-django-rest-framework.html

This is what will hopefully be the first in a series of reference articles for using `Core API`_ libraries with Django REST Framework (DRF_).  

This is an extraction from an existing production view running Django 1.11/2.0 on Python 3.6. The original code did something else, but for contract reasons I'm demonstrating this code with sending email.

Please note that this article is very terse, with almost no description, no tests, and no URL routing. Just enough code so that if you have a decent understand of DRF, you can make custom views work with Core API.

.. _`Core API`: http://www.coreapi.org/
.. _drf: http://www.django-rest-framework.org/

First, the serializer:

.. code-block:: python

    # serializers.py
    from django.core.mail import send_mail
    from markdown import markdown
    from rest_framework import serializers


    class EmailSerializer(serializers.Serializer):
        to_addresses = serializers.ListField(
            child=serializers.EmailField(),
            required=True
        )
        from_email = serializers.EmailField(required=True)    
        subject = serializers.CharField(required=True)
        message = serializers.CharField(required=True) 
        htmlize = serializer.BooleanField(required=False, default=False)  
        
        def create(self, validated_data):
            if validated_data['htmlize']:
                validated_data['html_message'] = markdown(validated_data['message'])
            send_mail(**validated_data)

Now the view:

.. code-block:: Python

    # views.py
    import coreapi
    import coreschema
    from rest_framework import schemas
    from rest_framework.views import APIView

    from .serializers import EmailSerializer
        
    class EmailCreateAPIView(APIView):
        """ Assumes you have set permissions and authentication in `settings.py`"""
        serializers = EmailSerializer
        schema = schemas.ManualSchema(fields=[
            coreapi.Field(
                "to_addresses",
                required=True,
                location="form",
                schema=coreschema.Array(
                  description="List of email addresses"
                )
            ),
            coreapi.Field(
                "from_email",
                required=True,
                location="form",
                schema=coreschema.String()
            ), 
            coreapi.Field(
                "subject",
                required=False,
                location="form",
                schema=coreschema.String()
            ),
            coreapi.Field(
                "message",
                required=False,
                location="form",
                schema=coreschema.String()
            ), 
        ])
        
        def post(self, request, format=None):
            serializer = EmailSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

Stay Tuned!
=============

I've decided to start posting my coding notes online again. These aren't tutorials, and may not be beginner friendly. Rather, these are code examples extracted from production systems that I'm putting up in a location I can reference easily that's 100% under my control. 

If you like what I'm doing, hit me up on Patreon_.

.. _Patreon: https://www.patreon.com/danielroygreenfeld