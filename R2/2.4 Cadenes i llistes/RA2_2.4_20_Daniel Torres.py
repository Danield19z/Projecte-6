#Programa fet per Daniel Torres
#Data: 22/10/2023
#Versio: 2.1
#Demana una llista de paraules i crea una nova llista amb només les paraules que comencen per vocal
paraules = input("Introdueix paraules separades per espais: ").split()
vocals = "aeiouAEIOU"
nova_llista = []
for i in paraules:
    if i[0] in vocals:
        nova_llista += [i]
print(nova_llista)
