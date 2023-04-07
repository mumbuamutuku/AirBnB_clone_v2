#!/usr/bin/env bash
# sets webserver for deplomment

sudo apt-get -y update
sudo apt-get install -y nginx

#Create the folder /data/web_static/releases/test/ if it doesn’t already exist
sudo mkdir -p /data/web_static/releases/test/

#Create the folder /data/web_static/shared/ if it doesn’t already exist
sudo mkdir -p /data/web_static/shared/

#Create a fake HTML file /data/web_static/releases/test/index.html
sudo echo "Hellow World" > /data/web_static/releases/test/index.html

#Create a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/ folder.
sudo ln -sf /data/web_static/releases/test /data/web_static/current

#Give ownership of the /data/ folder to the ubuntu
sudo chown -R ubuntu /data/
sudo chgrp -R ubuntu /data/

#Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
sudo printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /var/www/html;
    index  index.html index.htm;
    location https://mumbua.tech/hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }
    location /redirect_me {
        return 301 http://cuberule.com/;
    }
    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}" |sudo tee /etc/nginx/sites-available/default

#restart Nginx after updating the configuration
sudo service nginx restart
