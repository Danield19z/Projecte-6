#Fet per Daniel
#10/02/2026
#Crea classes i subclasses d'empleats i mostra polimorfisme: cada empleat calcula el seu sou
class Empleat:
    def calcular_sou(self):
        return 0  

class Fixe(Empleat):
    def calcular_sou(self):
        return 2000  

class Autonom(Empleat):
    def calcular_sou(self):
        return 100 * 15  

def mostrar_sous(llista_empleats):
    for e in llista_empleats:
        print(e.calcular_sou())

empleats = [Fixe(), Autonom()]
mostrar_sous(empleats)




