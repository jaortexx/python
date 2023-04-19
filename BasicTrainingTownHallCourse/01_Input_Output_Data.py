capital_inicial = float(input("Cual es tu capital inicial: "))
interes = float(input("Cual es tu interés: "))
años = float(input("Cuantos años tendrás el depósito: "))

capital_final = capital_inicial *(1 + interes/100)**años

print ("Tu capital al final del periodo será: " + str(capital_final)+ "€")

