import sys
sys.path.append('../../poo/heranca/')

from professor import Professor 

if __name__ == "__main__":
	p = Professor("Warley Kennedy", "Rocilda Diogenes", "99788-1751", "S123")
	p.imprimir()