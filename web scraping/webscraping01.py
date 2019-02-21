from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import csv

with urlopen('https://osu.ppy.sh/rankings/osu/performance') as page:
	page = page.read()
	page_soup = soup(page, 'html.parser')
	containers = page_soup.findAll('tr', {'class': 'ranking-page-table__row'})
	print('Top', len(containers), 'Players')

	with open('top_players_osu.csv', 'w') as file:
		field = ['rank', 'name', 'performance']
		csv_osu = csv.writer(file, delimiter=',')
		csv_osu.writerow(field)

		for con in containers:
			rank = con.find('td', {'class': 'ranking-page-table__column ranking-page-table__column--rank'}).text.strip()
			name = con.find('span', {'class': 'ranking-page-table__user-link-text js-usercard'}).text.strip()
			score = con.find('td', {'class': 'ranking-page-table__column ranking-page-table__column--focused'}).text.strip()
			score = score.replace(',','')
			line = [rank, name, score]
			csv_osu.writerow(line)

		 

			
