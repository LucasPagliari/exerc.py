from random import randint

print("Advinhe o número!!!")

i = int(input("Digite até qual valor pode ser selecionado: "))

nrand   = randint(0, i)
nguess  = 0
count   = 0

while nrand != nguess:
    nguess = int(input("Adivinhe o número: "))
    count += 1

    if count == 10:
        print("Chutou demais")
        break

    if nguess < nrand:
        print("O número é maior!!")  

    elif nguess > nrand:
        print("O número é menor!!")
    
    elif nguess == nrand:
        print("Acertou!")