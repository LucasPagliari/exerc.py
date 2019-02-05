import os
import sqlite3

os.remove("dsa.db") if os.path.exists("dsa.db") else None

conn = sqlite3.connect("dsa.db")

c = conn.cursor()

def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS produtos(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,'\
				'date TEXT, prod_name TEXT, valor REAL)')

def data_insert():
	c.execute('INSERT INTO produtos VALUES(10, "2018-05-02 21:57:10", "Teclado", 90)')
	conn.commit()

create_table()
data_insert()

for lines in c.execute('SELECT * FROM produtos'):
	print(lines)

c.close()
conn.close()