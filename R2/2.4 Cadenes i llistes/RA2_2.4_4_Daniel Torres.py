#Programa fet per Daniel Torres
#Data: 22/10/2023
#Versio: 2.1
#Demana una paraula i verifica si és un palíndrom
num = input("Introdueix una paraula: ")
cadena = ""
for i in num:
    cadena = i + cadena
if num == cadena:
    print("La paraula és un palíndrom.")
else:
    print("La paraula no és un palíndrom.")
