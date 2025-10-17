#Programa fet per Daniel Torres
#Data: 17/10/2023
#Versio: 2.1
#Demana a l'usuari un nombre enter i calcula la suma de tots els nombres des de 1 fins a aquest nombre
try:
    num1 = int(input("Introdueix un nombre:"))
    for i in range(1,num1+1):
        print(i)
except ValueError:
    print("Si us plau, introdueix un nombre enter vàlid.")
