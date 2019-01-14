print('Palindromos')
rng = int(input('Até: '))

for num in range(0,rng):
    num = str(num)
    
    if num == num[::-1]:
        print(num)       

    
