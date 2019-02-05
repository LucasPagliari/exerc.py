import math
def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1))

x = int(input('Até qual número quer checar?:: '))

nums = (n for n in range(3, x) if is_prime(n))

for n in nums:
	print(n)