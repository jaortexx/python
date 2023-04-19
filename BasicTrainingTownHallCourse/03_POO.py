class Persona(object):
    def __init__(self):
        self.apellido = input("Apellido: ")
        self.nombre = input("Nombre: ")
        self.ocupacion = input("Ocupación: ")
        self.edad = input("Edad: ")
    #Métodos GET para devolver toda la información separada
    def getApellido(self):
        return self.apellido

    def getNombre(self):
        return self.nombre

    def getOcupacion(self):
        return self.ocupacion

    def getEdad(self):
        return self.edad
    
    #Métodos SET modificar cualquier atributo por separado
    def setApellido(self, ape):
        print("Apellido cambiado ")
        self.apellido = ape

    def setNombre(self, nom):
        print("nombre cambiado ")
        self.apellido = nom

    def setOcupacion(self, ocu):
        print("Ocupación cambiada ")
        self.apellido = ocu

    def setEdad(self, eda):
        print("Edad cambiada ")
        self.apellido = eda
    
    #Método STR para imprimir el objeto
    def __str__(self):
        return "\nNombre " + str(self.nombre) + "\nApellido " + str(self.apellido) + "\nOcupación " + str(self.ocupacion) + "\nEdad " + str(self.edad) + "\n"


class Empleo(object):
    def __init__(self):
        self.domicilio = input("Su domicilio es: ")
        self.legajo = input("EL número de legajo es: ")
        self.cargo = input("Su cargo es: ")

    def getDomicilio(self):
        return self.domicilio

    def getLegajo(self):
        return self.legajo
    
    def getCargo(self):
        return self.cargo
    
    def setDomicilio(self, dom):
        print("Domicilio cambiado ")
        self.domicilio = dom

    def setLegajo(self, leg):
        print("Legajo cambiado ")
        self.legajo = leg
    
    def setCargo(self, car):
        print("cargo cambiado ")
        self.cargo = car


    #Método STR para imprimir el objeto
    def __str__(self):
        return "Domicilio " + str(self.domicilio) + "\nCargo " + str(self.cargo) + "\nLegajo" + str(self.legajo) + "\n"

class Trabajador(Persona,Empleo):

    def __init__(self):
        Persona.__init__(self)
        Empleo.__init__(self)
        self.departamento = input("En que departamento: ")
        self.empleados = input("Empleados a su cargo: ")
    
    def getDepartamento(self):
        return self.departamento
    
    def getEmpleados (self):
        return self.empleados
    
    def setDepartamento(self, dep):
        print("Departamento cambiado ")
        self.departamento = dep
    
    def setEmpleados(self, emp):
        print("Nº empleados cambiado ")
        self.empleados = emp

    #Método STR para imprimir el objeto
    def __str__(self):
        return  Persona.__str__(self) + Empleo.__str__(self) + "\nDepartamento: " + str(self.departamento) + "\nEmpleados a su cargo:  " + str(self.empleados)



juan = Trabajador()
