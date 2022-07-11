#programa mayor_edad.py que pide al usuario su edad, y muestra por pantalla si es o no es mayor de edad.

#Interactuando con el usuario pidiéndole su edad
edad = input("¿Qué edad tienes?\n")
mayor_edad = int(edad) >=18 
if mayor_edad:
    print("El usuario es mayor de edad")
else:
    print("El usuario no es mayor de edad")
