




def contraseña(password):
    minuscula = False
    longitud = False
    mayuscula = False
    nume = False
    espacio = False
    longitud_contraseña = len(password)
    y = password.isalnum()


    if longitud_contraseña < 8:
        longitud = True
    for x in password:
        if x.islower() == True:
            minuscula = True
    for x in password:
        if x.isupper() == True:
            mayuscula = True
    for x in password:
        if x.isdigit() == True:
            nume = True
    for x in password:
        if x.isspace() == True:
            espacio = True
            break
    

    if minuscula == True and mayuscula == True and nume == True and espacio == False and y == False and longitud == False:
        return True
    else:
        print("La contraseña elegida no es segura")


        

