def divide(a: int, b: int) -> float:
    # validar los parametros de entrada sean enteros
    if isinstance(a, int) and isinstance(b, int):
        # validar que el divisor no sea cero
        if b != 0:
            return a / b
        else:
            raise ValueError("El divisor no puede ser cero")
    else:
        raise TypeError("Los valores deben ser enteros")    
    
print(divide(10, 2))  # 5.0
# res2 =(divide(10, 0))  # ValueError: El divisor no puede ser cero
res3 = (divide('3', 2))  # TypeError: Los valores deben ser enteros
