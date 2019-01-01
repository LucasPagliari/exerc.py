import csv

count   = 0
newlist = []

with open("payments.csv", "r") as pay:
    leitor =  csv.reader(pay)
    for x in leitor:        
        count += 1
        if count % 100000 == 0:
            newlist.append(x)
            print(x)

print(newlist)

       