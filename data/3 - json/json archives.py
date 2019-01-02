# Criando um dicionário:
dict = {'nome': 'Lucas Alexandre',
        'linguagem': 'python',
        'similar': ['c','Modula-3','lisp'],
        'users': 20000,
        }

for x,y in dict.items():
    print(x,y)
print('\n')
import json
# Tranforma meu dicionário em objeto da biblioteca
json.dumps(dict)

with open('dados/3 - Manipulando JSON/dados.json','w') as archive:
    archive.write(json.dumps(dict))

with open('dados/3 - Manipulando JSON/dados.json','r') as archive:
    text = archive.read()
    data = json.loads(text)

print(data)
print('\n')

# web scrach - procurando dados na web
from urllib.request import urlopen

vim_response = urlopen('https://vimeo.com/api/v2/video/57733101.json').read().decode('utf8')

data = json.loads(vim_response)[0]

print('Título: ', data['title'])
print('url: ', data['url'])
print('Duração: ', data['duration'])
print('Duração: ', data['stats_number_of_plays'])
print('\n')

# copiando arquivo para outro
font = 'dados/3 - Manipulando JSON/dados.json'
base = 'dados/3 - Manipulando JSON/data.txt'

# Método 1
with open(font,'r') as infile:
    text = infile.read()
    with open(base,'w') as outfile:
        outfile.write(text)

# Método 2 +better+
open(base,'w').write(open(base,'r').read())