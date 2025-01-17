#!/bin/bash

docker compose exec mc_web_dev python manage.py flush --no-input

