#!/bin/bash
WEBLFAS_APP_ID=$1
WEBLFAS_SECRET_KEY=$2
sudo apt-get install wget
wget -O target.mp3 $3
python3 webflas.py
python3 parser.py