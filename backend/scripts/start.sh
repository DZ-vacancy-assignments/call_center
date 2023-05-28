#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset
set -o xtrace

python manage.py makemigrations users call_center
python manage.py migrate
# python manage.py migrate users
# python manage.py migrate call_center
python manage.py collectstatic --noinput --verbosity 0
python manage.py runserver_plus 0.0.0.0:8000
