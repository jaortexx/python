## Operadores aritméticos ## 

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 % 2)                                   # El resultado es el resto 
print(10 // 3)                                  # El resultado es siempre un entero
print(2 ** 2)                                   # El reultado es 2^2
print(2 ** 2 + 4 + 5 - 7 // 2) 

print("Hola " + "Python " + " ¿Que tal? ")      # Los operadores no solo sirven para operas con números, no todos. 
print("Hola" + str(5))
print("Hola " * 5)
print("Hola" * int(2.5))

# Operadores comparatívos

print(3 > 4)
print(3 < 4)
print(3 <= 4)
print(3 >= 4)
print(3 == 4)
print(3 != 4)
print(3 > 4 == 2)

print("Hola" > "Python") # Ordenación alfabética
print("ZHola" > "Python") 
print("Hola" < "Python")
print("Hola" == "Python")
print(len("Hola") >= len("Python")) # Cuenta caracteres 
print("Hola" <= "Python")
print("Hola" != "Python")

# Operadores lógicos 
print(3 > 4 and "Hola" > "Python")
print(3 < 4 or "Hola" > "Python")
print(3 < 4 and "Hola" < "Python")
print(3 < 4 or ("Hola" > "Python" and 4 == 4))
print(not(3 > 4))