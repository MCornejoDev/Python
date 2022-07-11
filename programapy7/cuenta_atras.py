# Realiza una cuenta atrás desde 20 a 0 mostrando únicamente los números pares:
# 20  18  16...  ...4  2  0. Emplea una estructura de repetición for,
# y usa un rango teniendo esto presente:
# el primer valor del rango habrá de ser 20
# el último valor será el adecuado para que la cuenta atrás muestre hasta el 0, incluido.
# el incremento o salto será el adecuado para que cuenta hacia atrás
# mostrando sólo números pares.
# Ejecuta y revisa el programa hasta que no tenga errores,
# y adjúntalo como segundo archivo de esta tarea.
print("Número pares desde el número 20 hasta el 0")
lista = list(range(20, -2, -2))
for n in lista:
    print(n)
