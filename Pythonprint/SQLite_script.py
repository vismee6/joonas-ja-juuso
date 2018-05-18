from serial import *
from datetime import *
import sqlite3
from sqlite3 import Error


def create_connection(sqlite_file):
    try:
        yht = sqlite3.connect(sqlite_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        yht.close()

if __name__ == '__main__':
    create_connection("lampo_ja_valo.sqlite")
