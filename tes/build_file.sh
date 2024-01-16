#!/bin/bash

apt-get update
apt-get install -y libsqlite3-dev  # Install development files for SQLite

pip3 install --disable-pip-version-check --target . --upgrade -r /vercel/path0/tes/requirements.txt
python3.9 manage.py collectstatic --noinput
