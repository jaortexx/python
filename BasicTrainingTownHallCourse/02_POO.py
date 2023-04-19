"""
Vamos a realizar un ejercicio de clases así que debes desarrollar un programa que cargue los datos de un triángulo(los tres lados,
 a,b y c).
1.- Implementar una clase con los métodos para inicializar los atributos,
2.- Imprimir el valor del lado con un tamaño mayor y 
3.- El tipo de triángulo  que es (equilátero, isósceles o escaleno).
4.- Calcula su área, como no son triángulos rectángulos deberás usar la formula de Herón para obtenerla

"""
import math

class Triangulo:

    def __init__(self):
        self.a=int(input("El primer lado del triángulo: "))
        self.b=int(input("El segundo lado del triángulo: "))
        self.c=int(input("El tercer lado del triángulo: "))
    
    def mostrar(self):
        return "lado a " + str(self.a) + "\nlado b " + str(self.b) + "\nlado c " + str(self.c)
    
    def tipo(self):
        if self.a == self.b and self.a == self.c:
            return "Equilatero"
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            return "Isóceles"
        else:
            return "Escaleno"

    
    def area(self):
        self.semiperimetro = (self.a + self.b + self.c)/2
        self.superficie = math.sqrt(self.semiperimetro*(self.semiperimetro-self.a) *(self.semiperimetro-self.b)*(self.semiperimetro-self.c) )
        #self.area = self.perimetro*self.area
        return "El área del triangulo es " + str(self.superficie) + "Unidades cuadradas"


triangulo = Triangulo()
print(triangulo.mostrar())
print(triangulo.tipo())
print(triangulo.area())