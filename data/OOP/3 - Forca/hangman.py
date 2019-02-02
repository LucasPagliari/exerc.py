import random

class Hangman():
	"""docstring for Rangman"""
	def __init__(self, word):
		self.word = word
		self.guessed = []
		self.missed = []

	def guess(self, letter):
		if letter in self.word and not in self.guessed:
			self.guessed.append(letter)
		elif letter n:
			self.missed.append(letter)

	def hide_word(self):
		hidden = ''
		for letter in self.word:
			if letter not in self.guessed:
				hidden += '*'
			else:
				hidden += letter
		return hidden

	def game_won(self):
		if '*' not in self.hide_word():
			return True
		else:
			return False

	def game_over(self):
		if len(self.missed) == 6 and self