#Se requiere de un algoritmo que lea los 250.000 votos de los 3 candidatos a intendente de la ciudad. Luego informar el dato del candidato ganador y los porcentajes de este candidato y los demás. (Ver función Aleatorio) 

from random import randint



candidato1 = 0
candidato2 =0
candidato3 = 0
cantidadDeVotos = int(250000)
votos = randint(1,3)
while cantidadDeVotos != 0:   
  if votos == 1:
    candidato1 = candidato1 + 1
  if votos == 2:
    candidato2 = candidato2 + 1
  if votos == 3:
    candidato3 = candidato3 + 1
  cantidadDeVotos -= 1   
  votos = randint(1,3)
  '''para ver pordonde va el proceso'''
  print(cantidadDeVotos)
if cantidadDeVotos == 0: 
  porcentaje1= (candidato1 * 100)// 250000
  porcentaje2= (candidato2 * 100)// 250000
  porcentaje3= (candidato3 * 100)// 250000
  if candidato1 ==candidato2 and candidato2 == candidato3 and candidato1 == candidato3:
    print("los candidatos 1 y 2 tienen la misma cantidad de votos")
  else:
    if candidato1 ==candidato2 and candidato1 < candidato3:
      print("los candidatos 1 y 2 tienen la misma cantidad de votos")
    else:
      if candidato1==candidato3 and candidato1 > candidato2:
        print("los candidatos 1 y 3 tienen la misma cantidad de votos")
      else:
        if candidato2==candidato3 and candidato2 > candidato1:
          print("los candidatos 2 y 3 tienen la misma cantidad de votos")
        else:
          if candidato1 > candidato2:
            if candidato1 > candidato3:
              print("el candidato numero 1 total de votos: ", str(porcentaje1), "%" )
              print("el candidato numero 2 total de votos: ", str(porcentaje2), "%" )
              print("el candidato numero  total de votos: ", str(porcentaje3), "%" )
              print("el ganador con una cantidad de votos de: ",str(candidato1), " es el candidato numero 1")
            else:
              print("el candidato numero 1 total de votos: ", str(porcentaje1), "%" )
              print("el candidato numero 2 total de votos: ", str(porcentaje2), "%" )
              print("el candidato numero  total de votos: ", str(porcentaje3), "%" )
              print("el ganador con una cantidad de votos de: ",str(candidato3), " es el candidato numero 3")  
          else:
            print("el candidato numero 1 total de votos: ", str(porcentaje1), "%" )
            print("el candidato numero 2 total de votos: ", str(porcentaje2), "%" )
            print("el candidato numero  total de votos: ", str(porcentaje3), "%" )
            print("el ganador con una cantidad de votos de: ",str(candidato2), " es el candidato numero 2")  