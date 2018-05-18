import sqlite3

sqlited_file = "valo_ja_lampo.sqlite"
table_name1 = "poyta1"
table_name2 = "poyta2"
new_field = "alue1"
field_type = "INTEGER"

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

c.execute("CREATE TABLE {tn} ({nf} {ft})".format(tn = table_name1, nf = new_field, ft = field_type))

c.execute("CREATE TABLE {tn} ({nf} {ft} PRIMARY KEY)".format(tn = table_name2, nf = new_field, ft = field_type))

conn.commit()
conn.close()

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
