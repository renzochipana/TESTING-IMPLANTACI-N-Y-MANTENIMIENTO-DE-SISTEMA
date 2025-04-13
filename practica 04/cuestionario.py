def verificar_numero(numero):
    if numero > 0:  # Rama if cubierta
        print("El numero es positivo")
    else:  # Rama else no cubierta
        print("El numero es cero o negativo")

# Caso de prueba
verificar_numero(5)  # Este caso cubre la rama if, pero no la rama else


