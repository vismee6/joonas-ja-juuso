from serial import *
import sqlite3

"""
print('<p>Loppu</p>')
print('</body>')
print('</html>')
"""

def lukia():
    conn = sqlite3.connect('tietokanta.db')
    c = conn.cursor()

    c.execute("SELECT * FROM taulu")

    conn.commit()
    conn.close()


def luoHTTPHeader():
    print("Content-type:text/html")
    print("""<!DOCTYPE html>
<html lang='fi'>
<head><title>Lämmin ja valoisa</title>
<link rel="stylesheet" href="jotain.css">
</head>""")

def luoSivunYlaosa():
    print("""<body>
<h1>Lämpö ja valo mittari</h1>
    """)
def LuoSivu(tiedot):
    print(tiedot)
    print("<p>Loppu</p>")
    print("</body>")
    print("</html>")

def main():
    luoHTTPHeader()
    luoSivunYlaosa()

    tiedot = lukia()

    LuoSivu(tiedot)

if __name__ == '__main__':
    main()
