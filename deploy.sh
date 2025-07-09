#!/bin/bash
cd /home/ubuntu/docker-image
git pull origin main
docker stop umair-container || true
docker rm umair-container || true
docker build -t umair-image:latest .
docker run -d --name umair-container umair-image:latest
