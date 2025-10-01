#Programa fet per Daniel Torres
#Data: 02/10/2023
#Versio: 2.1
#Demana a l'usuari un número enter i mostra la seva taula de multiplicar del 1 al 10
num = int(input("Introdueix un número enter: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")