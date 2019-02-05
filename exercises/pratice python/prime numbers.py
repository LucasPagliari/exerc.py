def primes(nums):
	for ndivisor in nums:
		for nbase in nums:
			if nbase % ndivisor == 0 and nbase != ndivisor:
				nums.remove(nbase)
	return nums

x = int(input('Até qual número quer checar?:: '))

list_x = [i for i in range(1,x)]

for n in primes(list_x):
	print(n)