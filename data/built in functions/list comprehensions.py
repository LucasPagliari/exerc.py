
lst = [x for x in 'python']
print(lst, '\n')

lst = [x**2 for x in range(11) if x % 2 == 0]
print(lst, '\n')

celsius = [0, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
lst = [float((temp * (9 / 5) + 32)) for temp in celsius]
print(lst)
