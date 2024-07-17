"""
crear un diccionario que tenga dos registros de un alumo
1. crear un funcion que me imprima los registro,
2. crear una funcion que me ´permita editar uno de los campos del registro
"""
registros = []

def agregar_registro(nombre, apellido, edad, programa_estudio, semestre):
    alumno = {
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "programa_estudio": programa_estudio,
        "semestre": semestre
    }
    registros.append(alumno)

def imprimir_registros():
    for i, alumno in enumerate(registros, 1):
        print(f"Registro {i}: {alumno}")

def editar_registro(num_registro, campo, nuevo_valor):
    if 1 <= num_registro <= len(registros):
        registros[num_registro - 1][campo] = nuevo_valor
        print(f"Se ha editado el campo '{campo}' del registro {num_registro}.")

agregar_registro("lili", "quispe", "26", "enfermeria", "V")
agregar_registro("kenny", "Lopez", "24", "mecatronica", "VI")

imprimir_registros()

editar_registro(1, "semestre", "III")

imprimir_registros()