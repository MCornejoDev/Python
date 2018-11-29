#Escriba un programa que pregunte primero si se quiere calcular el área de un triángulo o la de un círculo. 
# Si se contesta que se quiere calcular el área de un triángulo, el programa tiene que pedir entonces la base y 
# la altura y escribir el área. Si se contesta que se quiere calcular el área de un círculo, 
# el programa tiene que pedir entonces el radio y escribir el área.
#Se recuerda que el área de un triángulo es base por altura dividido por 2 y 
#que el área de un círculo es Pi (aproximadamente 3,141592) por el radio al cuadrado.
import math

print("CÁLCULO DE ÁREAS")
print("Elija una figura geométrica:")
print("a) Triángulo ---- b) Círculo")

figura = input("¿Qué figura quiere calcular (Escriba T o C)? ")

while figura != 'T' or figura != 'C':
    print("Opción incorrecta")
    figura = input(" Escriba T o C ")
    if(figura == 'T' or figura == 'C'):
        break
        
if(figura == "T"):
    baseT = float(input("Escriba la base: ")); alturaT = float(input("Escriba la altura: "))
    print(f"Un triángulo de base {baseT} y altura {alturaT} tiene un área de {(baseT * alturaT)/2}")
else:
    if(figura == "C"):
        radioC = float(input("Escriba el radio: "))
        print(f"Un círculo de radio {radioC} tiene un área de {math.pi * (radioC**2)}")  
