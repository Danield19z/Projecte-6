#Programa fet per Daniel Torres
#Data: 21/01/2026
#Versio: 2.1
#Crea una classe que se diu producte que despues modifica el seu preu
class Producte:
    def __init__(self, nom, preu):
        self.nom = nom          
        self.__preu = preu      
    
    def obtenir_preu(self):
        return self.__preu

    def modificar_preu(self, nou_preu):
        if nou_preu > 0:
            self.__preu = nou_preu
        else:
            print(f"Avís: el preu {nou_preu} no és vàlid i no s'ha canviat.")


    