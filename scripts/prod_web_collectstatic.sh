#!/bin/bash

docker compose exec mc_web_prod python manage.py collectstatic
