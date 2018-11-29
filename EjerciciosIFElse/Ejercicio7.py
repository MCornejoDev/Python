#Escriba un programa que pida los coeficientes de una ecuación de primer grado 
# (a x + b = 0) y escriba la solución.

#Se recuerda que una ecuación de primer grado puede no tener solución, tener una solución única, 
# o que todos los números sean solución. Se recuerda que la fórmula de las soluciones es x = -b / a

print("ECUACIÓN A X + B = 0")

a = float(input("Escriba el valor del coeficiente a: "));  b = float(input("Escriba el valor del coeficiente b: "))

if(a == 0 and b == 0):
    print("Todos los números son solución")
else:
    if(a == 0):
        print("La ecuación no tiene solución")
    else:
        print(f"La ecuación tiene una solución: {- b / a}")