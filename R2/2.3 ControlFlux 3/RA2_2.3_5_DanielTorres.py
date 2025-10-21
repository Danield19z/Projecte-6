#Programa fet per Daniel Torres
#Data: 17/10/2023
#Versio: 2.1
#Demana a l'usuari un nombre enter i imprimeix tots els nombres primers des de 2 fins a aquest nombre
try:
    num = int(input("Introdueix un nombre enter: "))
    for i in range(2, num + 1):
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                break
        else:
            print(i)
except ValueError:
    print("Has d'introduir un nombre enter vàlid.")
