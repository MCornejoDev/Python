#Escriba un programa que pida los coeficientes de una 
# ecuación de segundo grado (a x² + b x + c = 0) y escriba la solución.

#Se recuerda que una ecuación de segundo grado puede no tener solución, 
# tener una solución única, tener dos soluciones o que todos los números sean solución. 
# Se recuerda que la fórmula de las soluciones cuando hay dos soluciones es x = (-b ± √(b2-4ac) ) / (2a)

print("ECUACIÓN A X² + B X + C = 0")

a = float(input("Escriba el valor del coeficiente a: "))
b = float(input("Escriba el valor del coeficiente b: "))
c = float(input("Escriba el valor del coeficiente c: "))

if(a != 0):
    if(b > 0 or b < 0 and c > 0 or c < 0):
        print("La ecuación es completa ")
    else:
        if(b == 0):
            print("La ecuación es incompleta ax^2+c = 0")
        else:
            if(c == 0):
                print("La ecuación es incompleta ax^2+bx = 0 -> x(ax+b) = 0")
else:
    print("Solución muy compleja")
