#Fet per Daniel
#10/02/2026
#Crea persones i treballadors que poden saludar i mostrar la seva feina
class Persona:
    def __init__(self, nom, edat):
        self.nom = nom
        self.edat = edat

    def saludar(self):
        print(f"Hola, sóc {self.nom}")


class Treballador(Persona):
    def __init__(self, nom, edat, feina):
        super().__init__(nom, edat)  
        self.feina = feina

    def mostrar_feina(self):
        print(f"Treballo com a {self.feina}")


treballador = Treballador("Anna", 30, "enginyera")
treballador.saludar()       
treballador.mostrar_feina() 