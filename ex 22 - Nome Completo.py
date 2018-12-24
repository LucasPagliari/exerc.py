nome    = input("Digite seu Nome Completo: ")
# split separa as pelavras num array
array   = nome.split()
tamanho = 0

for i in array:
    tamanho += len(i)

print("Nome em minúsculo: {}".format(nome.lower()))
print("Nome em MAIÚSCULO: {}".format(nome.upper()))
print("Quantidade de Caracteres: {}".format(tamanho))
print("Quantidade de Espaços: {}".format(len(nome)-tamanho))
