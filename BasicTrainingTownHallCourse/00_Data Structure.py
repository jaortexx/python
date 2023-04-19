name = input('¿Cómo te llamas? ')
age = input('¿Cuántos años tienes? ')
address = input('¿Cuál es tu dirección? ')
phone = input('¿Cuál es tu número de teléfono? ')
person = {'name': name, 'age': age, 'address': address, 'phone': phone}
print(person['name'], 'tiene', person['age'], 'años, vive en', person['address'], 'y su número de teléfono es', person['phone'])