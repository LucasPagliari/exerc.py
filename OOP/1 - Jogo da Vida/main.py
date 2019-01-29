from pessoas import *
from time import sleep

opc = 1
menu ='''
[1] - Criar outro alguém
[2] - Quem sou eu?
[3] - Tomar Drinks
[4] - Envelhecer
[5] - Casar
[6] - Sair (x)
'''

while opc != 6:

    if opc == 1:
        # Usuário entra com os dados
        nome    =       input('Nome: ')
        idade   =   int(input('Idade: ')) 
        job     =       input('Job: ')
        cidade  =       input('Cidade: ')
                
        # Criando um Objeto 
        p1 = Pessoa(nome, idade, job, cidade)
        x = True

    elif opc == 2:
        p1.quemSouEu()

    elif opc == 3:
        p1.tomarDrinks()

    elif opc == 4:
        anos = int(input('Quantos anos quer envelhecer: '))
        p1.envelhecer(anos)
        
    elif opc == 5:
        p1.casar()
    
    sleep(1)
    print(menu)
    # Usuário insere escolha do menu
    opc = int(input('Escolha algo para fazer: '))    
    print('\n')

    pass