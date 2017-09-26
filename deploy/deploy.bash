#!/bin/bash

docker stop hacktheprinter && docker rm hacktheprinter && docker rmi hacktheprinter
[[ ! -f "dhparams.pem" ]] && openssl dhparam -out dhparams.pem 4096
docker build -t hacktheprinter .
docker run --name hacktheprinter -d -p 80:80 -p 443:443 -v /srv/hacktheprinter/conf/certs:/etc/nginx/certs:ro hacktheprinter && sleep 1 && docker ps
