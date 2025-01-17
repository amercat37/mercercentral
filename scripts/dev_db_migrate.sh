#!/bin/bash

docker compose exec mc_web_dev python manage.py makemigrations price_checker
docker compose exec mc_web_dev python manage.py migrate

