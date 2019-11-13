class AnimalEstimacao():
	__nome: str
	__idade: int

	def __init__(self, nome, idade):
		self.__nome = nome
		self.__idade = idade

	def get_nome(self):
		return self.__nome

	def set_nome(self, nome):
		self.__nome = nome

	def get_idade(self):
		return self.__idade

	def set_idade(self, idade):
		self.__idade = idade

	def imprimir(self):
		print("Nome:".ljust(12), self.__nome)
		print("Idade:".ljust(12), self.get_idade())