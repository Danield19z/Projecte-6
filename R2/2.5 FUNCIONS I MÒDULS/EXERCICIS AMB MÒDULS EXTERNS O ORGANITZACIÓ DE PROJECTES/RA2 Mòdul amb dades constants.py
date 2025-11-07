#Programa fet per Daniel Torres
#Data: 07/11/2025
#Versio: 2.1
#Fes un mòdul constants.py amb valors com PI, GRAVETAT, etc.
import PI
massa = int(input("Massa (kg): "))
print("Pes:", massa * PI.GRAVETAT, "N")
radi = int(input("Radi: "))
print("Àrea cercle:", PI.PI * radi * radi)
