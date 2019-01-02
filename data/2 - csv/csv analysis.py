# Dados obtidos em: https://data.cityofchicago.org/

f           = open("dados/2 - csv/payments.csv","r")
pay         = f.read()
rows        = pay.split("\n")
full_data   = []
count       = 0

for row in rows:
    row_split = row.split(",")
    full_data.append(row_split)
    count += 1

print(full_data[10000])
print("Este arquivo tem: " + str(count) + " linhas")
