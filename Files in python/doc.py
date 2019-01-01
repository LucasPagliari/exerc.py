
# r = read; a = append; w = write; x = create
# t = text; b = binary
textA   = open("archive.txt", "a")
strg    = input("Digite seu texto: ")
textA.write(strg)


textB   = open("archive.txt", "r")
print(textB.read()) 