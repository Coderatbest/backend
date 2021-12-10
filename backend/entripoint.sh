#!/bin/sh

# set -o errexit
# #set -o pipefail
# set -o nounset

python manage.py migrate
python manage.py collectstatic --noinput
/usr/local/bin/gunicorn backend.asgi --bind 0.0.0.0:8000 --chdir=$PWD