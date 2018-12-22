# 60/dia & 0,15/km
v_dia = 60
v_km = 0.15
i = 0
class CarroAluguel:
	def __init__(self, km, dias):
		self.km = km
		self.dia = dias
	
	def valorDia(self):
			valor = self.dia * v_dia
			print("Custo dos Dias: {}".format(valor))
			
	def valorKm(self):
		valor = self.km * v_km
		print("Custo dos Kms: {}".format(valor))
		
	def valorTotal(self):
		valor = self.km * v_km + self.dia * v_dia
		print("Valor Total: {}".format(valor))
	

menu = """
	[ 1 ] Valor dos Dias alugados 
	[ 2 ] Valor dos Kms rodados
	[ 3 ] Total a Pagar
	[ 4 ] Sair (x)
"""
print("Aluguel de Carros!")
dias = int(input("Quantos dias usados: "))
km = int(input("Quantos kms rodados: "))
car = CarroAluguel(km, dias)

while i != 4:
	if i == 1:
		car.valorDia()
	elif i == 2:
		car.valorKm()
	elif i == 3:
		car.valorTotal()
	else:
		print("Digite uma opção válida!!")
	
	print(menu)
	i = int(input())

