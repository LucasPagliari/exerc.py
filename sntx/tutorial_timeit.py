import timeit

input_list = range (100)

def div_five(num):
	if num % 5 == 0:
		return True
	else:
		return False

list_x = (i for i in input_list if div_five(i))

list_y = [i for i in input_list if div_five(i)]

print(timeit.timeit('''input_list = range (100)

def div_five(num):
	if num % 5 == 0:
		return True
	else:
		return False

list_y = [i for i in input_list if div_five(i)]''', number=1000))