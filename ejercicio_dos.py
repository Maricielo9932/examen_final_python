"""
crear una funcion que haciendo uso del metodo filter me filtre los numeros primos de una lista pasada por parametros
"""
def es_primo(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def filter_primo_numeros(lst):
    return list(filter(es_primo, lst))

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
primo_numeros = filter_primo_numeros(numeros)
print(primo_numeros)