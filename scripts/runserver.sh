#!/bin/bash
set -e

# Start postgres service
docker-compose up -d postgres;

# Trap Ctrl+C
function ctrl_c() {
    docker-compose down
  }

trap ctrl_c INT

# Export environemnt variables
export POSTGRES_USER=user;
export POSTGRES_PASS=pass;
export POSTGRES_HOST=localhost;
export POSTGRES_DB=pagejobs;

# Run python manage commands
python phdnotes/manage.py runserver
