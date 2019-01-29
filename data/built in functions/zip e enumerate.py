# zip: une duas sequências, elementos a mais são ignorados
# enumerate: retorna uma tupla (índice, valor)

x = [a for a in range(1, 6)]
y = [a for a in range(6, 11)]
print(x, y)

itr = zip(x, y)

for i in itr:
    print(i)

print('\n')

# Listas com qnt. de elementos !=    
x = [a for a in range(1, 4)]
y = [a for a in range(6, 11)]
print(x, y)

itr = zip(x, y)

for i in itr:
    print(i)

print('\n')

# Dicionários
d1 = {'k1':1, 'k2':2}
d2 = {'k3':3, 'k4':4}

itr = zip(d1, d2)

print('\n', 'Keys')
for i in itr:
    print(i)


itr = zip(d1, d2.values())

print('\n', 'Keys d1 && Values d2')
for i in itr:
    print(i)
