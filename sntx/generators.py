
# Generator:
def simple_gen():
	yield 'Oh'
	yield 'hello'
	yield 'there'

for i in simple_gen():
	print(i)


password = (3, 6, 1)

def combo_gen():
	for c1 in range(10):
		for c2 in range(10):
			for c3 in range(10):
				yield (c1, c2, c3)

# Prevent us from using break every for loop
for (c1, c2, c3) in combo_gen():
	print(c1, c2, c3)
	if (c1, c2, c3) == password:
		print('Found the pass: ', (c1, c2, c3))
		break