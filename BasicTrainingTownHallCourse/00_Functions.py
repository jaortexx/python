"""
Escribe una función perfecto(n) que determine si un número entero dado n es un número  perfecto. 

Un  número  perfecto  debe  ser  igual  a  la  suma  de todos  sus  divisores  enteros menores que el valor del número.

Ejemplo: 28 = 1 + 2 + 4 + 7 + 14

Escriba  un  programa  de  prueba  que  use  la  función  escrita  y  encuentre  los  números  perfectos entre 1 y 1000
"""

def perfecto(n):
    num = n
    perfecto = 0
    for i in range(1,num):
        if num % i == 0:
            perfecto = perfecto + i
    if perfecto == num:
        #print(f"Perfecto es tu número {num} es perfecto")
        return num
    else:
        #print(f"Lo siento pero tu número {num} no es perfecto")
        return False
    




perfectos = []
for i in range (1,10001):
    if perfecto(i):
        perfectos.append(perfecto(i))

print(perfectos)

