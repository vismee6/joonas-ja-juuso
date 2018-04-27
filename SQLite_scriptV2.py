#! /usr/bin/python3
# -*- coding: utf-8 -*-

"""
Copyright (c) 2018 Jani Mantynen & Ville Heikkiniemi
Permission is granted to copy, distribute and/or modify this document under
the terms of the GNU Free Documentation License, Version 1.3 or any later
version published by the Free Software Foundation; with no Invariant Sections,
no Front-Cover Texts, and no Back-Cover Texts. A copy of the license can be
found online at http://www.fsf.org/licensing/licenses/fdl.txt
"""

from serial import *
from datetime import *
import time
import json
import os

# Muuttujat
#JSON = '/var/www/html/project/data.json'
JSON = 'data.json' # Testasin työpöydällä

def Tapahtuma(data):
	# Haetaan JSON tiedosto. Jos ei ole, luodaan.
	try:
		with open(JSON) as tuonti:
			json_data = json.load(tuonti)
	except json.decoder.JSONDecodeError:
		json_data = {} # luo tyhjää
	except FileNotFoundError:
		json_data = {} # tee tyhjä tietokanta
		open(JSON, 'a').close() ## tietokanta syntyy
		os.chmod(JSON, 0o755) # ? oikeuksiin liittyvä

	# Päivitetään refenrenssiaika
	json_data['REF'] = int(time.time())  # tietue avain-arvo

	# Jos dataa on kaksi tavua, PROTOKOLLA
	if len(data) == 2:
		# Käydään läpi  JSON tietueet. Jos on olemassa, päivitetään aika. Jos ei ole, luodaan.
		lippu = 0 # vipu
		for avain, arvo in json_data.items():  # tietue kerrallaan
			if avain == data: # jos löytyy tällä avaimella oleva tietue
				json_data[avain] = int(time.time()) # hae uusi kellonaika
				lippu = 1

		if lippu==0:
			json_data[data] = int(time.time()) # uusi tietue
	# -------------------------------------------------
	# Kirjoitetaan JSON tiedostoon.
	try:
		with open(JSON, 'w') as outfile:
			json.dump(json_data, outfile)
	except Exception:
		print('Ei pysty kirjoittamaan')

def main():  # Ohjelman suoritus alkaa tästä
	# Yritetäänn luoda sarjaporttisoketti
	try:
		microbit = Serial(port='/dev/ttyACM0', baudrate=115200, timeout=2)
	except Exception:
		print('Tarkista portti')

	# Odotetaan sarjaporttiliikennettä Kuuntelee koko ajan ja iäti
	#	sarjaporttia
	while True: # Ikuinen luuppi!
		try:
			Tapahtuma(microbit.read(2).decode())
		except KeyboardInterrupt:
			print('Keskeytetään')
			sys.exit()  # Ohjelman lopetus

if __name__ == "__main__":
	main()  # Käynnisty
