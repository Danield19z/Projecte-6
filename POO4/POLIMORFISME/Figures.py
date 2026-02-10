#Fet per Daniel
#10/02/2026
# Crea classes i subclasses de figures i mostra polimorfisme: cada figura dibuixa la seva forma específica
class Figura:
    def dibuixar(self):
        return "Dibuixant una figura genèrica"

class Cercle(Figura):
    def dibuixar(self):
        return "Dibuixant un cercle"

class Quadrat(Figura):
    def dibuixar(self):
        return "Dibuixant un quadrat"

class Triangle(Figura):
    def dibuixar(self):
        return "Dibuixant un triangle"


cercle = Cercle()
quadrat = Quadrat()
triangle = Triangle()
print(cercle.dibuixar())
print(quadrat.dibuixar())
print(triangle.dibuixar())
