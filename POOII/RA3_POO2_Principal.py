#Programa fet per Daniel Torres
#Data: 23/01/2026
#Versio: 2.1
#Importo les classes creades en els altres fitxers i creo objectes per a cadascuna d'elles.

from Alumne import Alumne

a = Alumne(18)
print(a.get_edat())  

b = Alumne(-8)
print(b.get_edat())

from CompteBancari import CompteBancari

Compte = CompteBancari(1000)
Ingre = CompteBancari(500)
print(Compte.consulta_saldo())
print(Ingre.veure_quantitat())

from Contrasenya_segura import Usuari

usuari = Usuari("Contrasenya123")
print(usuari.verificar_contrasenya("Contrasenya123"))  
print(usuari.verificar_contrasenya("Altre4s"))          
success, missatge = usuari.canviar_contrasenya("NovaP")
print(success, missatge)  
success, missatge = usuari.canviar_contrasenya("Gola52sf")
print(success, missatge)  


from Gestor_de_puntuació import Joc

j = Joc()
print(j.get_puntuacio())  
j.sumar_punts(10)
j.sumar_punts(5)
print(j.get_puntuacio())  
j.reiniciar()
print(j.get_puntuacio())  

from Producte import Producte

p = Producte("Televisor", 500)
print(p.nom)             
print(p.obtenir_preu())  

p.modificar_preu(600)
print(p.obtenir_preu())  

p.modificar_preu(-50)    
print(p.obtenir_preu())  

from Sensor import Sensor

sensor1 = Sensor()
print(sensor1.llegir_valor())  
sensor1.modificar_valor(12)
print(sensor1.llegir_valor())  
sensor1.modificar_valor(120)   
print(sensor1.llegir_valor())  
sensor1.modificar_valor(-10)   
print(sensor1.llegir_valor())

from Temps_en_hores import Rellotge 

r = Rellotge(7)
print(r.mostrar())    
r.set_hores(21)
print(r.mostrar())    

from Termòstat import Termostat

t = Termostat()
print(t.temperatura)  
t.temperatura = 25
print(t.temperatura)  
t.temperatura = 5     
print(t.temperatura)  

from Estudiant_amb_nota import Estudiant

estudiant1 = Estudiant(8.5)
print(estudiant1.veure_nota()) 

estudiant1.modificar_nota(9.2)
print(estudiant1.veure_nota())  

estudiant1.modificar_nota(11)   
print(estudiant1.veure_nota())  

estudiant1.modificar_nota(-1)   
print(estudiant1.veure_nota())  

from Email_usuari import CompteUsuari

usuari1 = CompteUsuari("prova@domini.com")
print(usuari1.get_email())  

usuari1.set_email("invalide")  
print(usuari1.get_email())  

usuari1.set_email("nou@email.com")
print(usuari1.get_email())  

