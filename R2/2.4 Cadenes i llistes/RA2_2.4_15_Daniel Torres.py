#Programa fet per Daniel Torres
#Data: 22/10/2023
#Versio: 2.1
#Crea una llista amb noms i ordena'ls alfabèticament.
llistat = []
frase = input("Introdueix noms separats per espais: ")
llistat = frase.split()
llistat.sort()
print("Llista ordenada alfabèticament:", llistat)
