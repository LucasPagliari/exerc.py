# Github API with Python

from urllib.request import urlopen
import json

name = 'LucasPagliari' #input('Username on Github: ')
link = 'https://api.github.com/users/'+name+'/repos'
resp = urlopen(link).read().decode('utf-8')
data = json.loads(resp)

for repo in data:
	print(repo['name'], repo['language'])
	print(repo['html_url'])
	print('\n')
	

