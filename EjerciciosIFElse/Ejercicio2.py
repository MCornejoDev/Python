#Escriba un programa que pida dos números y que conteste cuál es el menor y cuál el mayor o que escriba que son iguales.

print("COMPARADOR DE NÚMEROS")
n1 = float(input("Escriba un número: "))
n2 = float(input("Escriba otro número: "))

if(n1 == n2):
    print("Los dos números son iguales")
else:
    if (n1 > n2):
        print(f"Menor: {n2}; Mayor: {n1}")
    else:
        print(f"Menor: {n1}; Mayor: {n2}")