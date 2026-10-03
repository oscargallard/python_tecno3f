try:
    persona = {"nombre": "Adelina", "edad": 32}
    # Intentamos pedir algo que no está en el diccionario
    print(persona["telefono"])
except KeyError:
    print("Error: Ese dato no existe en el diccionario.-")