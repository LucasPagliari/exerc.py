from random import randint
from time import  sleep
print('-=-'*30)
print('                 \033[1;30 Vamos jogar Jo ken po ? \033[m')
print('-=-'*30)

print('Eu vou escolher pedra,papel ou tesoura, faça a sua escolha ! ')


itens = ('pedra','papel','tesoura')
computador = randint(0 , 2)
print('\n')
print('''Suas Opçoes
[0] Pedra
[1] Papel
[2] Tesoura''')
print('\n')
jogador = int(input('Escolha uma opção: '))

print('                                Jo')
sleep(1)
print('                                Ken')
sleep(1)
print('                                Po')

if computador == 0:         #o computador escolheu pedra
    if jogador == 0:        #jogador escolheu pedra
        print('Temos um empate')
        print('Eu escolhi Pedra e você escolheu Pedra')

    elif jogador == 1:      #jogador escolheu papel
        print('Você \033[1;32mGanhou\033[m !')
        print('Eu escolhi Pedra e você escolheu Papel ')

    elif jogador == 2:      #jogador escolheu tesoura
        print('Você  \033[1;31mPerdeu\033[m !')
        print('Eu escolhi Pedra e você escolheu Tesoura')

elif computador == 1:       #o computador escolheu papel
    if jogador == 0:        #jogador escolheu pedra
        print('Você  \033[1;31mPerdeu\033[m !')
        print('Eu escolhi Papel e você escolheu Pedra')

    elif jogador == 1:      #jogador escolheu papel
        print('Temos um Empate !')
        print('Eu escolhi Papel e você escolheu Papel')

    elif jogador == 2:      #jogador escolheu tesoura
        print('Você \033[1;32mGanhou\033[m !')
        print('Eu escolhi Papel e você escolheu Tesoura')

elif computador == 2:       #o computador escolheu tesoura
    if jogador == 0:        #jogador escolheu pedra
        print('Você \033[1;32mGanhou\033[m !')
        print('Eu escolhi Tesoura e você escolheu Pedra')

    elif jogador == 1:      #o jogador escolheu papel
        print('Você \033[1;31mPerdeu\033[m !')
        print('Eu escolhi Tesoura e você escolheu Papel')

    elif jogador == 2:      #o jogador escolheu Tesoura
        print('Temos um Empate !')
        print('Eu escolhi Tesoura e você escolheu Tesoura')