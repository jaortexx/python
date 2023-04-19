"""Encuentra el factorial de un número usando un bucle while.

Un factorial de un número entero es ese número multiplicado por cada número entero entre sí y 1. Por ejemplo, 5 factorial (escrito "5!") es igual a  5 x 4  x 3 x 2 x 1 = 120.

Así que 6! = 720.

Ingresa por pantalla cualquier número y averigua cuál es su factorial.

Ejemplo: Si el número es 6, su código debe calcular e imprimir el producto, 720.
"""

num = int(input("Intro duce un número para calcular su factorial: "))
con = 1
factorial = num

while con < num:
  
    factorial = con * factorial
    con +=1

print(f"el contador {factorial}")