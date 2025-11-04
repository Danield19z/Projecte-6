#Programa fet per Daniel Torres
#Data: 22/10/2023
#Versio: 2.1
#Escriu una funció que retorni la llista al revés (sense reverse())
llista = input("Introdueix paraules separades per espais: ").split()
nova_llista = []
for i in range(len(llista)-1, -1, -1):
    nova_llista.append(llista[i])
print(nova_llista)

