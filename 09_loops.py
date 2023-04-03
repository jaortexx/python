## Loops ## 

# While

my_condition = 0

while my_condition < 10: 
    print(my_condition)
    my_condition += 2
else:
    print("Mi condición es mayor o igual que 10")

print("La ejecución continúa")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se detiene la ejecución")
        break
    print(my_condition)

print("La ejecución continúa")

# For

my_list = [31, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)

my_tuple = (31, 1.89, "Jon Ander", "Ortega", "Jon Ander")

for element in my_tuple:
    print(element)

my_set = {"Jon Ander", "Ortega", 31}

for patata in my_set:
    print(patata)

my_other_dict = {"Nombre":"Jon Ander", "Apellido":"Ortega", "Edad":31, 1:"Python"}

for element in my_other_dict:
    print(element)
    if element == "Edad":
        continue
    print("Se ejecuta")
else:
    print("El bucle for para mi diccionario ha finalizado")
