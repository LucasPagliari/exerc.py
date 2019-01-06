# Biblioteca para mexer com arquivos .csv
# csv = Comma-Separated Value = Valores Separados Por Vírgula
import csv

user_sign   = int(input('Quantos usuários serão cadastrados: '))

# variável contador
count       = 0

# Lista para salvar todo dado
all_data    = []
list_data   = []

# Enquanto contador for menor que o número de usuários
# a serem cadastrados, continue no loop
while count < user_sign:

    # Zera a lista
    list_data   = []
    
    # Variáveis que recebem os nomes e senha
    user_name = input('Nome do Usuário: ')
    user_pass = input('Senha do Usuário: ')
    
    # Caso nome e senha forem iguais inicia o loop while
    while user_pass == user_name:
        print('ERROR: Senha não pode ser igual ao Nome')
        user_pass = input('Digite Outra Senha: ')
    
    # Acrecenta a lista o Nome do usuário
    list_data.append(user_name)
    
    # Acrecenta a lista a Senha do usuário 
    list_data.append(user_pass)

    # Representação de como a lista 'list_data' fica:
    # list_data = [user_name, user_pass]

    
    # Adiciona a list_data em outra lista
    all_data.append(list_data)
    
    # Representação de como a lista 'all_data' fica:
    #  all_data = [ [user_name, user_pass] , [user_name, user_pass] ]
    # É uma lista dentro de uma lista
    
    # adiciona um ao contador
    count += 1

    pass

# Conceito/tradução:
# Com o arquivo "usuários.csv" aberto na variável 'new_file'
# no modo "w" (write = escrita) faça:
with open('usuários.csv','w') as new_file:
    # Caso o arquivo não exista o próprio python cria

    # Título das colunas:
    fdnames   = [['nomes','senhas']]
    # Lista dentro de uma lista

    # Crio um objeto chamado csv_write, com o modo de
    # escrever em csv (csv_write)
    csv_write = csv.writer(new_file, delimiter=',')
                            # Qual arquivo ele escreverá: new_file = usuários.csv
                            # delimiter é o que separará os valores, no caso vírgula
                            # mude o delimeter para outros valores para teste e compreensão

    # Escreva na linha os fdnames: Nomes e Senhas
    csv_write.writerows(fdnames)

    # Escreve todos os dados recolhidos no programa acima 
    csv_write.writerows(all_data)

    # Após terminar o with o arquivo é fechado

# Nota: Os dados estão dentro de uma lista que está dentro de outra lista  ex: [[ ]]
# isso porque o módulo csv só escreve corretamente assim, caso deixar apenas em uma lista 
# ele irá separar com vírgulas as letras. Caso queira fazer o teste retire as aspas da parte à seguir:

    # Ele escreverá na última linha uma lista apenas  ex: [] e não uma lista dentro de uma lista [[ ]] 
    # como foi feito anteriormente
    '''
    teste = ['Lucas', '123456']
    csv_write.writerows(teste)
    '''