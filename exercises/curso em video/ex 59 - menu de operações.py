menu = """
	[ 1 ] Somar
	[ 2 ] Multiplicar
	[ 3 ] Maior
	[ 4 ] Novos Números
	[ 5 ] Sair do Programa
"""
i = 4

while i != 5:
    
    if i == 1:
        print("{} + {} = {}".format(num1, num2, num1 + num2))
    elif i == 2:
        print("{} * {} = {}".format(num1, num2, num1 * num2))
    elif i == 3:
        if num1 > num2:
            print(num1)
        else:
            print(num2)
    elif i == 4:
        num1 = int(input("Digite um número: "))
        num2 = int(input("Digite outro número: "))

    print(menu)
    i = int(input("Selecione sua opção: "))
    print(" ")

print("ByeBye")
