

archivo = open ("listado-palabras_castellano.txt", "r")

contador=0
for palabra in archivo:
    print(palabra)

print("El archivo tiene", contador, "palabras")
