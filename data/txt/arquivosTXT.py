import os

text = "olha mundo me chamo zobert"
text += " e meu amigo é o marke"

archive = open(os.path.join("zorb.txt"), "w")

for word in text.split():
    archive.write(word + " ")

archive.close()

archive = open("zorb.txt", "r")
content = archive.read()
archive.close()

print(content)

# Outro método
# Executa o método close() automaticamente

with open("zorb.txt","w") as archive:
    text = input("Digite seu texto: ")
    archive.write(text + "\n")

with open("zorb.txt","a") as archive:
    text = input("Digite outro texto: ")
    archive.write(text + "\n")

with open("zorb.txt", "r") as archive:
    content = archive.read()

print(content)
print(len(content))

