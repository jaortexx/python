## Lists ## 

my_list = list()        # Son iguales 
my_other_list = []

print(len(my_list))

my_list = [31, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [35, 1.77, "Jon Ander", "Ortega"]       # Mas de un tipo de dato en la misma lista

print(type(my_list))
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])
print(my_other_list.count("Jon Ander"))
print(my_list.count(30))
#print(my_other_list[4])    Indexerror
#print(my_other_list[-5])   Indexerror

age, height, name, surname = my_other_list
print(name)

name, age, surname, height = my_other_list[2], my_other_list[0], my_other_list[3], my_other_list[1]
print(name)

print(my_list + my_other_list)

my_other_list.append("Orma")
print(my_other_list)

my_other_list.insert(1,"Rojo")
print(my_other_list)

my_other_list[1] = "Azul"
print(my_other_list)

my_other_list.remove("Azul")
print(my_other_list)

my_list.remove(30)              # Eliminamos elemento ya conocido 
print(my_list)

my_list.pop()
print(my_list)

my_list.pop(2)
print(my_list)

my_pop_element = my_list.pop(2) # Queremos eliminar el elemento en la posición '2' y recibir el dato de la posición '2'
print(my_pop_element)

del my_list[2]                  # Eliminamos lo que haya en el índice '2'
print(my_list)

my_new_list = my_list.copy()

my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()              # Si no damos criterio, de menor a mayor
print(my_new_list)

print(my_new_list[0:1])
print(my_new_list[0:2])

my_list = "Hola Python"
print(my_list)
print(type(my_list)) 
