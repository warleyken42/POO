class Animal:
	__peso: int

	def __init__(self, peso):
		self.__peso = peso

	def get_peso(self):
		return self.__peso

	def comer(self):
		self.__peso += 3

	def correr(self):
		self.__peso -= 1