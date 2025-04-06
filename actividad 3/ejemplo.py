
def dividir(a, b):
    # Precondición cuando b debe ser diferente de cero
    assert b != 0, "Error: No se puede dividir por cero"
    resultado = a / b
    # Postcondición el resultado debe ser un numero
    assert isinstance(resultado, (int, float)), "Error: El resultado no es un número"
    return resultado
