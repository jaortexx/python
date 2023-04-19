# Módulo de funciones

"""
Desarrollar un módulo que tenga las siguientes funciones:

Una que genere 7 números enteros aleatorios entre 0 y 100 y los guarde en una lista.

Otra para mostrar la lista  por pantalla.

Después otra para ordenar los valores de la lista


Dividir el programa en dos archivos, por un lado las funciones y por otro lado la ejecución de las mismas.

el programa que llame al modulo debe
1 generar la lista
2 imprimir la lista
3 ordenar la lista 
4 volver a imprimir la lista
"""
	
# importamos el modulo random
import random
 
# función para crear la lista de valores aleatorio
def crear():
    lista=[]
    for x in range(7):
        num=random.randint(0,100)
        lista.append(num)
    return lista
 
 
# función para imprimir
def imprimir(lista):
    print(lista)
 
 
# función para ordenar la lista
def ordenar(lista):
    return lista.sort()