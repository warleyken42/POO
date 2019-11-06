class Pessoa:
	__nome: str
	__endereco: str
	__telefone: str

	def __init__(self, nome, endereco, telefone):
		self.__nome = nome
		self.__endereco = endereco
		self.__telefone = telefone

	def get_nome(self):
		return self.__nome

	def set_nome(self, nome):
		if len(nome) > 0:
			self.__nome = nome

	def get_endereco(self):
		return self.__endereco

	def set_endereco(self, endereco):
		self.__endereco = endereco

	def get_telefone(self):
		return self.__telefone

	def set_telefone(self, telefone):
		self.__telefone = telefone

	def imprimir(self):
		print("Nome:".ljust(12), self.__nome.upper())
		print("Endereço:".ljust(12), self.__endereco)
		print("Telefone:".ljust(12), self.__telefone)



	
