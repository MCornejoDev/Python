#Escriba un programa que pida dos números enteros y que escriba si el mayor es múltiplo del menor.

print("COMPARADOR DE MÚLTIPLOS")
n1 = int(input("Escriba un número: ")); n2 = int(input("Escriba otro número: "))

if(n1 >= n2):
    if(n1 % n2 == 0):
        print(f"El {n1} es múltiplo de {n2}")
    else:
        print(f"El {n1} no es múltiplo de {n2}")
else:
    if(n2 % n1 == 0):
        print(f"El {n2} es múltiplo de {n1}")
    else:
        print(f"El {n2} no es múltiplo de {n1}")