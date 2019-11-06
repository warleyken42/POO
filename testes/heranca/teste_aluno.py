import sys
sys.path.append('../../poo/heranca/')

from aluno import Aluno

if __name__ == "__main__":
	a = Aluno("Warley Kennedy", "Rocilda Diogenes", "(88)99788-1751")
	#a.add_disciplina("Poo", "Estrutura de Dados", "GTI")
	a.add_disciplina()
	a.imprimir()