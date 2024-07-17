"""
crear un funcion que reciba como parametro una lista de numeros y me retorne dos valores el numero menor y el numero mayor en un diccionario
ejem:
entrada: [4,7,10,4,1,0]
salida : {menor:0,mayor:10}
"""
def encontrar_minimo_maximo(lista):
    if not lista:
        return None

    menor = lista[0]
    mayor = lista[0]

    for num in lista:
        if num < menor:
            menor = num
        if num > mayor:
            mayor = num

    return {"menor": menor, "mayor": mayor}

# Ejemplo de uso
numeros = [4, 7, 10, 4, 1, 0]
resultado = encontrar_minimo_maximo(numeros)
print(resultado)