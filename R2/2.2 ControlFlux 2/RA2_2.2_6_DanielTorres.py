#Programa fet per Daniel Torres
#Data: 02/10/2023
#Versio: 2.1
#Mostra els primers 10 termes de la seqüència de Fibonacci
a = 0 #Variable per al primer terme
b = 1 #Variable per al segon terme
comptador = 0 #Variable per comptar els termes
while comptador < 10: #Funció while per repetir el procés 10 vegades
    print(a) #Mostra el valor de a
    a, b = b, a + b #Lo que fa es que a prengui el valor de b i b prengui el valor de a + b
    comptador += 1 #Incrementa el comptador en 1
print("Fi del programa") #Missatge de fi de programa
    