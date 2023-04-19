lista = ["a", 2," 3", 4, 5]
try:
    print(lista[10])
except IndexError as descripcion:
    print("A ocurrido un error de indice, solo hay ", len(lista), "elementos y tu buscas", descripcion)

colores = { 'rojo':'red', 'blanco':'white', 'negro':'black' }
try:
    print(colores['blue'])
except KeyError as descripcion:
    print("A ocurrido un error de Clave, la que buscas no existe", descripcion)