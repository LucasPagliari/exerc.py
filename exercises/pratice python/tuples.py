# Não podem ser alteradas
from collections import namedtuple

Lucas = namedtuple('Lucas',['lastname', 'age', 'favcolor']) 

p = Lucas('Pagliari', 20, 'Blue')

print(p.lastname)
print(p.age)
print(p.favcolor)