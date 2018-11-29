#Escriba un programa que pida tres números y que escriba si son los tres iguales,
#si hay dos iguales o si son los tres distintos.

print("COMPARADOR DE TRES NÚMEROS")
n1 = float(input("Dime un número : ")); n2 = float(input("Dime otro número : ")); n3 = float(input("Dime otro número : "))

if(n1 == n2 and n1 == n3 and n2 == n3): #Los tres números son iguales
    print("Los tres números son iguales")
else:
    if(n1 == n2 != n3 or n1 == n3 != n2 or n2 == n3 != n1): #Hay dos números iguales
        print("Hay dos números iguales")
    else:
        if(n1 != n2 and n1 != n3 and n2 != n3):
            print("Los tres números son distintos")  #Los tres números son distintos