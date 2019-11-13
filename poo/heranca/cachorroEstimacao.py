
from animalEstimacao import AnimalEstimacao
from cachorro import Cachorro

class CachorroEstimacao(Cachorro, AnimalEstimacao):

	def __init__(self, nome, idade, raca, peso):
		AnimalEstimacao.__init__(self, nome, idade)
		Cachorro.__init__(self, raca, peso)

	def imprimir(self):
		AnimalEstimacao.imprimir(self)
		Cachorro.imprimir(self)

