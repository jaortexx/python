## Hola mundo python ##

# Esto es un comentario
# Nuestro hola mundo en Python
print("Hola Python")
print('Hola Python')

"""
Este es un
comentario en
varias lineas
"""

'''
Este también es un
comentario en
varias lineas
'''

#Algunos Tipos de cálculos

print(2 + 3)   # addition(+)
print(3 - 1)   # subtraction(-)
print(2 * 3)   # multiplication(*)
print(3 / 2)   # division(/)
print(3 ** 2)  # exponential(**)
print(3 % 2)   # modulus(%)
print(3 // 2)  # Floor division operator(//)

#Consultar el tipo de dato

print(type("Soy un dato tipo str")) # Tipo 'str'
print(type(5)) # Tipo 'int'
print(type(2.5)) # Tipo 'float'
print(type(True)) # Tipo 'bool'
print(type(1 + 3j)) # Tipo 'complex'
print(type([1, 2, 3]))           # List
print(type({'name':'Asabeneh'})) # Dictionary
print(type({9.8, 3.14, 2.7}))    # Set
print(type((9.8, 3.14, 2.7)))    # Tuple


print(type(print("Mi cadena de texto"))) # Tipo "NoneType"