from functools import reduce
import random

lista = sorted(random.sample(range(0, 100),4))
print("Lista 1: " + str(lista))

def soma(a, b):
	x = a + b
	return x

# Aplica a função até o último elemento
# retorna um valor  
x = reduce(soma,lista)
print(x)

x = reduce(lambda a, b: a+b, lista)
print(x)

