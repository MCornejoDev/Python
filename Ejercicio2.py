#Escriba un programa que pida el peso (en kilogramos) y la altura (en metros) de una persona y 
# que calcule su índice de masa corporal (imc).
# Se recuerda que el imc se calcula con la fórmula imc = peso / altura 2

peso = float(input("Digame su peso en KG : ")); altura = float(input("Digame su altura en metros : "))
resultado = peso/(altura**2); print(resultado)

