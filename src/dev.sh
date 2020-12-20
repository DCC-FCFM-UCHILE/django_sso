#!/bin/bash
cd ..
. venv/bin/activate
cd src/django_sso
python manage.py runserver
