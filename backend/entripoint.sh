#!/bin/sh

set -o errexit
# set -o pipefail
set -o nounset
python manage.py migrate
python manage.py collectstatic --noinput
# python manage.py collectstatic --noinput
gunicorn backend.asgi:application -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000 --chdir=$PWD