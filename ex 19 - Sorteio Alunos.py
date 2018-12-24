from random import randint
from time import  sleep

sort = "Sorteando...."
qnt_alunos = int(input("Digite a Quantidade de Alunos: "))
nome_alunos = []

for i in range(0,qnt_alunos):
    nome_alunos.append(input("Nome do Aluno: ")) 

for i in range(len(sort)-4,len(sort)+1):
    print(sort[0:i])
    sleep(0.4)

print(nome_alunos[randint(0,qnt_alunos)])