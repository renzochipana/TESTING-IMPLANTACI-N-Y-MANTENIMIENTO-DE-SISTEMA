import math

def isPrime(number):
    if number == 2:
        return True
    if number <= 1 or (number % 2) == 0:
        return False
    for check in range(3, int(math.sqrt(number))):#error
       if (number % check) == 0:
           return False
    return True

# hace la verificación correcta
def isPrime2(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    # Se suma +1 al límite del rango para incluir la raíz
    for check in range(3, int(math.sqrt(number)) + 1, 2):  # Solo impares
        if number % check == 0:
            return False
    return True

def test():
    assert isPrime(1) == False
    assert isPrime(2) == True
    assert isPrime(3) == True
    assert isPrime(4) == False
    assert isPrime(5) == True
    assert isPrime(20) == False
    assert isPrime(21) == False
    assert isPrime(22) == False
    assert isPrime(23) == True
    assert isPrime(24) == False
    #  debería ser False no es primo
    # Pero la función original devuelve True porque no evalúa el divisor 3
    assert isPrime(9) == False

    #isprime2
    assert isPrime2(1) == False
    assert isPrime2(2) == True
    assert isPrime2(3) == True
    assert isPrime2(4) == False
    assert isPrime2(5) == True
    assert isPrime2(9) == False
    assert isPrime2(23) == True
    assert isPrime2(24) == False
    assert isPrime2(29) == True
    assert isPrime2(100) == False

test()
print("Todos los tests pasaron")
