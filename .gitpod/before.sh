# /bin/bash

echo BEFORE

cd /workspace/django_sso/app
pip install --upgrade pip
pip install -r _requirements/base.txt -r _requirements/develop.txt
pur -r _requirements/base.txt
pur -r _requirements/production.txt
