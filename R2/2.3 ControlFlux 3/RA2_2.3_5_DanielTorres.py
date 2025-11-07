#Programa fet per Daniel Torres
#Data: 17/10/2025
#Versio: 2.1
#Demana a l'usuari un nombre enter i imprimeix tots els nombres primers des de 2 fins a aquest nombre
try:
    num = int(input("Introdueix un nombre enter positiu: "))
    for i in range(2, num+1):
        print(i)
    if num < 2:
        print("El nombre ha de ser major o igual a 2.")
except ValueError:
    print("Si us plau, introdueix un nombre enter vàlid.")
