import requests
import json

name = input('Username on Github: ')

link = 'https://api.github.com/users/'+name+'/repos'

data = requests.get(link).json()

# Keys dos Dicionários
# name
# language
# html_url
for repo in data:
	print(repo['name'], repo['language'])
	print(repo['html_url'])
	
	
