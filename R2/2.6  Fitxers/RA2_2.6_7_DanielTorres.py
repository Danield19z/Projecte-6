#Programa fet per Daniel Torres
#Data: 14/11/2025
#Versio: 2.1
#Un programa que intenti escriure en un fitxer anomenat resultats.txt
try:
    fitxer = open("resultats.txt", "w")
    fitxer.write("Aquest és un text de prova\n")
    fitxer.close()
    print("S'ha escrit correctament al fitxer.")
except PermissionError:
    print("Error: no tens permisos per escriure a resultats.txt.")
