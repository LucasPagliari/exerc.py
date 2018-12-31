num = int(input("Digite um número para multiplicar: "))
fim = int(input("Digite até qual número multiplicar: "))

i=1
lista = ["Resultados:"]

# Faz a tabuada do numero inserido
while i < fim+1:
	resultado = num * i
	print ("{} x {} = {}".format(i,num, resultado))
	lista.append(str(resultado))
	i+=1

# Mostra apenas os resultados
for a in lista:
	print(a)

"""
Com apenas For
num = int(input('Digite um numero para multiplicar: '))
i = int(input('Digite até onde multiplicar: '))

for c in range(0,i+1):
    print('{} X {} = {}'.format(num ,c,(num * c)))
"""