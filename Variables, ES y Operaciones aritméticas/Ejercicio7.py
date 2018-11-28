#Escriba un programa que pida una cantidad de segundos y que escriba cuántas horas, minutos y segundos son.

print("CONVERTIDOR DE SEGUNDOS A HORAS Y MINUTOS")
segundos = int(input("Escriba una cantidad de segundos: "))

horas = segundos // 3600
minutos = segundos % 3600 // 60
resto = segundos % 60

print(f"{segundos} segundos son {horas} horas, "
      f"{minutos} minutos y {resto} segundos")