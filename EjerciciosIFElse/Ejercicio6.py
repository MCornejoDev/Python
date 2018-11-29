#Escriba un programa que pida un año y que escriba si es bisiesto o no.
# Se recuerda que los años bisiestos son múltiplos de 4, pero los múltiplos de 100 no lo son, 
# aunque los múltiplos de 400 sí.

print("COMPROBADOR DE AÑOS BISIESTOS")
annobisiesto = int(input("Escriba un año y le diré si es bisiesto:"))

if(annobisiesto % 4 == 0):
    if(annobisiesto % 100 != 0 or annobisiesto % 400 == 0):
        print(f"El año {annobisiesto} es un año bisiesto.")
    else:
        print(f"El año {annobisiesto} no es un año bisiesto porque es divisible por 100 y aun acabando en 00 no es divisible por 400")
else:
    print(f"El año {annobisiesto} no es divisible por 4")