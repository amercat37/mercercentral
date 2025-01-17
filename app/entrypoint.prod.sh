#!/bin/sh

if [ "$DATABASE" = "external" ]
then
    echo "Waiting for external database to start..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "External database started"
fi

#python manage.py makemigrations
#python manage.py migrate

exec "$@"
