#!/bin/bash

docker compose exec mc_web_prod python manage.py makemigrations price_checker
docker compose exec mc_web_prod python manage.py migrate

