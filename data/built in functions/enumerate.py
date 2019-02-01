
seq = ['a', 'b', 'c']

# Retorna um iterator, (indice, valor)
for i in enumerate(seq):
    print(i)

for i, v in enumerate(seq):
    print('índice:', i, 'valor:', v)
