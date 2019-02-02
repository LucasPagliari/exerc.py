class Employee:
 	
 	raise_amt = 1.04
 	day = 5

 	def __init__(self, first, last, pay):
 		self.first= first
 		self.last= last
 		self.pay = pay

 	def apply_raise(self):
 		self.pay = int(self.pay * self.raise_amt) 

 	@classmethod
 	def set_raise_amount(cls, amount):
 		# cls = class
 		cls.raise_amt = amount

 	# To an object
 	@classmethod
 	def from_string(cls, emp_str):
 		first, last, pay = emp_str.split('-')

 	# Does not take extras parameters like self or cls
 	@staticmethod
 	def is_workday(day):
 		if day == 5 or 6:
 			return False
 		return True
 	pass

# Inheritance - Subclasses
class Developer(Employee):
	
	raise_amt = 1.10

	def __init__(self, first, last, pay, prog_lang):
		super().__init__(first, last, pay)
		# OR Employee.__init__(self...)
		self.prog_lang = prog_lang
	pass

print(help(Developer))

dev = Developer('Cory','Jojo',5000,'Python')

print(dev.pay)
dev.apply_raise()
print(dev.pay)
print(dev.prog_lang)
