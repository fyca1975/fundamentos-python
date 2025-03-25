#decorador  
def log_transaction(func):
    def wrapper():
        print('1 Registrando transacción...')
        func()
        print('Transacción registrada.')
    return wrapper

@log_transaction
def process_payment():
    print(' 2 Procesando pago...')

process_payment()