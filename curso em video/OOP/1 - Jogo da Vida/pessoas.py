# Orientação a objeto
# Definindo uma classe
class Pessoa:
      
    # Método de Construção
    def  __init__(self, nome, idade, job, cidade):

        # Atributos do Objeto
        self.nome       = nome
        self.idade      = idade
        self.job        = job
        self.cidade     = cidade
        self.solteiro   = True
        self.vivo       = True

     # Exibir informações da pessoa
    def quemSouEu(self):
        
        if self.solteiro:
            word = 'estou'
        
        else:
            word = 'não estou'

        texto   =''' 
        {0} tenho {1} anos, sou um {2}.
        Resido na cidade de {3}.
        Ademais {4} solteiro.'''

        # Insere no texto a cima os parâmetros passado no format
        print(texto.format(self.nome,self.idade,self.job,
        self.cidade,word))

    # Método da classe (Chegar se é maior de idade)
    def tomarDrinks(self):
        
        if self.vivo:
        
            if self.idade < 18:
                print('Menor de Idade')
            
            else:
                print('Ta tudo liberado. E você bebeu')

        else:
            self.obito()

        pass
   
    # Casamento
    def casar(self):
        
        # Se vivo = True
        if self.vivo:
        
            if self.idade <= 16:
                print('Você ta muito novo ainda!!')

            elif self.idade <= 20:
                print('Espera... só pra ter certeza')

            else:
                self.solteiro = True
                print('Pronto você se casou')

        else:
            self.obito()

        pass

    def envelhecer(self,anos):

        if self.idade > 80:
            print('Você morreu #sad')
            self.vivo = False

        elif anos <= 30:
            self.idade += anos
            print('Você tem ' + str(self.idade) + ' anos')

        pass
        

    def obito(self):
        
        self.vivo = False
        ano_atual = self.idade + 2018
        print('''Aqui jaz {}, faleceu com {} anos \n
        {}, Ano {}
        '''.format(self.nome, self.idade, self.cidade, ano_atual))
        
        pass
       

    pass
