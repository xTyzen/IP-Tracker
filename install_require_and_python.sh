#!/bin/bash

sudo su

apt-get update -y
apt-get install python3
apt-get install python3-pip
clear
apt-get update -y
clear

pip install pystyle
pip install colorama
pip install requests
pip install jsonlib
pip install folium
pip install web-browser
pip install temp
