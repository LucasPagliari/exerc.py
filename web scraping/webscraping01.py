from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import csv

with urlopen('https://osu.ppy.sh/rankings/osu/performance') as page:
	page = page.read()
	page_soup = soup(page, 'html.parser')
	# Busca todas tags tr com classe: x
	containers = page_soup.findAll('tr', {'class': 'ranking-page-table__row'})
	print('Top', len(containers), 'Players')

	# Abre arquivo para escrita('w'), newline evita linhas em branco
	with open('top_players_osu.csv', 'w', newline='') as file:
		field = ['rank', 'name', 'performance']
		# Escrever dados em csv
		csv_osu = csv.writer(file, delimiter=',')
		csv_osu.writerow(field)

		for con in containers:
			# Busca as tags com suas classes, .text.strip() pega o texto e retira espaços em branco
			rank = con.find('td', {'class': 'ranking-page-table__column ranking-page-table__column--rank'}).text.strip()
			name = con.find('span', {'class': 'ranking-page-table__user-link-text js-usercard'}).text.strip()
			score = con.find('td', {'class': 'ranking-page-table__column ranking-page-table__column--focused'}).text.strip()
			# Tratando os dados
			rank = rank.replace('#','')
			score = score.replace(',','')
			line = [rank, name, score]
			print(line)
			csv_osu.writerow(line)

		 

			
