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




https://stackoverflow.com/questions/71128069/postgres-database-not-connecting-to-flask-app-connection-to-server-at-localhos


https://medium.com/free-code-camp/docker-development-workflow-a-guide-with-flask-and-postgres-db1a1843044a

https://levelup.gitconnected.com/dockerizing-a-flask-application-with-a-postgres-database-b5e5bfc24848


psql -h 127.0.0.1 -p 5432 -U itagar -d inspire

https://gist.github.com/phortuin/2fe698b6c741fd84357cec84219c6667