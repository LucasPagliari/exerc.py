# Filtra os elementos que retornam true da função
from random import sample

lista = sorted(sample(range(10, 1000), 10))
print(lista)


def par(x):
    if x % 2 == 0:
        return True
    else:
        return False

# (Function, list)    
x = list(filter(par, lista))
# Return an iterator
print(x)


# Better way
x = list(filter(lambda num: num % 2 == 0, lista))
print(x)
