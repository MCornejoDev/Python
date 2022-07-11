#Escribe un segundo programa invertir.py que pide una palabra al usuario 
#y genera otra palabra idéntica 
#pero con las letras en orden inverso (caballo > ollabac). 
#Después se pregunta al usuario si dese invertir otra palabra,
#y repetirá el proceso, hasta que el usuario indique no.
respuesta = ''
palabra_invertida = ""
while respuesta != 'n':
    palabra_usuario = input("¿Qué palabra vamos a invertir? : \n")
    for letra in palabra_usuario:
        palabra_invertida = letra + palabra_invertida
    print("Su palabra invertida es : ", palabra_invertida)
    respuesta = input("¿Desea invertir otra palabra? (s/n): \n")
    palabra_invertida = ""
print("Gracias por invertir palabras")