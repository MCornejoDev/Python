# CALENTAMIENTO: crea un programa que dada una palabra, dice cuantas letras tiene

# La función input() nos permite asignar a una variable un valor ingresado por el usuario
palabra = input("Introduce una palabra: ")
vocales = "aeiouAEIOUáéíóúÁÉÍÓÚ"  # cadena con todas las vocales
contadorPalabra = 0
contadorVocales = 0

print("Contamos las letras de la palabra: ", palabra, "...")
# Bucle para recorrer una a una las letras de la palabra
for letra in palabra:
    if letra in vocales: 
        contadorVocales+=1
    contadorPalabra+=1

# Final del programa
if(contadorPalabra == 1):
    print("La palabra <", palabra, "> tiene", contadorPalabra, " letra")   
else:
    print("La palabra <", palabra, "> tiene", contadorPalabra, " letras")

if(contadorVocales == 1):
    print("La palabra <", palabra, "> tiene", contadorVocales, " vocal")   
else:
    print("La palabra <", palabra, "> tiene", contadorVocales, " vocales")
