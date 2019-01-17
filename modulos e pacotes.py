import urllib.request

resposta = urllib.request.urlopen('http://www.fatecjd.edu.br/portal/')

print (resposta)

html = resposta.read()
i = 0
for x in html:
    if i < 100:
        print(x)
    i+=1    
print(html)
