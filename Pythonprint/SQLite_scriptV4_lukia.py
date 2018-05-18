from serial import *
import sqlite3

conn = sqlite3.connect('tietokanta.db')
print("tietokanta avattu")
c = conn.cursor()

c.execute("SELECT * FROM taulu")

conn.commit()

for row in c:
    print ("Testi ",row[0])

conn.close()

print("loppu")
