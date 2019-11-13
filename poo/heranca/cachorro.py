from animal import Animal

class Cachorro(Animal):
	__raca: str

	def __init__(self, raca, peso):
		super(Cachorro, self).__init__(peso)
		self.__raca = raca
		
	def get_raca(self):
		return self.__raca

	def latir(self):
		print("Au Au")

	def imprimir(self):
		print("Raça:".ljust(12), self.__raca)
		print("Peso:".ljust(12), self.get_peso())
	
	
p = Cachorro("Puldo", 10)