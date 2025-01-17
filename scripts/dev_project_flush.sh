#!/bin/sh

rm -rf ../app/price_checker/migrations/
sudo /bin/sh -c 'rm -rf /mount/docker-01/volumes/mercercentral/db_dev/data/*'
sudo /bin/sh -c 'rm -rf /mount/docker-01/volumes/mercercentral/sqladmin_dev/*'
