#!/bin/bash
export WEBLFAS_APP_ID=$1
export WEBLFAS_SECRET_KEY=$2
sudo apt-get install python3-pip -y && pip3 install -r requirements.txt
sudo apt-get install wget -y
wget -O target.mp3 $3
python3 weblfas.py && python3 parser.py
