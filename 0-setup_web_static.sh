#!/usr/bin/env bash
# Script that sets up my web servers for the deployment of web_static
apt-get -y update
apt-get -y install nginx
service nginx start
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo sh -c 'echo "Holberton school"> /data/web_static/releases/test/index.html'
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '19i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n' /etc/nginx/sites-available/default
service nginx restart
