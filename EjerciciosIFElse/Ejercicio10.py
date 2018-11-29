#Escriba un programa que pida una distancia en centímetros y que escriba esa distancia en kilómetros, 
# metros y centímetros (escribiendo solamente las unidades necesarias).

#Estos son algunos ejemplos de posibles respuestas:

# Distancia en cm	Distancia en km, m y cm
# 100 cm	                    1 m
# 240 005 cm            2 km, 400 m, 5 cm
# 67 cm                             67 cm
# 300 004 cm            3 km,        4 cm
# La dificultad del ejercicio se puede reducir o aumentar según la forma de presentar el resultado:

#sin separador entre unidades: 2 km 400 m 5 cm
#separando con comas las unidades: 2 km, 400 m, 5 cm
#separando con comas y con la conjunción 'y' en la última unidad: 2 km, 400 m y 5 cm

print(" CONVERTIDOR DE CM A KM, M Y CM ")

distaciaCmUsuario = int(input("Escriba una distancia en centímetros: "))

distanciaKm = distaciaCmUsuario // 100000
distanciaM = distaciaCmUsuario % 100000 // 100
distanciaCm = distaciaCmUsuario % 100

print(f"{distaciaCmUsuario} centímetros son {distanciaKm} Km, {distanciaM} m y {distanciaCm} cm")

#43210 centímetros son 432 m, 10 cm.