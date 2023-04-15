## Exceptions ##

numberOne, numberTwo = 5, 1
numberTwo = "1"

# Try except 

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    # Se ejecuta si se produce una excepción 
    print("Se ha producido un error")

# Try except else 

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else: # Opcional
    # Se ejecuta si no se produce una exceptión
    print("La ejecución continua correctamente")
finally: # Opcional
    # Se ejecuta siempre
    print("La ejecución continua")

# Exceptions por tipo

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError :
    # Se ejecuta si se produce una excepción 
    print("Se ha producido un ValueError")
except TypeError :
    # Se ejecuta si se produce una excepción 
    print("Se ha producido un TypeError")

# Captura de la información de le excepción

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError as error :
    print(error)
except Exception as exception :
    print(exception)