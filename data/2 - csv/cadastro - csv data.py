import csv

user_sign   = int(input('Quantos usuários serão cadastrados: '))
count       = 0
all_data    = []

while count < user_sign:
 
    list_data   = []
    user_name = input('Nome do Usuário: ')
    user_pass = input('Senha do Usuário: ')
    
    while user_pass == user_name:
        print('ERROR: Senha não pode ser igual ao Nome')
        user_pass = input('Digite Outra Senha: ')
    
    list_data.append(user_name)
    list_data.append(user_pass)
    all_data.append(list_data)
    
    count += 1

    pass

with open('usuários.csv','w') as new_file:
    fdnames   = [['nomes','senhas']]
    csv_write = csv.writer(new_file, delimiter=',')

    csv_write.writerows(fdnames)
    csv_write.writerows(all_data)