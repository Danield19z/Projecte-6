#Progama fer per Daniel Torres
#data 23/09/2025
#version 1.0
num1 = float(input("Introdueix el primer número: ")) #variable per guardar el primer número
num2 = float(input("Introdueix el segon número: ")) #variable per guardar el segon número

suma = num1 + num2 #variable per guardar la suma dels dos números
resta = num1 - num2 #variable per guardar la resta dels dos números
multiplicacio = num1 * num2 # variable per guardar la multiplicació dels dos números
divisio = num1 / num2 # variable per guardar la divisió dels dos números

# Funció per imprimir el número sense decimals si és enter
def format_numero(n):
    if n.is_integer():  # comprova si el número és enter
        return int(n)
    else:
        return n

print("La suma és:", format_numero(suma)) #Se mostra en pantalla la suma dels dos números
print("La resta és:", format_numero(resta)) #Se mostra en pantalla la resta dels dos números
print("La multiplicació és:", format_numero(multiplicacio)) #Se mostra en pantalla la multiplicació dels dos números
print("La divisió és:", format_numero(divisio)) #Se mostra en pantalla la divisió dels dos números
