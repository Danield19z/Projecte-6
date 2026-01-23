#Programa fet per Daniel Torres
#Data: 21/01/2026
#Versio: 2.1
#Creacio d'una classe Estudiant amb atribut nota i mètodes per veure i modificar la nota.
class Estudiant:
    def __init__(self, nota):
        if 0 <= nota <= 10:
            self._nota = nota
        else:
            self._nota = 0
            print(f"Avís: nota {nota} fora de rang, s'ha assignat 0.")

    def veure_nota(self):
        return self._nota

    def modificar_nota(self, nova_nota):
        if 0 <= nova_nota <= 10:
            self._nota = nova_nota
        else:
            print(f"Avís: nota {nova_nota} fora de rang, no s'ha canviat.")
