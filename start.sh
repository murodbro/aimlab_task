#!/bin/sh

python manage.py collectstatic

python manage.py migrate

gunicorn --bind 0.0.0.0:8000 configs.wsgi:application
