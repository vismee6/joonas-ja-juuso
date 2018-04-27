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
