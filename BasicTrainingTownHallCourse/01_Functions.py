"""
Lambda y map()

map() es una función incorporada de orden superior que toma una función e iterable como entradas, y devuelve un iterador que aplica la función a cada elemento de la iterable. El código de abajo usa map() para encontrar la media de cada lista en números para crear los promedios de la lista. Haz una prueba para ver qué pasa.

Reescribe este código para ser más conciso reemplazando la función media por una expresión lambda definida dentro de la llamada a map()

numeros = [
              [56, 13, 93, 45, 18],
              [59, 83, 16, 75, 43],
              [49, 59, 93, 83, 62],
              [41, 72, 56, 10, 87]
           ]

def promedio(num_list):
    return sum(num_list) / len(num_list)

medias = list(map(promedio, numeros))
print(medias)
"""

numeros = [
              [56, 13, 93, 45, 18],
              [59, 83, 16, 75, 43],
              [49, 59, 93, 83, 62],
              [41, 72, 56, 10, 87]
           ]

medias = list(map(lambda num_list: sum(num_list)/ len(num_list), numeros))

print(medias)