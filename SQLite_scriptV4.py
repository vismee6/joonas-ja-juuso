from serial import *
import sqlite3

def Tapahtuma(data):
    if len(data) > 5:
        try:
            conn = sqlite3.connect('tietokanta.db')
        except Exception:
            print("tietokantaa ei avattu")
            sys.exit()

        c = conn.cursor()
        lampo = (data[5:len(data)])
        valo = (data[5:len(data)])
        c.execute("INSERT INTO taulu VALUES (?, ?)", (lampo, valo))
        conn.commit()
        conn.close()

def main():
    try:
        microbit = Serial(port='/dev/ttyACM0', baudrate=115200, timeout=2)
    except Exception:
        print("tarkista portti")
    while True:
        try:
            Tapahtuma(microbit.readline().decode())
        except KeyboardInterrupt:
            print("keskeytetään")
            sys.exit()
if __name__ == "__main__":
    main()
