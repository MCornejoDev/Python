#Escriba un programa que pida una temperatura en grados Celsius y que escriba esa temperatura en grados Fahrenheit.
#Se recuerda que la relación entre grados Celsius (C) y grados Fahrenheit (F) es la siguiente: F = 1,8 * C + 32
#35.0 ºC son 95.0 ºF

print("CONVERTIDOR DE GRADOS CELSIUS A GRADOS FAHRENHEIT")
gradosCelsius = float(input("Escriba una temperatura en grados Celsius: "))
resultadoF = round( ((1.8 * gradosCelsius) + 32),1 )

print(f"{gradosCelsius} ºC son {resultadoF} ºF")
