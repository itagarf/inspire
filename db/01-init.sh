#!/bin/bash
set -e
export PGPASSWORD=mysecretpassword;
psql -v ON_ERROR_STOP=1 --username "postgres" --dbname "postgres" <<-EOSQL
    CREATE DATABASE postgres;
EOSQL



###ignore


aws ecr get-login-password \
        --region eu-west-1 | docker login \
        --username AWS \
        --password-stdin <account-id>.dkr.ecr.us-east-1.amazonaws.com



aws ecr get-login-password --region eu-west-1 | docker login --username AWS --password-stdin 428253719401.dkr.ecr.eu-west-1.amazonaws.com




  config: |
    address-pools:
    - name: default
      protocol: layer2
      addresses:
      - 192.168.1.240 - 192.168.1.250