lista = []

for i in range(0,20):
    lista.append(i)

print(lista)
print('\n')

def square(x):
    return (x**2)

# Aplica a função a cada um dos itens
# retorna uma lista de mesmo tamanho
x = list(map(square,lista))
print(x)
print('\n')


x = list(map((lambda x: x**3), lista))

print(x)
print('\n')

a = [1, 2, 3] 
b = [4, 5, 6]
c = [7, 8, 9]

x = list(map(lambda x,y,z: x+y+z, a, b, c))
print(x)
