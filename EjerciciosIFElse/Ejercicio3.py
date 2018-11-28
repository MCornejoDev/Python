#Escriba un programa que pida el año actual y un año cualquiera y 
# que escriba cuántos años han pasado desde ese año o cuántos años faltan para llegar a ese año.

print("COMPARADOR DE AÑOS")
anno1 = int(input("¿En qué año estamos?: ")); anno2 = int(input("Escriba un año cualquiera: "))

if(anno1 == anno2):
    print("¡Son el mismo año!")
else:
    if(anno1 > anno2):
        annosPasados = anno1 - anno2
        if(annosPasados == 1):
            print(f"Desde el año {anno2} han pasado {annosPasados} año")    
        else:
            print(f"Desde el año {anno2} han pasado {annosPasados} años")
    else:
        annosRestantes = anno2 - anno1
        if(annosRestantes == 1):
            print(f"Para llegar al año {anno2} faltan {annosRestantes} año.")    
        else:
            print(f"Para llegar al año {anno2} faltan {annosRestantes} años.")