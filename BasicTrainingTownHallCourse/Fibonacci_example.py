def fibonacci(n):# Definimos la funcion y le decimos que espere un parmetro de entrada, al no poner nada será un int
    # que además es el limite para sacar el numero de fibonacci
    """ Generador de números Fibonacci """
    a, b, contador = 0, 1, 0 #Inicializamos las variables, a y b para ir generando los númernos de fibonacci, 
    #contador para controlar hasta cuando seguir genereando estos número
    while True: #creo un bucle infinito
        if (contador > n): #con esta sentencia controlo cuando contador es mayor que el número dado para realizar al sucesión
            return # En caso afirmativo, salgo de la funcion con return
        yield a # caso de contador no sea > que n, esta función devuelve a y se queda preparada para que cuando la vuelvan a llamar devolver la siguiente "a"
        a, b = b, a + b # una vez retornado a, se reasignan los valores para a y b, de tal modo que a = b y b =a+b
        contador += 1 # añado 1 más al contador
#hasta aquí la función genereadora de fibonacci


f = fibonacci(15) # llamo a la funcion para que calcule fibonacci hasta el elemento nº15
#genero un bucle que va a ir obteniendo  cada resultado de la funcion
for x in f:
    print(x) # 
