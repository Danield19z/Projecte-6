#Programa fet per Daniel Torres
#Data: 13/01/2026
#Versio: 2.1
# Crea una classe Cotxe amb els atributs marca, model i any
class Cotxe:
    def __init__(self, marca, model, any):
        self.marca = marca
        self.model = model
        self.any = any

    def mostrar(self):
        print(self.marca, self.model, self.any)

