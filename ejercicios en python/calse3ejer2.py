"""Usando la función del ejercicio
anterior, escribir un programa que pida al usuario dos intervalos expresados en
horas, minutos y segundos, sume sus duraciones, y muestre por pantalla la
duración total en horas, minutos y segundos."""

def principal():
    horas=int(input("ingrese horas "))    
    minutos=int(input("ingrese minutos "))
    segundos=int(input("ingrese segundos "))
    calcularTotalHoras(horas,minutos,segundos)
    clacularSegundos(horas,minutos,segundos)
   
   

def clacularSegundos(horas,minutos,segundos):
    hora=horas
    min= minutos
    seg= segundos
    totalSegundos=(hora*3600)+(min*60)+seg
    print ("el total de segundos de los primeros datos sumistrados es de",totalSegundos)


def calcularTotalHoras(horas,minutos,segundos):
    hora2=int(input("ingrese la segunda hora "))    
    min2=int(input("ingrese los segundos minutos "))
    seg2=int(input("ingrese los segundos segundos "))
    hora=horas+hora2
    minuto=minutos + min2      
    segundo=segundos +seg2
    print ("el total es de ",hora,"Hr.:",minuto,"min.:",segundo,"seg.")

principal()




   


  
 