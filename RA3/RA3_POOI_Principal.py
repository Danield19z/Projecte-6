#Programa fet per Daniel Torres
#Data: 13/01/2026
#Versio: 2.1
#Importo les classes creades en els altres fitxers i creo objectes per a cadascuna d'elles,

from Cotxe import Cotxe
cotxe = Cotxe("Toyota", "Corolla", 2020)
cotxe2 = Cotxe("Honda", "Civic", 2019)
cotxe.mostrar()
cotxe2.mostrar()

from Rectangle import Rectangle 
rectangle = Rectangle(5, 10)
rectangle2 = Rectangle(3, 4)
rectangle3 = Rectangle(6, 8)
rectangle.mostrar()
rectangle2.mostrar()
rectangle3.mostrar()

from Persona import Persona

p1 = Persona("Maria", 30)
p2 = Persona("Joan", 35)
p3 = Persona("Anna", 25)
p4 = Persona("Pere", 40)


from Producte import Producte
producte1 = Producte("Llibre", 15)
producte2 = Producte("Joc de taula", 30)
producte = Producte("Auriculars", 50) 
producte1.aplicar_descompte(10)
producte1.mostrar_informacio()
producte2.aplicar_descompte(10)
producte2.mostrar_informacio()

from Estudiant import Estudiant  
joan = Estudiant("Joan", 7)   
anna = Estudiant("Anna", 3)   
pere = Estudiant("Pere", 6)   
maria = Estudiant("Maria", 4) 

from CompteBancari import CompteBancari
compte = CompteBancari(1000)  
compte.depositar(100)         
compte.retirar(900)  
compte.retirar(500)         
compte.mostrar_saldo()    

from Cercle import Cercle

c1 = Cercle(3)
c2 = Cercle(4)
c3 = Cercle(5)
c4 = Cercle(6)
c5 = Cercle(7)


from Animal import Animal, Gos
animal = Animal("Pepe", "Gat")
animal.mostrar_informacio()
print() 
gos = Gos("Rex", "Pastor Alemany")
gos.mostrar_informacio()

from Llibreta import Llibre
from Llibreta import Biblioteca

llibre1 = Llibre("Don Quixote", "Miguel de Cervantes", 1605)
llibre2 = Llibre("La casa de papeñ", "George Orwell", 1949)
biblioteca = Biblioteca()
biblioteca.afegir_llibre(llibre1)
biblioteca.afegir_llibre(llibre2)
biblioteca.mostrar_tots()


from Punt import Punt  
punt1 = Punt(3, 6)
punt2 = Punt(4, 2)
punt3 = Punt(4, 3)
punt4 = Punt(1, 2)
print("Punt1:", punt1.mostrar())
print("Punt2:", punt2.mostrar())
print("Distància entre punt1 i punt2:", punt1.distancia(punt2))
print("Punt3:", punt3.mostrar())
print("Punt4:", punt4.mostrar())
print("Distància entre punt3 i punt4:", punt3.distancia(punt4))
