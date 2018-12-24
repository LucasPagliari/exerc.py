nome        = input("Digite seu Nome Completo: ")
# split separa as palavras num array
array       = nome.split()
tamanho     = 0
checa_nome  = -1

for i in array:
    tamanho += len(i)

print("""
    Nome em minúsculo: {}
    Nome em MAIÚSCULO: {}
    Quantidade de Caracteres: {}
    Quantidade de Espaços: {}
    """.format(nome.lower(),nome.upper(),tamanho,len(nome)-tamanho))

checa_nome  =   nome.lower().find("lucas")
if checa_nome > -1 :
    print("Possui: Lucas")
else:
    print("Não Possui: Lucas")