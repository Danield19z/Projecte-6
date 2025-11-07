#Programa fet per Daniel Torres
#Data: 17/10/2025
#Versio: 2.1
#Demana a l'usuari un nombre enter i imprimeix tots els nombres parells des de 0 fins a aquest nombre
try:
    num=int(input("Introdueix un nombre enter: "))
    if num < 0:
        print("introdueix un nombre enter no negatiu.")
    else:
        print("Nombres parells des de 0 fins a", num, ":")
        for i in range(0, num + 1, 2):
            print(i)
except ValueError:
    print("Si us plau, introdueix un nombre enter vàlid.")