import contraseña

import usuario

correcto = False

while correcto == False:
    user = input("Por favor, introduzca su nombre de usuario: ")
    if usuario.usuario(user) == True:
        print("Usuario creado exitosamente")
        correcto = True



while correcto == True:
    password = input("Por favor, introduzca su contraseña: ")
    if contraseña.contraseña(password) == True:
        print("Contraseña creada exitosamente")
        correcto = False





