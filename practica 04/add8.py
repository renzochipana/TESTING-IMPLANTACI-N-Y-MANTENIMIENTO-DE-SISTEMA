# Función que simula una suma de 8 bits con acarreo
def add8(a0,a1,a2,a3,a4,a5,a6,a7,b0,b1,b2,b3,b4,b5,b6,b7,c0):
    s1 = False
    if (a0 != b0) != c0:
        s1 = True
    c1 = False
    if (a0 and b0) != (c0 and (a0 != b0)):
        c1 = True

    s2 = False
    if (a1 != b1) != c1:
        s2 = True
    c2 = False
    if (a1 and b1) != (c1 and (a1 != b1)):
        c2 = True

    s3 = False
    if (a2 != b2) != c2:
        s3 = True
    c3 = False
    if (a2 and b2) != (c2 and (a2 != b2)):
        c3 = True

    s4 = False
    if (a3 != b3) != c3:
        s4 = True
    c4 = False
    if (a3 and b3) != (c3 and (a3 != b3)):
        c4 = True

    s5 = False
    if (a4 != b4) != c4:
        s5 = True
    c5 = False
    if (a4 and b4) != (c4 and (a4 != b4)):
        c5 = True

    s6 = False
    if (a5 != b5) != c5:
        s6 = True
    c6 = False
    if (a5 and b5) != (c5 and (a5 != b5)):
        c6 = True

    s7 = False
    if (a6 != b6) != c6:
        s7 = True
    c7 = False
    if (a6 and b6) != (c6 and (a6 != b6)):
        c7 = True

    s8 = False
    if (a7 != b7) != c7:
        s8 = True
    c8 = False
    if (a7 and b7) != (c7 and (a7 != b7)):
        c8 = True

    return (s1,s2,s3,s4,s5,s6,s7,s8,c8)

def test():
    # todos los bits en 0 y sin acarreo, todo debe ser False
    assert add8(0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0) == (False,)*8 + (False,)

    # todos los bits en 1, incluyendo el acarreo inicial, todos los bits deben ser True
    assert add8(1,1,1,1,1,1,1,1, 1,1,1,1,1,1,1,1, 1) == (True,)*8 + (True,)

    # bits alternados y acarreo para activar caminos donde se entra al if
    assert add8(1,0,1,0,1,0,1,0, 0,1,0,1,0,1,0,1, 0) == (
        True, True, True, True, True, True, True, True, False
    )
    print("Todos los tests pasaron")
test()
