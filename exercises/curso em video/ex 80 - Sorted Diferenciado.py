from random import sample
from time import time

num = sample(range(0, 100), 100)
num3 = sample(range(0, 100), 100)

num2 = []

t1 = time()
while num:
	minimum = num[0]
	for x in num:
		if x < minimum:
			minimum = x
	num2.append(minimum)
	num.remove(minimum)  
t2 = time()

print(num2)
print('tempo do algoritmo:', t2-t1)

t1 = time()
num3 = sorted(num3)
t2 = time()

print(num3)
print('tempo do sorted:', t2-t1)
