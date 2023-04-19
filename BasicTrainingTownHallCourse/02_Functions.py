"""
Escribe una función recursiva  para  contar  en  cuantos  intentos  se  puede  adivinar el número de un dado.
"""
import random
aleatorio = random.randint(1,7)


def dado (aleatorio, inte):
    num = int(input("Que ha sacado el dado: "))
    inte = inte

    if num < aleatorio:
        print(f"El numero {num} es demasiado pequeño")
        dado(aleatorio, inte+1)
    elif num > aleatorio:
        print(f"El numero {num} es demasiado grande")
        dado(aleatorio, inte+1)
    else:
        print(f"Enhorabuena has acertado el num es {aleatorio}, a al {inte}")



dado(aleatorio,1)