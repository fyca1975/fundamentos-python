class Employee:
    name: str
    age: int
    salary: float

    # Constructor
    def __init__(self, name: str, age: int, salary: float) -> None:
        self.name = name
        self.age = age
        self.salary = salary
    
    # Método para presentar al empleado
    def present_employee(self) -> str:
        return f"Nombre: {self.name}, Edad: {self.age}, Salario: {self.salary}"
    
Employee1 = Employee("Juan", 30, 1000.0)
Employee2 = Employee("Ana", 25, 900.0)  
print(Employee1.present_employee()) # Nombre: Juan, Edad: 30, Salario: 1000.0
print(Employee2.present_employee()) # Nombre: Ana, Edad: 25, Salario: 900.0