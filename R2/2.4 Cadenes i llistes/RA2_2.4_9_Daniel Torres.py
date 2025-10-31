#Programa fet per Daniel Torres
#Data: 22/10/2023
#Versio: 2.1
#Crea un programa que divideixi una frase en paraules i les mostri una per una.
cadena = input("Introdueix una frase: ")
paraules = cadena.split()
print("Les paraules de la frase són:")
for paraula in paraules:
    print(paraula)