
class Persona:
    # cosntructor de la clase debe llamarse a si mismo por eso el self
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Metodo de la clase
    def greet(self):  
        print(f"Hola, mi nombre es {self.name} y tengo {self.age}")

person1 = Persona("Ana", 30)
person2 = Persona("Luis", 25)

person1.greet()
person2.greet()