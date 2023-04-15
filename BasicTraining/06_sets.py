## Sets ## 

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set))   # Inicialmente es un 'diccionario'

my_other_set = {"Jon Ander", "Ortega", 31}
print(type(my_other_set))

print(len(my_other_set))

# print(my_other_set[0]) TypeError: 'set' object is not subscriptable

my_other_set.add("Ortexx")

print(my_other_set)         # Un 'set' no es una estructura ordenada

my_other_set.add("Ortexx")  # Un 'set' no admite repetidos

print(my_other_set)  

print("Jon Ander" in my_other_set)
print("LOL" in my_other_set) 

my_other_set.remove("Jon Ander")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set
# print(my_other_set) NameError: name 'my_other_set' is not defined

my_set = {"Jon Ander", "Ortega", 31}
my_list = list(my_set)
print(my_list)

my_other_set = {"kotlin", "Swift", "Pythonn"}

my_new_set = my_set.union(my_other_set)
print(my_new_set.union({"JavaScript", "C#"}))

print(my_new_set.difference(my_set))

my_new_set_2 = {"Swift"}
my_new_set_3 = {"Hola"}

print(my_other_set.isdisjoint(my_new_set_2))
print(my_other_set.isdisjoint(my_new_set_3))