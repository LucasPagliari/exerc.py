# A classe é utilizada apenas quando o objeto é criado ou
# quando os métodos são usados. Com métodos não precisando reescrever
# uma "função" sempre que necessária.
# 
### Atenção ###
#Este código utiliza alguns conceitos de objeto orientado
#O programa foi criado apenas para conhecer os comandos e conceitos

#e está longe de ser um exemplo para os que queiram se aprofundar

#Criando classe
class Produto:
    
    #Todo método tem "()" podendo ter ou não parâmetros
    #Já atributos não tem

    #Método de Construção de um Objeto
    #ela executa quando queremos criar um objeto
    def __init__(self, nome, valor,):
        #Parâmetro "x" e "y" devem ser passados junto ao método

        #Dá ao objeto criado atributos de nome e valor
        self.nome = nome 
        self.valor = valor
        #self: referece ao próprio objeto (no caso p1)

    #Método de Pagamento
    def modoPagamento(self): 
        #Parâmetro self é utilizado pois o método é chamado pelo objeto (p1.modoPagamento)
        modo_pag = 0
        
        #loop para evitar que o usuário coloque outra opção
        while modo_pag < 1  or  modo_pag > 4:
            print (" Forma de pagamento: \n"
            "[ 1 ] - Dinheiro (Desconto de 10%) \n"
            "[ 2 ] - Débito (Desconto de 5%)\n"
            "[ 3 ] - Crédito 2x (sem juros)\n"
            "[ 4 ] - Crédito 3x ou mais (juros 2%/mês)\n")
            print("\n")

            #Usuário escolhe o modo de pagamento de 1 à 4
            modo_pag = int(input("Modo de Pagamento:"))
        
        #Faz com que o método retorne valores (no caso o modo de pagamento)
        return modo_pag

    #Método de Desconto
    def desconto(self, modo_pag): 
        #parâmetro "self" utilizado pois o objeto que executa o método "(p1.desconto)"
        #parâmetro "modo_pag" é o modo de pagamento
        
        #Dinheiro:
        if modo_pag==1:
            desconto = 10
        #Débito
        else:
            desconto = 5 

        #Calcula o desconto
        valor_desconto = self.valor*(desconto)/100

        #Exibe os resultados obtidos
        #.format() insere uma variável nas {}
        print("Desconto: {} ".format(valor_desconto)) 
        #pode-se fazer contas dentro do .format()
        print("Valor Final: {} ".format(self.valor - valor_desconto))

    #Método de Juros
    def juros(self, modo_pag):
        
        #Parcelado mais de 2x
        if modo_pag==4:
            juros = 0.02
            
            #loop para garantir que o usuário digite um n° maior que 2
            meses = 0   
            while meses <= 2:
                meses = int(input("Quantos meses?: "))
                #exibe ao usuário um erro 
                if meses <=2:
                    print("Valor Inválido: Deve ser maior que 2")
        
        #Crédito apenas 2 parcelas
        else:
            juros = 0
            meses = 2
            
        #Calcula o Valor Final com juros
        x = self.valor * (1 + juros) ** meses
        #Calcula as parcelas
        y = (x)/meses

        #exibe os resultados obtidos
        print("Juros: {} ".format(x - self.valor))
        print("Parcela: {} ".format(y))
        print("Valor Final: {}".format(x))           
    
    #Define o final da classe
    pass 

print("Bem vindo, Você comprou um celular!!!")
custo = float(input("Quanto custou?: "))

#Criando um objeto
p1 = Produto("Celular", custo) #executa o: def __init__(self, nome, valor)
    #devemos passar os atributos ao método

#Executa o método, sendo que é retornado um valor de 1 à 4
#que é atribuido à variável modo
modo = p1.modoPagamento()

if modo > 2:
    #maior que 2: "Crédito 2x" ou "Crédito 3x ou mais"
    p1.juros(modo)
else:
    #menor que 2: "À vista" ou "Débito"
    p1.desconto(modo)
