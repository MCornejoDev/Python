#Escriba un programa que pida una temperatura en grados Fahrenheit y que escriba esa temperatura en grados Celsius.
#Se recuerda que la relación entre grados Celsius (C) y grados Fahrenheit (F) es la siguiente: C = (F - 32) / 1,8
#451.0 ºF son 232.8 ºC
print("CONVERTIDOR DE GRADOS FAHRENHEIT A GRADOS CELSIUS")
gFahrenheit = float(input("Escriba una temperatura en grados Fahrenheit: "))

resultadoC = round( ((gFahrenheit - 32) / 1.8),1 )
print(f"{gFahrenheit} ºF son {resultadoC} ºC")