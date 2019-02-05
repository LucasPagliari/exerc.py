import random

board = ['''
>>>>>>>>>>Hangman<<<<<<<<<<
+---+
|   |
    |
    |
    |
    |
=========''', '''
+---+
|   |
O   |
    |
    |
    |
=========''', '''
+---+
|   |
O   |
|   |
    |
    |
=========''', '''
 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

class Hangman():
	
	def __init__(self, word):
		self.word = word
		self.guessed = []
		self.missed = []

	def guess(self, letter):
		if letter in self.word and letter not in self.guessed:
			self.guessed.append(letter)
		elif letter not in self.missed:
			self.missed.append(letter)

	def hide_word(self):
		hidden = ''
		for letter in self.word:
			if letter not in self.guessed:
				hidden += '*'
			else:
				hidden += letter
		return hidden

	def game_board(self):
		return board[len(self.missed)]

	def game_won(self):
		if '*' not in self.hide_word():
			return True
		return False

	def game_over(self):
		if len(self.missed) == 6 and self:
			return True
		return False

	def game_status(self):
		print(self.game_board())
		print(self.hide_word())
		print(self.missed)
		letter = input('\n:Letra::')
		self.guess(letter)

	pass

def randword():
	with open('words.txt','r') as f:
		words = f.read().split('\n')
		return random.choice(words)

def main():
	g1 = Hangman(randword())
	
	while not g1.game_over():
		g1.game_status()

		if g1.game_won():
			print ('\nParabéns! Você venceu!!')
			print (g1.word)
			break
		elif g1.game_over():
			print(board[6])
			print ('\nGame over! Você perdeu.')
			print ('A palavra era ' + g1.word)
		
	print ('\nFoi bom jogar com você!')

if __name__ == '__main__':
	main()
