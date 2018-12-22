n1 = int(input('\033[1;30mDigite um numero: '))
n2 = int(input('\033[1;30mDigite um numero: '))

resp = ''
while resp != 5 :
    resp = int(input('''\033[1;30mEscolha uma das opções abaixo:\033[m 
    
            \033[1;30m[1] Somar
            [2] Multiplicar
            [3] Maior Valor
            [4] Entrar com novos valores
            [5] Sair do programa\033[m
            '''))

    if resp > 5 :
        print('\033[1;30mOpção Invalida, Digite Novamente\033[m')

    if resp == 1:
        soma = n1 + n2
        print('\033[1;30mA soma entre {} e {} é de {}\033[m '.format(n1,n2,soma))

    elif resp == 2:
        mult = n1 * n2
        print('\033[1;30mA multiplicação entre {} e {} é de {}\033[m '.format(n1, n2, mult))

    elif resp == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('\033[1;30mEntre {} e {} o maior é {}\033[m '.format(n1,n2,maior))

    elif resp == 4:
        n1 = int(input('\033[1;30mDigite outro valor:\033[m '))
        n2 = int(input('\033[1;30mDigite outro valor:\033[m '))


    resp2 = input('\033[1;30mDeseja continuar ? [S/N]:\033[m ').upper()

    if resp2 == 'N':
        break