import os 
import sqlite3
import random
import datetime
import matplotlib.pyplot as plt

os.remove('course.db') if os.path.exists('course.db') else None

conn = sqlite3.connect('course.db')
c = conn.cursor()

def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS produtos'\
				'(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,'\
				'date TEXT, prod_name TEXT, valor REAL)')

def random_data_insert():
	with open('produtos.txt', 'r') as f:
		produtos = f.read().split('\n')
		prod = random.choice(produtos)
		valor = random.randrange(100,5000)
		time = datetime.datetime.now()
		c.execute('INSERT INTO produtos (date, prod_name, valor) VALUES ( ?, ?, ?)',
					(time, prod, valor))
		conn.commit()

def data_query_all():
	c.execute('SELECT * FROM produtos')
	for data in c.fetchall():
		print(data)

def data_query():
	c.execute('SELECT * FROM produtos WHERE valor > 2500')
	for data in c.fetchall():
		print(data)

def update_values():
	c.execute('UPDATE produtos SET valor = 500 WHERE valor < 1000')
	conn.commit()

def delete_data():
	c.execute('DELETE FROM produtos WHERE valor > 4000')
	c.execute('DELETE FROM produtos WHERE valor < 1000')
	conn.commit()

def create_graph():
	c.execute('SELECT id, valor FROM produtos')
	ids = []
	values = []
	for i, v in c.fetchall():
		ids.append(i)
		values.append(v)
	plt.bar(ids, values)
	plt.show()


create_table()	
for i in range(9):
	random_data_insert()
	print('criando dados')
data_query_all()
update_values()
create_graph()
