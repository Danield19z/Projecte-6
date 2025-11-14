#Programa fet per Daniel Torres
#Data: 14/11/2025
#Versio: 2.1
#un programa que intenti llegir un fitxer anomenat dades.txt
try:
    fitxer = open("dades.txt", "r")  
    contingut = fitxer.read()         
    print(contingut)                  
    fitxer.close()                    
except FileNotFoundError:
    print("Error: el fitxer dades.txt no existeix.")  
