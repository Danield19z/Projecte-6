#Programa fet per Daniel Torres
#Data: 02/10/2023
#Versio: 2.1
#Mostra els primers 10 termes de la seqüència de Fibonacci
num = int(input("Introdueix un número enter positiu: "))

for i in range(2, num):
    if num % i == 0:
        print(num, "no és un nombre primer.")
        break
else:
    if num > 1:
        print(num, "és un nombre primer.")
    else:
        print(num, "no és un nombre primer.")
