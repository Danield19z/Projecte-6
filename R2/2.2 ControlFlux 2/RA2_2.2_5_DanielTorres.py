#Programa fet per Daniel Torres
#Data: 02/10/2023
#Versio: 2.1
#Demana a l'usuari un número enter positiu i determina si és un nombre primer o no



# Demanem un número a l'usuari
num = int(input("Introdueix un número enter positiu: "))

# Control del cas dels números menors que 2
if num < 2:
    print(num, "no és un nombre primer.")
else:
    primer = True  # Suposem que és primer
    # Recorrem tots els nombres entre 2 i num-1
    for i in range(2, num):
        if num % i == 0:  # Si trobem algun divisor
            primer = False
            break  # Parem el bucle, ja sabem que no és primer
    # Imprimim el resultat
    if primer:
        print(num, "és un nombre primer.")
    else:
        print(num, "no és un nombre primer.")
