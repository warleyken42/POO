from pessoa import Pessoa

class Aluno(Pessoa):
	__disciplinas: list()
	__estudando: bool

	def __init__(self, nome, endereco, telefone):
		super(Aluno, self).__init__(nome, endereco, telefone)
		self.__disciplinas = []
		self.__estudando = False

	def get__disciplinas(self):
		return self.__disciplinas

	def add_disciplina(self, *disciplinas):

		for disciplina in disciplinas:
			self.__disciplinas.append(disciplina)

	def is_estudando(self):
		return self.__estudando

	def estudar(self):
		self.__estudando = True

	def imprimir(self):
		super(Aluno, self).imprimir()
		print("Estudando:".ljust(12), "Sim" if self.is_estudando() else "Não")
		print("Disciplinas:".ljust(12), len(self.__disciplinas))

		for i in self.__disciplinas:
			print('', i)