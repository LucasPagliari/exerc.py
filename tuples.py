import random

lis = sorted(random.sample(range(0,50),20))
print(lis)

# Não podem ser alteradas
tuple_ex = ("Sou","eu","Lucas")
tup = tuple(lis)
print(tup)

st = set(lis)
print(st)