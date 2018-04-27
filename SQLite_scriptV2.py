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
import sqlite3
import os

# Muuttujat
#sqlite3 = '/var/www/html/project/data.sqlite3'
sqlite3 = 'data.sqlite3' # Testasin työpöydällä

def Tapahtuma(data):
	# Haetaan sqlite3 tiedosto. Jos ei ole, luodaan.
	try:
		with open(sqlite3) as tuonti:
			sqlite3_data = sqlite3.load(tuonti)
	except sqlite3.decoder.sqlite3DecodeError:
		sqlite3_data = {} # luo tyhjää
	except FileNotFoundError:
		sqlite3_data = {} # tee tyhjä tietokanta
		open(sqlite3, 'a').close() ## tietokanta syntyy
		os.chmod(sqlite3, 0o755) # ? oikeuksiin liittyvä

	# Päivitetään refenrenssiaika
	sqlite3_data['REF'] = int(time.time())  # tietue avain-arvo

	# Jos dataa on kaksi tavua, PROTOKOLLA
	if len(data) == 2:
		# Käydään läpi  sqlite3 tietueet. Jos on olemassa, päivitetään aika. Jos ei ole, luodaan.
		lippu = 0 # vipu
		for avain, arvo in sqlite3_data.items():  # tietue kerrallaan
			if avain == data: # jos löytyy tällä avaimella oleva tietue
				sqlite3_data[avain] = int(time.time()) # hae uusi kellonaika
				lippu = 1

		if lippu==0:
			sqlite3_data[data] = int(time.time()) # uusi tietue
	# -------------------------------------------------
	# Kirjoitetaan sqlite3 tiedostoon.
	try:
		with open(sqlite3, 'w') as outfile:
			sqlite3.dump(sqlite3_data, outfile)
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
