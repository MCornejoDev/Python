#Saludo incial
print("Hola, mundo\n")

#Asignación de valores a variables (no es necesario definirlas previamente ni indicar su tipo de datos)
nombre="Maria"             #asigna tu nombre a la variable
edad= 19                      #asigna tu edad
mayor_edad = edad >=18        #cuando se evalúa la expresión edad>=18 se obtiene un valor lógico verdadero o falso
altura = 1.74                 #escribe tu altura en metros con dos decimales separados por un punto '.'

#Mostramos por pantalla información y datos
print("Te saluda", nombre, "a sus", edad, "años...")
print( "...con una altura de " , altura)
print("Y entre tú y yo, si me preguntas si soy mayor de edad, la respuesta es", mayor_edad)

#Interactuamos con el usuario pidiéndole su nombre
usuario = input("Por cierto, ¿Cómo te llamas?")
print("Bonito nombre", usuario)

#Comprobamos cuál es el tipo de datos de cada una de las variables que hemos utilizado
print ("El tipo de datos de la variable nombre es una cadena de texto: ", type(nombre) )
print ("El tipo de la variable edad es un entero:", type(edad) )
print ("El tipo de altura es un real:", type(altura) )
print ("Y el tipo de la variable mayor_edad es lógico: ", type(mayor_edad) )

print("Ten paciencia conmigo, que estoy aprendiendo. ¡Chao!")
  
