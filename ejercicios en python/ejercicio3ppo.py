"""escribe un programa que solicite 5 numeros enteros e imprime el maximo y el minimo de los valores."""

cant=0

while cant !=5:
    numero1= int(input("ingrese un numero entero "))
     
    if cant == 0:        
        maximovalor= numero1
        minimovalor=numero1
    else:
        if numero1 > maximovalor:
            maximovalor= numero1
        elif numero1 < minimovalor:
            minimovalor = numero1
    cant+=1 
    
print("el valor mas alto ingresado es " + str(maximovalor))
print("el valor mas bajo ingresado es " + str(minimovalor))
