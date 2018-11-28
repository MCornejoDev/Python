#Escriba un programa que pida una cantidad y que escriba cuántas gruesas, docenas y unidades son.

#Se recuerda que una gruesa son doce docenas.

print("CONVERTIDOR A GRUESAS Y DOCENAS")
unidades = int(input("Escriba una cantidad (entera): "))

gruesas = unidades // 144
docenas = unidades % 144 // 12
resto = unidades % 12

print(f"{unidades} unidades son {gruesas} gruesas, "
      f"{docenas} docenas y {resto} unidades")