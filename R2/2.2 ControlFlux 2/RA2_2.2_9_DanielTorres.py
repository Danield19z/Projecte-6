#Programa fet per Daniel Torres
#Data: 02/10/2023
#Versio: 2.1
#Trobar el número màxim d’una llista
for i in range(5):
    num = int(input("Introdueix un número: "))
    if i == 0:
        max_num = num
    else:
        if num > max_num:
            max_num = num
print("El número màxim és:", max_num)