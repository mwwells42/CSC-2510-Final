FROM ubuntu:20.04

COPY /app /app

RUN apt-get update && \
    apt-get install -y sudo curl git nano && \
    adduser --quiet --disabled-password 
    --shell /bin/bash --home /home/devuser 
    --gecos "User" devuser && \
    echo "devuser:<a href="mailto://p@ssword1">p@ssword1</a>" | 
    chpasswd &&  usermod -aG sudo devuser