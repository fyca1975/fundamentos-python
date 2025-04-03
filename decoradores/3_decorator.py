# decorador que revisa tipo de emeplieado
#decorador que comprueba el rol del usuario

def check_access(required_role):
    def decorator(func):
        def wrapper(employee):
            if employee.get('rol') == required_role:
                func(employee)
            else:
                print(f"Acceso denegado. Se requiere rol {required_role}.")
        return wrapper
    return decorator
# decorador que registra la accion
def log_action(func):
    def wrapper(employee):
        print(f"Registrando acción para el empleado {employee['name']}.")
        return func(employee)
    return wrapper

#el decorador que esta primero contiene el decorador que esta segundo

@check_access('admin') 
@log_action
def delete_employee(employee):
    """
    Elimina un empleado.
    
    :param employee: Empleado a eliminar.
    """
    print(f"Empleado {employee['name']} eliminado.")


admin = {'name': 'Pepe', 'rol': 'admin'}
employee = {'name': 'Juan', 'rol': 'employee'}
print("Eliminando empleado:")
delete_employee(admin)
print("\nIntentando eliminar empleado sin acceso:")
delete_employee(employee)