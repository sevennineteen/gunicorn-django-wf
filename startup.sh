#!/bin/bash
source bin/activate
export DJANGO_SETTINGS_MODULE=myproject.settings.$1
gunicorn_django -c etc/gunicorn.$1.conf &