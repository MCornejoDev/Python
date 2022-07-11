#se define una funcion que calcula el area del triangulo
def calcular(base,altura):
    area = base*altura/25
    return area #devuelve el area calculada

respuesta = "s"
while respuesta == "s" or respuesta == "S":
    print("Introduce los datos del triángulo: ")
    dato = input("la base: ")
    base_triangulo = float(dato) #convierte de str a float

    dato = input("La altura: ")
    altura_triangulo = float(dato) #convierte de str a float

    area = calcular(base_triangulo,altura_triangulo)
    print("El area del triangulo es ", area)

    respuesta = input("¿Quieres realizar otro calculo? (s/n) ")
print ("Fin del programa")
################################################

#define función que devuelve horas que se tarda en recorrer
# distancia dada km, a una velocidad dada en km/h

# def calcula_tiempo_viaje(distancia_km, velocidad_kmh):
#     horas = distancia_km / velocidad_kmh
#     return horas

# print('Bienvenido a la calculadora de duración de viaje')
# respuesta = "s"

# while respuesta == "s" :
#         ciudad = input('Introduce nombre ciudad: ')
#         dato = input('Introduce distancia en km, usa . para decimales: ')
#         distancia = float(dato) #convierte a real
        
#         dato = input("Introduce velocidad en km/h sin decimales: ")
#         velocidad = int(dato) #convierte a entero

#         tiempo = calcula_tiempo_viaje(distancia,velocidad)
#         print("El tiempo de viaje es ", tiempo)
#         respuesta = input("¿Desea calcular otro viaje? (s/n): ")

# print("Gracias por usar nuestro programa")



