import math

def isPrime2(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for check in range(3, int(math.sqrt(number)) + 1, 2):
        if number % check == 0:
            return False
    return True

def test():
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