#Programa fet per Daniel Torres
#Data: 02/10/2023
#Versio: 2.1
#Calcula la suma dels primers 100 nombres enters positius (de 1 a 100)
suma = 0 #Variable per acumular la suma
for i in range(1, 101): #variable i que recorre els nombres de l'1 al 100
    suma += i #Variable suma que acumula la suma dels nombres
print("La suma dels primers 100 nombres enters positius és:", suma) #Mostra el resultat per pantalla