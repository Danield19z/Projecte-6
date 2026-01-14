#Programa fet per Daniel Torres
#Data: 13/01/2026
#Versio: 2.1
#Crea una classe anomenada CompteBancari que permet als usuaris ingressar i retirar diners, així com veure el saldo actual.
class CompteBancari:
    def __init__(self, saldo=0):
        self.saldo = saldo

    def depositar(self, quantitat):
        self.saldo += quantitat
        print(f"S'han ingressat {quantitat}€. Nou saldo: {self.saldo}€.")

    def retirar(self, quantitat):
        if quantitat <= self.saldo:
            self.saldo -= quantitat
            print(f"S'han retirat {quantitat}€. Nou saldo: {self.saldo}€.")
        else:
            print("Fons insuficients.")

    def mostrar_saldo(self):
        print(f"Saldo actual: {self.saldo}€.")

