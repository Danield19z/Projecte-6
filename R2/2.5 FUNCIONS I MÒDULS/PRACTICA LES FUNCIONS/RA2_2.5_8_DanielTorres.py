#Programa fet per Daniel Torres
#Data: 07/11/2025
#Versio: 2.1
#Calcula factorials de diversos nombres
def factorial(n):
    resultat = 1
    for i in range(1, n + 1):
        resultat *= i
    print(resultat)
factorial(0)  
factorial(3)
factorial(5)  
