import random

lista1 = sorted(random.sample(range(0,20),15))
lista2 = random.sample(range(0,20),15)

pares = []
for i in lista:
    if i%2 == 0:
        pares.append(i)
print(pares)

# Melhor maneira de se fazer:
impares = [i for i in lista if i%2 == 1] 
print(impares)
