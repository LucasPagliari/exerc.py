import os

pa = 'C:/Users/Casa/Desktop/appa/RepositorioPython/material'

with open('lista.txt','r') as f:
	folders = f.read().split('\n')
	for folder in folders:
		newpa = ''
		newpa = pa + '/' + folder
		print(folder)
		print(newpa)
		if not os.path.exists(folder):
			os.makedirs(folder)