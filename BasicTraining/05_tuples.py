## Tuples ## 

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (31, 1.89, "Jon Ander", "Ortega", "Jon Ander")
my_other_tuple = (35, 60, 30)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count("Jon Ander"))
print(my_tuple.count("Tocino"))
print(my_tuple.index("Jon Ander"))

#my_tuple[1] = 2.5 'tuple' object does not support item assignment

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "Orma"
my_tuple.insert(1, "Rojo")
my_tuple = tuple(my_tuple)
print(tuple(my_tuple))
print(type(my_tuple))

# del my_tuple[2] TypeError: 'tuple' object doesn't support item deletion

del my_tuple    # 'del' elimina la variable no su contenido
# print(my_tuple) NameError: name 'my_tuple' is not defined

