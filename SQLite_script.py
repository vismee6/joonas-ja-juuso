import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    try:
        yht = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        yht.close()

if __name__ == '__main__':
    create_connection("lampo_ja_valo.db")
