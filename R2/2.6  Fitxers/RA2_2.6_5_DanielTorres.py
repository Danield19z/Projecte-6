#Programa fet per Daniel Torres
#Data: 14/11/2025
#Versio: 2.1
#Mostra el contingut per pantalla i afegeix una línia al final sense esborrar el contingut anterior
fitxer = open("sortida.txt", "r+")
contingut = fitxer.read()
print("Contingut actual del fitxer:")
print(contingut)
fitxer.write("Aquesta és una línia afegida al final\n")
fitxer.close()
