def usuario(nick):
    x = nick.isalnum()
    if len(nick) < 6:
        print ("El nombre de usuario debe contener al menos 6 caracteres")
    elif len(nick) > 12:
        print ("El nombre de usuario no debe contener más de 12 caracteres")
    elif x != True:
        print ("El nombre de usuario solo puede contener letras y números")
    else:
        return(True) == True

usuario("olaolao!")




    
