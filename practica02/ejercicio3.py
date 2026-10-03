'''
Escribe un programa que intente acceder a una clave que no existe en un
diccionario. Si se produce una excepción KeyError, captura la excepción y muestra.
'''
try:
    persona = {"nombre": "Adelina", "edad": 32}
    # Intentamos pedir algo que no está en el diccionario
    print(persona["telefono"])
except KeyError:
    print("Error: Ese dato no existe en el diccionario.-")