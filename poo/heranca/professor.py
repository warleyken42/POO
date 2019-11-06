from pessoa import Pessoa

class Professor(Pessoa):
	__ministrando: bool
	__siape: str

	def __init__(self, nome, endereco, telefone, siape):
		super(Professor, self).__init__(nome, endereco, telefone)
		self.__ministrando = False
		self.__siape = siape

	def get_siape(self):
		return self.__siape

	def set_siape(self, siape):
		self.__siape = siape

	def is_ministrando():
		return self.__ministrando

	def ministrar(self):
		self.__ministrando = True