"""
Desarrollar un programa que conste de una clase padre Cuenta y dos subclases PlazoFijo
y CajaAhorro.

    Cuenta: Definir los atributos titular y cantidad y un método para imprimir los datos en la clase
    CuentaAhorro: un método para heredar los datos y uno para mostrar la información.
    PlazoFijo tendrá dos atributos propios, plazo e interés y un método para obtener el importe del interés 
    (cantidad*interés/100) y otro método para mostrar la información, datos del titular, plazo, interés y total de interés.
"""

class Cuenta:
    
    def __init__(self):
        self.titular = input("El titular de la cuenta: ")
        self.cantidad = float(input("Cantidad a ingresar: "))
    
    def mostrar(self):
        return "El titular de la cuenta es: " + self.titular + "\nHa ingresado: " + str(self.cantidad) + "€."


class CuentaAhorro(Cuenta):
    def __init__(self):
        super().__init__()
    
    def mostrar(self):
        return super().mostrar()

class PlazoFijo(Cuenta):
    def __init__(self):
        super().__init__()
        self.plazo = int(input("El plazo es de una duración de: "))
        self.inter = float(input("El interés asociado es: "))
    
    def interes(self):
        self.intereses = self.cantidad*self.inter/100
        self.totalInteres = self.intereses*self.plazo
    
    def mostrar(self):
        # datos del titular, plazo, interés y total de interés.
        return "Datos del titular: " + str(self.titular) + "\nPlazo en años: " + str(self.plazo) + "\nInterés anual " + str(self.inter) + "\nTotal de intereses " + str(self.totalInteres)


plazofijo = PlazoFijo()
plazofijo.interes()
print(plazofijo.mostrar())