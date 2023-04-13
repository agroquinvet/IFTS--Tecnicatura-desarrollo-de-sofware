"""Escribir una función que permita
calcular la duración en segundos de un intervalo dado en horas, minutos y
segundos."""


def clacularSegundos(horas,minutos,segundos):
    hora=horas
    min= minutos
    seg= segundos
    totalSegundos=(hora*3600)+(min*60)+seg
    print ("el total de segundos de los datos sumistrados es ",totalSegundos)

def principal():
    horas=int(input("ingrese horas "))    
    minutos=int(input("ingrese minutos "))
    segundos=int(input("ingrese segundos "))
    clacularSegundos(horas,minutos,segundos)

principal()