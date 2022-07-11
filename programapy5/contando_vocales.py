# Contando vocales

# La función input() nos permite asignar a una variable un valor ingresado por el usuario
palabra = input("Introduce una palabra: ")

vocales = "aeiouAEIOUáéíóúÁÉÍÓÚ"  # cadena con todas las vocales
contador = 0

print("Contamos las vocales de la palabra: ", palabra, "...")
# Bucle para recorrer una a una las letras de la palabra
for letra in palabra:
    print("\t...revisando", letra)
    if letra in vocales: 
        print("+1 vocal")
        contador+=1

# Final del programa
print("La palabra <", palabra, "> tiene", contador, "vocales")