# Demanar el nombre de minuts
minuts_totals = int(input("Introdueix el nombre de minuts: "))

# Calcular hores i minuts restants
hores = minuts_totals // 60
minuts = minuts_totals % 60

# Mostrar el resultat
print(f"{minuts_totals} minuts són {hores} hores i {minuts} minuts.")
