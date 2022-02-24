==================
Django-Admin-Mazer
==================

Django-Admin-Mazer is a Django app to change design of default Django admin panel. 
It is based on Bootstrap 5 and an open-source template named Mazer.
It is developed to be a drop-in replacement for Django's default admin panel 
unlike other admin panel libraries which require extra configurations.

Quick start
-----------

1. Add "django_admin_mazer" to your INSTALLED_APPS setting above "django.contrib.admin" like this::

    INSTALLED_APPS = [
        'django_admin_mazer',
        "django.contrib.admin",
        ...
    ]

2. Start the development server and visit http://127.0.0.1:8000/admin/ or your admin url.
   The "Mazer" template should override the default admin panel designs.
