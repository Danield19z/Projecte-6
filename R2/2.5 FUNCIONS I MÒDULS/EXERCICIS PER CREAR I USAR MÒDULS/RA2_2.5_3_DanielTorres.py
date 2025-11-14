#Programa fet per Daniel Torres
#Data: 07/11/2025
#Versio: 2.1
#Mòdul de geometria
import geometria

costat = int(input("Posa una mida: "))
print("Àrea del quadrat:", geometria.area_quadrat(costat))

radi = int(input("Posa una mida: "))
print("Àrea del rado: ", geometria.area_cercle(radi))

base = int(input("Posa la base del rectangle: "))
altura = int(input("Posa l'altura del rectangle: "))
print("Àrea de l'altura i la base", geometria.area_rectangle(base,altura))
