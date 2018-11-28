#Si el apartado 1 le resulta demasiado difícil, 
#resuelva primero los apartados 2 y 3 e intente de nuevo resolver el apartado 1.
#Si resuelve sin problemas el apartado 1, no es necesario que haga los apartados 2 y 3.

#Apartado 1 : 
#Escriba un programa que pida una distancia en pies y pulgadas y que escriba esa distancia en centímetros.
#Se recuerda que un pie son doce pulgadas y una pulgada son 2,54 cm.

pies = float(input("Escriba una cantidad de pies: ")); pulgadas = float(input("Escriba una cantidad de pulgadas: "))

dePulgadas_a_Centimetros = pulgadas*2.54

if pulgadas == 1.0:
    print(f"{pulgadas} pulgada son {dePulgadas_a_Centimetros} cm")
else:
    print(f"{pulgadas} pulgadas son {dePulgadas_a_Centimetros} cm")


dePies_a_Centimetros = pies*2.54*12
if pies == 1.0:
    print(f"{pies} pie son {dePies_a_Centimetros} cm")
else:
    print(f"{pies} pies son {dePies_a_Centimetros} cm")

resultado = dePulgadas_a_Centimetros + dePies_a_Centimetros; print(f"{pies} pies y {pulgadas} pulgadas son {resultado} cm")


