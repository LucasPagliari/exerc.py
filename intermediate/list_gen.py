# List: Run out of memory
x = [i for i in range(6)]

# Generator: Run out of time
y = (i for i in range(6))
print(y)

print('\n')

input_list = [20, 5, 6, 1, 2, 5, 15, 11, 50, 3]

def div_five(num):
	if num % 5 == 0:
		return True
	else:
		return False


list_y = (i for i in input_list if div_five(i))
[print(i) for i in list_y]

print('\n')

xyz = ([i, ii] for ii in range(4) for i in range(4))

print(xyz)
print([i for i in xyz])
