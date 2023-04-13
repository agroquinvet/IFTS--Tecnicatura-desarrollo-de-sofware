#.- Se requiere de un algoritmo que lea la serie de números positivos hasta que el usuario ingrese un CERO. Cuando el usuario ingrese el valor determinado para parar con el ingreso de valores, informará: la sumatoria de los valores ingresados, la cantidad de números leídos, el mayor valor ingresado y el menor. 

men = 0
may = 0
total = 0
cantidad = 0
numeroReal = int(input("ingrese un numero real o ingrese 0 si desea salir del sistema: "))
while numeroReal != 0:
    if numeroReal < 0:
        print("usted ingreso un numero invalido intentelo nuevamente")
        numeroReal = int(input("ingrese un numero real o ingrese 0 si desea salir del sistema: "))
    else: 
      if cantidad == 0:
        total = total + numeroReal
        men = numeroReal
        may = numeroReal
        cantidad = cantidad + 1
      else: 
        total = total + numeroReal
        cantidad = cantidad + 1
        if may < numeroReal:
         may = numeroReal
        if numeroReal < men:
          men = numeroReal
    numeroReal = int(input("ingrese un numero real o ingrese 0 si desea salir del sistema: "))
if numeroReal == 0:
   print("el numero mayor ingresado es : ", str(may))
   print("el numero menor ingresado es : ", str(men))
   print("la cantidad total de numeros ingresados es : ", str(cantidad))
   print("la sumatoria de los numeros ingresados es : ", str(total))