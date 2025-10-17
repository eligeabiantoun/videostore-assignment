#!/usr/bin/env bash
set -e

python videostore/manage.py collectstatic --noinput || true
python videostore/manage.py migrate --noinput || true
exec python videostore/manage.py runserver 0.0.0.0:8000
