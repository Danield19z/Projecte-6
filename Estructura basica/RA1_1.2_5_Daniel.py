#Progama fer per Daniel Torres
#data 23/09/2025
#version 1.0
PI = 3.14159   # constant per al valor de pi
def calcula_area_cercle(radi): #funció que calcula l'àrea del cercle
    return PI * radi * radi
radi = float(input("Introdueix el radi del cercle: ")) #Entrada del usuari
area = calcula_area_cercle(radi) #Us de la funció per calcular l'àrea
print("L'àrea del cercle és:", area) #Sortida per pantalla de l'àrea del cercle
print("Fi del programa") #Missatge de fi del programa
