import sys
sys.path.append('../../poo/heranca/')

from pessoa import Pessoa 

if __name__ == "__main__":
	p = Pessoa("Warley Kennedy", "Rocilda Diogenes", "99788-1751")
	p.imprimir()