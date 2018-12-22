'''
o programa pede o valor da compra de produtos
e calcula o desconto em alguns testes e em outros
ele parcela o valor do produto e calcula o preço de cada parcela,
no ultimo teste ele ainda calcula os juros de 20%
'''

valor_produto = float(input('\033[1;31mDigite o valor a ser pago da compra: '))

print('\033[1;31mTemos algumas opçoes de pagamento, escolha a que estiver mais favoravel !')

print('\033[1;30mOpção [1] : A vista no dinheiro ou no cheque vc ganha 10% de desconto\n'
      '\033[1;30mOpção [2] : A vista no cartão você ganha 5% de desconto\n'
      '\033[1;30mOpção [3] : Em até 2x no cartão o produto sai pelo preço normal\n'
      '\033[1;30mOpção [4] : Em 3x ou mais no cartão o produto tem 20% de juros')
print('\n')

num = int(input('Digite o numero correspondende a opção desejada: '))

if num == 1:
    calc = valor_produto - (valor_produto * 10 / 100)
elif num == 2:
    calc = valor_produto - (valor_produto * 5 / 100)
elif num == 3:
    calc = valor_produto  # o valor do produto esta parcelado em duas parcelas
    parcela = valor_produto / 2
    print('A sua compra será parcelada em 2x saindo com um valor de {}'.format(parcela))
elif num == 4:
    # a compra pode ser parcelada em 3x ou mais será necessario perguntar ao usuario o numero de parcelas
    calc =  valor_produto + (valor_produto * 20 / 100)
    parcela = int(input('Em quantas parcelas você deseja parcelar ? '))
    novo_preço = calc / parcela
    print('Você parcelou em {} vezes logo cada parcela tem o valor de {:.2f}  '.format(parcela,novo_preço))

print('Como você escolheu a opção {} , o produto saira pelo valor de {} '.format(num,calc))

