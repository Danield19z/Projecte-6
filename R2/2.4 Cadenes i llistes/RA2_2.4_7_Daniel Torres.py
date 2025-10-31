#Programa fet per Daniel Torres
#Data: 22/10/2023
#Versio: 2.1
#Demana una cadena i compta quantes vegades apareix una lletra concreta
cadena = input("Introdueix una cadena de text: ")
lletra = input("Introdueix una lletra per comptar les seves aparicions: ")
contador = 0
for i in cadena:
    if i == lletra:
        contador += 1
print("La lletra", lletra, "apareix", contador, "vegades a la cadena.")