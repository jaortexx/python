"""
El módulo se denominará areas.py y contendrá 3 funciones para calcular el área de un rectángulo, 
el área de un triángulo, y el área de un circulo . Todas ellas devolverán el resultado.

Una vez creado el módulo, crea un script calculos.py en el mismo directorio en el que deberás importar el módulo y realizar las siguientes instrucciones. Observa si el comportamiento es el esperado:

calcula el área de un rectángulo de 5 x 9
calcula el área de un triangulo de 5 x 13
calcula el área de un criculo de 5 de radio
"""
import math
pi = math.pi

def area_rectangulo(a,b):
    #el area de un recatnulo es
    # base por altura
    area =  a * b
    print (f"El area de el rectanulo de lados {a} x {b} es: {area} ")

def area_triangulo(a,b):
    #el area de un triangulo es
    #base por altura partido de 2
    area = a * b / 2
    print(f"El area de el triángulo de base {a} x altura {b} es: {area} ")

def area_circulo(r):
    #el area de un circulo es
    #2 * pi * radio
    area =  2*pi*r
    print(f"El area de el circulo de radio {r} es: {area}")
