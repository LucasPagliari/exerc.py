import csv

count = 0
with open('dados/2 - csv/payments.csv','r') as f:
    data = csv.reader(f, delimiter='\n')
    for row in data:
        if count < 10:
            print(row)
        count += 1