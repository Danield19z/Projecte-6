edat1 = int(input("Introdueix l'edat de la primera persona: "))
edat2 = int(input("Introdueix l'edat de la segona persona: "))
print("Primera persona:", edat1, "anys")
print("Segona persona:", edat2, "anys")
if edat1 > edat2:
    print("La primera persona és més gran.")
elif edat2 > edat1:
    print("La segona persona és més gran.")
else:
    print("Tenen la mateixa edat.")
