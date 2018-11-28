#Escriba un programa que pida dos números enteros y que calcule su división, escribiendo si la división es exacta o no

print("DIVISOR DE NÚMEROS")
dividendo = int(input("Escriba el dividendo : ")); divisor = int(input("Escriba el divisor : "))
cociente = dividendo // divisor
resto = dividendo % divisor
if(divisor == 0):
    print("No se puede dividir por 0")
else:
    if(dividendo % divisor == 0):
        print("La división es exacta.")
    else:
        print("La división no es exacta. El cociente es {cociente} y el resto es {resto}")