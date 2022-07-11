# La función input() nos permite asignar a una variable un valor ingresado por el usuario
a = input("Introduce el primer número: ")
b = input("Introduce el segundo número: ")

if a == b:
    #Son iguales
	print('Los números', a, 'y', b, 'son iguales')
elif a < b:
    #A es menor
    print('El número', a, 'es menor que', b)
else:
	#A es mayor
    print('El número', a , 'es mayor que', b)

# Final del programa
print("Fin del programa")