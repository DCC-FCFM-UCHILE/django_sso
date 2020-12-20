#!/bin/bash
cd ..
. venv/bin/activate
cd src/django_sso
python manage.py runserver 0.0.0.0:5002
