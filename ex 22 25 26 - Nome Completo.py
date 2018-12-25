nome        = input("Digite seu Nome Completo: ")
# split separa as palavras num array
array       = nome.split()
tamanho     = 0
checa_nome  = -1
nome_proc   = "lucas"
letra_proc  = "a"

# EX 22
for i in array:
    tamanho += len(i)

print("""
    Nome em minúsculo: {}
    Nome em MAIÚSCULO: {}
    Quantidade de Caracteres: {}
    Quantidade de Espaços: {}
    """.format(nome.lower(),nome.upper(),tamanho,len(nome)-tamanho))

# EX 25
checa_nome  =   nome.lower().find(nome_proc)
if checa_nome > -1 :
    print("Possui: "+ nome_proc)
else:
    print("Não Possui: " + nome_proc)
    
# EX 26
print("Letra Procurada" + letra_proc)
print("Primeira posição= {}".format(nome.lower().find(letra_proc)))
print("Última posição  = {}".format(nome.lower().rfind(letra_proc)))
print("Quantas vezes   = {}".format(nome.lower().count(letra_proc)))