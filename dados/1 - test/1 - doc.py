
# r = read; a = append; w = write; x = create
# t = text; b = binary
textA   = open("archive.txt", "w")
strg    = input("Digite seu texto: ")
textA.write(strg)
textA.close()

textA   = open("archive.txt", "r")
print(textA.read()) 