#Escriba un programa que pida una cantidad de segundos y que escriba cuántos minutos y segundos son.
#1234 segundos son 20 minutos y 34 segundos
#120 segundos son 2 min y 0 segundos

print("CONVERTIDOR DE SEGUNDOS A MINUTOS")
cSegundos = int(input("Escriba una cantidad de segundos: "))

minutos = cSegundos // 60
resto = cSegundos % 60

print(f"{cSegundos} segundos son {minutos} min y {resto} seg")