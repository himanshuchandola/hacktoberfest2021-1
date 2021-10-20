import requests

import json

ipaddress = input("Ip Address : ")

iprequest = requests.get(f"http://ip-api.com/json/{ipaddress}")

if iprequest.status_code == 200:

	ipdata = json.loads(iprequest.text)

	if ipdata["status"] == "success":

		for key in ipdata:

			print(f"{key.capitalize()} : {ipdata[key]}")

			

			if key == "lon":

				lat = ipdata["lat"]

				lon = ipdata["lon"]

				maps = f"https://www.google.com/maps/@{lat},{lon},9z"

				print(f"Maps : {maps}")
