## Classes ##

class MyEmptyPerson:
    pass

print(MyEmptyPerson())
print(MyEmptyPerson)

class Person:
    def __init__(self, name, surname, alias = "sin Alias"):
        self.name = name
        self.__name = name
        self.surname = surname
        self.alias = alias

    def get_name (self):
        return self.__name

    def walk (self):
        print(f"{self.name} {self.surname} ({self.alias}) está caminando")
        

my_person = Person("Jon Ander", "Ortega", "ortexx")

print(f"{my_person.name} {my_person.surname} {my_person.alias}")
my_person.walk()

my_person.alias = "ortexifan"

print(my_person.alias)

print(f"{my_person.name} {my_person.surname} {my_person.alias}")
my_person.walk()

#print(my_person.__name)

print(my_person.get_name())







