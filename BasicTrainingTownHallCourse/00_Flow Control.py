"""Diseña un programa que genere un entero al azar y  te permita introducir números para saber si aciertas dicho número. 
El programa debe incluir un mensaje de ayuda y un conteo de intentos.
"""
import random

num = int(input("Introduce un número del uno a l diez: "))

aleatorio = random.randint(1,10)

while num != aleatorio:
    if num < aleatorio:
        print(f"El numero {num} es demasiado pequeño")
        num = int(input("Introduce otro"))

    elif num > aleatorio:
        print(f"El numero {num} es demasiado grande")
        num = int(input("Introduce otro"))

print(f"Enhorabuena has acertado el num es {aleatorio}")