#!/bin/bash
set -e

# Start postgres service and run migrations commands
docker-compose up -d postgres;
docker-compose run django python phdnotes/manage.py makemigrations
docker-compose run django python phdnotes/manage.py migrate
docker-compose down
