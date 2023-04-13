#Se requiere de un algoritmo que permita al gerente de una empresa ingresar el sueldo que posee actualmente un empleado. En caso de que este sea menor a 50.000 se le deberá aumentar un 15% e informar el monto final que obtendrá. En caso de que sea superior a 50.000 se le deberá aumentar un 10% e informar el monto final que obtendrá. Cuando el gerente termine de ingresar los sueldos y calcular los aumentos, informará el dinero total que la empresa deberá destinar a dichos aumentos y el monto total que deberán depositar en concepto de sueldos. 

sueldoMEnor50 = 0
sueldoMAyor50 = 0
totalAumentos = 0
porcentaje15 =()
porcentaje10 = ()
totalSueldos = ()
sueldoFinal = ()
sueldo=int(input("ingrese el sueldo del empleado o ingrese 0 para salir del sistema "))
while sueldo !=0:  
  if sueldo < 50000:
    sueldoMEnor50 = sueldoMEnor50 + sueldo
    porcentaje15= sueldo * 1.5
    totalAumentos = totalAumentos + (sueldo * 0.15)
  else:
    sueldoMAyor50 = sueldoMAyor50 + sueldo
    porcentaje10 = sueldo * 1.5
    totalAumentos = totalAumentos + (sueldo * 0.15)
  sueldo=int(input("ingrese el sueldo del empleado o ingrese 0 para salir del sistema "))  
if sueldo == 0:
  totalSueldos= sueldoMEnor50 + sueldoMAyor50
  sueldoFinal = totalSueldos + totalAumentos
  print("el monto final de los aumentos es de : ",str(totalAumentos))
  print(" el monto final de los sueldos sin aumentos es de: ", str(totalSueldos))
  print("el monto de sueldos final con aumentos a pagar es de: ", str(sueldoFinal))