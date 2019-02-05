limit = int(input('Até qual número: '))

def palindromo(num):
	num = str(num)
	if num == num[::-1]:
		return True
	return False

list_gen = (x for x in range(0,limit) if palindromo(x))

for num in list_gen:
	print(num)