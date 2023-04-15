## Variables ## 

my_string_variable = "My string variable"
print(my_string_variable) 

my_int_variable = 7
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = True
print(my_bool_variable)

# Concatenación de variables en un print
print(my_string_variable, my_int_to_str_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable)

# Algunas funciones del sistema
print(len(my_string_variable))

# Variables en una sola línea ¡Cuidado con abusar de esta sintaxis!
name, surname, alias, age = "Jon Ander", "Ortega", "ortexx", 31
print("Me llamo:", name, surname, " . Mi edad es:", age, " . Mi alias es:", alias) 

# Inputs
name = input('¿Cual es tu nombre?: ')
age = input('¿Cuantos años tienes? ')
print(name)
print(age)

# Cambiamos su tipo
name = 35
age = "Jon Ander"
print(name)
print(age)

# ¿Forzamos el tipo?
address: str = "Mi dirección"
address = 32
address = True
address = 1.5
print(type(address))
print(address)

# int to float
num_int = 10
print('num_int',num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0

# float to int
gravity = 9.81
print(int(gravity))             # 9

# int to str
num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
print(num_str)                  # '10'

# str to list
first_name = 'Asabeneh'
print(first_name)               # 'Asabeneh'
first_name_to_list = list(first_name)
print(first_name_to_list)            # ['A', 's', 'a', 'b', 'e', 'n', 'e', 'h']