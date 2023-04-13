"""Implementar un programa en Python que pida al usuario que ingrese dos números y muestre la suma, resta, división y multiplicación de ambos."""

numero1=int(input("ingrese el primer numero para relaizar las operaciones: "))
numero2=int(input("ingrese el segundo numero para relaizar las operaciones: "))

suma=numero1 + numero2
resta=numero1 - numero2
multi=numero1 * numero2
divi=numero1 / numero2

print("la suma de los numeros ingresados es "+ str(suma))
print("la resta de los numeros ingresados es "+ str(resta))
print("la multiplicacion de los numeros ingresados es "+ str(multi))
print("la divicion de los numeros ingresados es "+ str(divi))