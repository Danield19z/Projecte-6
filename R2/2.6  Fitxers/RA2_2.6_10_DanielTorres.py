#Programa fet per Daniel Torres
#Data: 14/11/2025
#Versio: 2.1
#Assegura’t que el fitxer es tanqui sempre, fins i tot si es produeix un error en llegir-lo
fitxer = open("dades.txt", "r") 
try:
    contingut = fitxer.read()
    print("Contingut llegit:")
    print(contingut)
finally:
    fitxer.close()
    print("El fitxer s'ha tancat correctament.")
