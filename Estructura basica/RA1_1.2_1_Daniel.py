#Progama fer per Daniel Torres
#data 23/09/2025
#version 1.0
import math #Entrada d'uaris

PI = 3.1416 #Constant

def calcular_area(radi): #Funcio per calcular l'area del cercle
    return PI * (radi ** 2)

radi = float(input("Introdueix el radi del cercle: ")) #Demana a l'usuari el radi del cercle
area = calcular_area(radi)
print("L'area del cercle es:", area) #Surtida per pantalla