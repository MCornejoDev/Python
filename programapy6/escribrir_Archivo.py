

archivo1 = open ("listado-palabras_castellano.txt", "r")

archivo2 = open("palabras_A.txt", "w")

for palabra in archivo1:
    if palabra[0] == "a":
        archivo2.write(palabra)


