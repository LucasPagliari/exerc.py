import os
import sqlite3

os.remove("escola.db") if os.path.exists("escola.db") else None

# Conecta com o Database, se não cria um
con = sqlite3.connect('escola.db')
print(type(con))

# Permite percorrer pelos resgistros do db
cur = con.cursor()
print(type(cur))

# var
sql_create = 'create table cursos'\
'(id integer primary key,'\
'titulo varchar(100),'\
'categoria varchar(140))'

cur.execute(sql_create)

# Strings = comandos em SQL
sql_insert = 'insert into cursos values (?, ?, ?)'

recset = [(1000, 'Data Science Pratice','Data Science'),
			(1001,'Big data Fundamentos', 'Big Data'),
			(1002,'Python Fundamentos', 'Análise de Dados')]

# Inserindo Registros
for rec in recset:
	cur.execute(sql_insert, rec)

# Grava a Transação
con.commit()
# Seleciona Todos os Registros
cur.execute('select * from cursos')
# Recupera os resultados
dados = cur.fetchall()

for linha in dados:
	print('Id: %d, Título: %s, Categoria: %s' % linha)

print('\n')
recset = [(1003, 'Gestão de Dados com MongoMB','Big Data'),
			(1004,'R Fundamentos', 'Análise de Dados')]

for rec in recset:
	cur.execute(sql_insert, rec)

con.commit()
cur.execute('select * from cursos')
dados = cur.fetchall()

for linha in dados:
	print('Id: %d, Título: %s, Categoria: %s' % linha)

# Fecha a conexão
con.close()