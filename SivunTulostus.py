"""
print('<p>Loppu</p>')
print('</body>')
print('</html>')
"""

def lukia():
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

def luoHTTPHeader():
    print("Content-type:text/html/n/n")
    print("""<!DOCTYPE html>
    <html lang='fi'>
    <head><title>Lämmin ja valoisa</title>
    <link rel="stylesheet" href="jotain.css">
    </head>
    """)

def luoSivunYlaosa():
    print("""<body>
    <h1>Lämpö ja valo mittari</h1>
    """)
    def LuoSivu(tiedot):
        print(tiedot)
        print("<p>Loppu</p>")
        print("</body>")
        print("</html>")

def sivu():
    luoHTTPHeader()
    luoSivunYlaosa()

    tiedot = lukia()

    LuoSivu(tiedot)

if __name__ == '__sivu__':
    sivu()
