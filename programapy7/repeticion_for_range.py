#pedir un número
respuesta = input("Introduce un número : ")
numero = int(respuesta)
#representar por pantalla la tabla de multiplicar del número
for n in range(1,11):
    resultado = numero * n
    print(numero , " x ", n , " = ", resultado)
    resultado = ""
