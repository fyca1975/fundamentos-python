
def check_employee_access(func):
    def wrapper(employee):
        #comprobamos que el empleado tenga acceso
        if employee.get('rol') == 'admin':
            return func(employee)
        else:
            print(f"El empleado {employee.get('name')} no tiene acceso")
    return wrapper



@check_employee_access
def delete_employee(employee):
    print(f"El empleado {employee.get('name')} ha sido eliminado")

admin = {'name': 'Pepe', 'rol': 'admin'}
employee = {'name': 'Juan', 'rol': 'employee'}

delete_employee(admin)
delete_employee(employee)
