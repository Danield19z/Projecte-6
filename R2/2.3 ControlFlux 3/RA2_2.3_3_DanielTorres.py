#Programa fet per Daniel Torres
#Data: 17/10/2023
#Versio: 2.1
#Un programa que mostri la taula de multiplicar d'un número introduït per l'usuari
try:
    num=int(input("Introdueix un número:"))
    for i in range(1,11):
        print(num,"*",i,"=",num*i)
except ValueError:
    print("Si us plau, introdueix un número vàlid.")