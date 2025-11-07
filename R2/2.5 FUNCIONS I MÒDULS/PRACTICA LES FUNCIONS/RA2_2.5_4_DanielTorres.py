#Programa fet per Daniel Torres
#Data: 07/11/2025
#Versio: 2.1
#Comprova si diferents nombres són parells
numeros = [1, 2, 3, 4, 5, 6]

def es_parell(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

for numero in numeros:
    print("El número", numero, "és parell:", es_parell(numero))
