#Programa fet per Daniel Torres
#Data: 02/10/2023
#Versio: 2.1
#Trobar el número màxim d’una llista
for i in range(5): #Funciona per a 5 números
    num = int(input("Introdueix un número: ")) #Variable per a guardar el número
    if i == 0: #Funcio per a que el primer número sigui el màxim
        max_num = num #Variable per a guardar el número màxim
    else: #Funcio per a comparar els números
        if num > max_num: 
            max_num = num
print("El número màxim és:", max_num) #Mostra el número màxim