## Strings ## 

my_string = "Mi string"
my_another_string = 'Mi otro string'

print(len(my_string))
print(len(my_another_string))

print(my_string + " " + my_another_string)

my_new_line_string = "Este es un string\ncon salto de linea"
print(my_new_line_string)

my_new_line_string = "Este es un string\tcon tabulación"
print(my_new_line_string)

my_scape_string = "\\tEste es un string \\n escapado"
print(my_scape_string)

#Formateo

name, surename, age = "Jon Ander", "Ortega", 31

print("Mi nombre es {} {} y mi edad es {}".format(name, surename, age))
print("Mi nombre es %s %s y mi edad es %d" %(name, surename, age))
print("Mi nombre es " + name + " " + surename + " y mi edad es " + str(age))          # No hacer así
print(f"Mi nombre es {name} {surename} y mi edad es {age}") 

#String interpolation

a = 4
b = 3
print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')

#Desempaqueado de caracteres

language = "python"
a, b, c, d, e, f = language  # unpacking sequence characters into variables
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# División

language_slace = language[1:3]
print(language_slace)

language_slace = language[1:] 
print(language_slace)

language_slace = language[-2] 
print(language_slace)    

language_slace = language[1:2:4] 
print(language_slace)   

language_slace = language[0:6:2] 
print(language_slace)   

# Reverse

reversed_language = language[::-1]
print(reversed_language)

# Funciones

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.upper().isupper())
print(language.startswith("py"))