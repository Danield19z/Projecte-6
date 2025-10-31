#Programa fet per Daniel Torres
#Data: 22/10/2023
#Versio: 2.1
#Crea una llista amb 5 nombres i imprimeix el major i el menor.
llista_nombres = (int(input("Introdueix un nombre: ")) for _ in range(5))
print("El nombre major es:", max(llista_nombres))