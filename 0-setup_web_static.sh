#!/usr/bin/env bash
# sets up my web servers for the deployment of web_static

sudo apt-get update
sudo apt-get -y install nginx

sudo mkdir -p /data/web_static/releases/test/ /data/web_static/shared/

sudo sh -c 'echo "Holberton school by maged" >/data/web_static/releases/test/index.html'

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sh -c 'echo "
server {
    listen 80;
    add_header X_Served_by \$HOSTNAME;
    listen [::]:80 default_server;
    server_name magedsaif.tech;
    location /hbnb_static {
        alias /data/web_static/current/;
    }
}" > /etc/nginx/sites-available/default'

sudo service nginx restart