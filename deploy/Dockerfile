# Copyright 2013 Thatcher Peskens
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

FROM ubuntu:16.04

MAINTAINER Dockerfiles

# Install required packages and remove the apt packages cache when done.
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 8B3981E7A6852F782CC4951600A6F0A3C300EE8C
RUN echo "deb http://ppa.launchpad.net/nginx/stable/ubuntu xenial main" > /etc/apt/sources.list.d/nginx.list
RUN apt-get update && \
    apt-get upgrade -y && \ 	
    apt-get install -y \
	git \
	python3 \
	python3-dev \
	python3-setuptools \
	python3-pip \
	nginx \
	supervisor \
	sqlite3 \
    tzdata && \
	pip3 install -U pip setuptools && \
   rm -rf /var/lib/apt/lists/*

# Set timezone
# https://www.ivankrizsan.se/2015/10/31/time-in-docker-containers/
RUN echo "America/Argentina/Buenos_Aires" >/etc/timezone && \
    ln -sf /usr/share/zoneinfo/America/Argentina/Buenos_Aires /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata

# Create limited user
RUN useradd -U -m -d /home/docker -s /bin/bash app

# install uwsgi now because it takes a little while
RUN pip3 install uwsgi

# setup all the configfiles
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
RUN sed -i '/^user /s/.*/user app;/' /etc/nginx/nginx.conf
#COPY nginx.conf /etc/nginx/nginx.conf
COPY dhparams.pem /etc/nginx/dhparams.pem
COPY nginx-app.conf /etc/nginx/sites-available/default
COPY supervisor-app.conf /etc/supervisor/conf.d/


# COPY requirements.txt and RUN pip install BEFORE adding the rest of your code, this will cause Docker's caching mechanism
# to prevent re-installing (all your) dependencies when you made a change a line or two in your app.

COPY app/requirements.txt /home/docker/code/app/
RUN pip3 install -r /home/docker/code/app/requirements.txt

# add (the rest of) our code
COPY . /home/docker/code/

# Drop privs
#USER app:app
#ENV HOME /home/docker

# install django, normally you would remove this step because your project would already
# be installed in the code/app/ directory
# RUN django-admin.py startproject website /home/docker/code/app/
WORKDIR /home/docker/code/app/eko
RUN python3 manage.py check
RUN python3 manage.py collectstatic
RUN python3 manage.py makemigrations
RUN python3 manage.py migrate

# Fix permissions
RUN chown -R app:app /home/docker/ /var/log/nginx

EXPOSE 80

# supervisor must run as root
CMD ["supervisord", "-n"]
