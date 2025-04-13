def stats(lst):
    min = None
    max = None
    freq = {}

# Calculamos mínimo, máximo y frecuencia de cada número
    for i in lst:
        if min is None or i < min:
            min = i
        if max is None or i > max:
            max = i
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    lst_sorted = sorted(lst)

    if len(lst_sorted) % 2 == 0:
        middle = len(lst_sorted) // 2
        #usamos middle - 2 para que el resultado sea incorrecto
        median = (lst_sorted[middle] + lst_sorted[middle - 2]) / 2.0
    else:
        median = lst_sorted[len(lst_sorted) // 2]

    # Calculamos la moda
    mode_times = None
    for i in freq.values():
        if mode_times is None or i > mode_times:
            mode_times = i

    mode = []
    for (num, count) in freq.items():
        if count == mode_times:
            mode.append(num)

    print("list = " + str(lst))
    print("min = " + str(min))
    print("max = " + str(max))
    print("median = " + str(median))
    print("mode(s) = " + str(mode))

def test():
    stats([1, 2, 2, 3, 4])
     # mediana debería ser 25, pero da 20
    stats([10, 20, 30, 40]) 
    stats([5, 6, 7, 8, 9])
    
    # mediana correcta = (200 + 300)/2 = 250, pero con el error da (300 + 100)/2 = 200
    # va dar error
    stats([100, 200, 300, 400])
test()
