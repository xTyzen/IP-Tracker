#!/usr/bin/python3
# IP Tracker V3.0.0
# Code By: xTyzenツ.py

import os
import sys
import json
import requests
import time
import folium
import webbrowser
import tempfile
from pystyle import *
from colorama import *

os.system("cls || clear")

intro = """  ██╗██████╗    ████████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ 
  ██║██╔══██╗   ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
  ██║██████╔╝█████╗██║   ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝
  ██║██╔═══╝ ╚════╝██║   ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
  ██║██║           ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
  ╚═╝╚═╝           ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝by xTyzenツ X                      
                              [!] Updated [!]

                             >> Press Enter <<"""

Anime.Fade(Center.Center(intro), Colors.white_to_red, Colorate.Vertical, interval=0.035, enter=True)

def aff():
    print(f"""{Fore.LIGHTRED_EX}    ________      ______                __                
   /  _/ __ \    /_  __/________ ______/ /_____  _____    
   / // /_/ /_____/ / / ___/ __ `/ ___/ //_/ _ \/ ___/    
 _/ // ____/_____/ / / /  / /_/ / /__/ ,< /  __/ /        
/___/_/         /_/ /_/   \__,_/\___/_/|_|\___/_/         
                                                 by xTyzenツIV
                      [!] Updated [!]""")

    time.sleep(1)

def ip():
    Write.Print("\n[+] >> Please enter the victim's IP address: ", Colors.white_to_green, end='')
    ip_addr = input()
    print("\n")

    req1 = requests.get(f"http://ipinfo.io/{ip_addr}")
    req2 = requests.get(f"http://ip-api.com/json/{ip_addr}")
    req3 = requests.get(f"http://api.db-ip.com/v2/free/{ip_addr}")

    resp1 = req1.json()
    resp2 = req2.json()
    resp3 = req3.json()

    Write.Print(f"[!] {json.dumps(resp3, indent=4)}", Colors.white_to_red)
    print("\n")
    Write.Print(f"[!] {json.dumps(resp1, indent=4)}", Colors.white_to_red)
    print("\n")
    Write.Print(f"[!] {json.dumps(resp2, indent=4)}", Colors.white_to_red)
    print("\n")

    if 'lat' in resp2 and 'lon' in resp2:
        lat = resp2['lat']
        lon = resp2['lon']
        print(f"Latitude: {lat}, Longitude: {lon}")

        mymap = folium.Map(location=[lat, lon], zoom_start=12)
        folium.Marker(
            location=[lat, lon],
            popup="The victim is here!",
            icon=folium.Icon(color="red", icon="info-sign")
        ).add_to(mymap)

        with tempfile.NamedTemporaryFile(delete=False, suffix=".html") as temp_file:
            map_path = temp_file.name
            mymap.save(map_path)

        webbrowser.open(f'file://{map_path}')

    Write.Print("[#] Results will be deleted in 25s [#]", Colors.blue_to_white)
    time.sleep(25)
    os.system("cls || clear")

while True:
    aff()
    ip()
