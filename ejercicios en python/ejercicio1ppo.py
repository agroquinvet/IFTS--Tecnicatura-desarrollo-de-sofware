"""Escribir un programa en Python que pida al usuario que ingrese los tamaños de la base y la altura de un rectángulo y muestre:

1.El perímetro del rectángulo
2.El área del rectángulo"""
Base = int(input("ingrese el tamaño de la base del rectancgulo "))

Altura=int(input("ingrese el alto del rectangulo "))

perimetro= 2*Base + 2*Altura
print("el perimetro es: "+str(perimetro))
Area = Base * Altura
print("el area es: "+str(Area))



