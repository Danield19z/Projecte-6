#Programa fet per Daniel Torres
#Data: 22/10/2023
#Versio: 2.1
#Demana una paraula i guarda cada lletra en una llista.
llista=[]
paraula=input("Introdueix una paraula: ")
for lletra in paraula:
    llista.append(lletra)
    print("Llista de lletres:", llista)
