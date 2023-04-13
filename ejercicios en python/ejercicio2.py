#Se requiere de un algoritmo que permita el ingreso de las edades de un grupo de personas. Una vez cargados todos estos valores informar el promedio de sus edades. 

totalEdades = 0
cantidadEdad = 0
Edad = int(input("ingrese una edad o ingrese 0(cero) para salir del sistema: "))
while Edad !=0:
   if Edad < 0:
      print("el numero que ingreso es incorrecto intentenlo nuevamente")
   else:
    totalEdades = totalEdades + Edad
    cantidadEdad = cantidadEdad + 1
    Edad = int(input("ingrese una edad o ingrese 0(cero) para salir del sistema: "))
if Edad == 0:
    promedioEdades= totalEdades // cantidadEdad
    print("el promedio de las edades suministradas es: ", str(promedioEdades))