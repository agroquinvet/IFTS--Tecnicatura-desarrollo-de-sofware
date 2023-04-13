#Se requiere de un algoritmo que permita ingresar los registros de un censo hasta que el censista indique que ya ha cargado todos los resultados. Cuando esto ocurra, se deberá informar cantidad de personas censadas, el promedio de edad de ellos y cuantas de estas personas cuentan con internet en sus hogares. 

from xmlrpc.client import boolean


totalInternet= 0
totalPersona=0
sumaEdades=0
personaCensada = input("ingrese el nombre de la persona Censada ")


while personaCensada != "termine":
  edades = int(input("ingrese la edad de la persona: "))  
  internet= boolean(input("ingrese true si posee internet de lo contrario ingrese false: "))
  if internet == True:
    totalInternet = totalInternet + 1
  sumaEdades= sumaEdades + edades
  totalPersona= totalPersona + 1  
  personaCensada = input("ingrese el nombre de la persona Censada o ingrese termine para salir del sistema: ")
if personaCensada == "termine":
  promedioEdades= sumaEdades // totalPersona
  print("el total de personas censadas fue: ", totalPersona)
  print("El promedio de edades de las personas censadas es de: ", promedioEdades)
  print("el total de personas con internet son: ", totalInternet)