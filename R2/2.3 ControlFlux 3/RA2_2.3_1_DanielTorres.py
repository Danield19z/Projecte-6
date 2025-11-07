#Programa fet per Daniel Torres
#Data: 17/10/2025
#Versio: 2.1
#Programa que generi una seqüència de nombres des de 0 fins a un nombre introduït per l'usuari.
try:
    num = int(input("Introdueix un nombre:"))
    for i in range(num + 1):
        print(i)
except ValueError:
    print("Si us plau, introdueix un nombre enter vàlid.")