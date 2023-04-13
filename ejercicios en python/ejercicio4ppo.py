"""Escribe un programa en Python que solicite 5 números enteros al usuario. 
El mismo debe indicar si entre dichos valores hay números duplicados o no, 
imprimiendo por pantalla “HAY DUPLICADOS” o “SON TODOS DISTINTOS”"""
cant=0
list=[]
while cant != 5:
    numero1= int(input("ingrese un numero entero "))
    list.append(numero1)
    cant +=1
if len(list) == len(set(list)):
    print("Todos los numeros son distintos")
else:
    print("hay numeros duplicados")
    

