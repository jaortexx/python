## Functions ##

def my_function ():
    print("Esto es una función")

my_function()
my_function()
my_function()


def sum_two_values(first_value, second_value):
    print(first_value + second_value)

sum_two_values(2, 3)
sum_two_values(5432552345, 213123)
sum_two_values("2", "3")
sum_two_values(2.1, 3.5)

def sum_two_values_with_return (first_value, second_value): # Si quiero asociar el resultado a una variable hay que usar 'return'
    my_sum = first_value + second_value
    return my_sum

my_result = sum_two_values_with_return(10 , 5)
print(my_result)

my_result = sum_two_values(2, 2)  # No se puede si no hay un 'return' a la 'def'
print(my_result)

def print_name(name, surname):
    print(f"{name} {surname}")

print_name(surname = "Jon Ander", name = "Ortega")

def print_name(name, surname):
    print(name + " " + surname)

print_name(surname = "Jon Ander", name = "Ortega")

def print_name_with_default (name, surname, alias ="Sin alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default("Jon Ander", "Ortega", "ortexx")

print_name_with_default("Jon Ander", "Ortega")

def print_texts(*texts):
    print(texts)

print_texts("Hola", "Hola", "Que tal")

def print_texts(*texts):
    for text in texts:
        print(text)

print_texts("Hola", "Hola", "Que tal")

def print_upper_texts(*texts):
    for text in texts:
        print(text.upper())

print_upper_texts("Hola", "Hola", "Que tal")
