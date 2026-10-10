'''
Imprimir un mensaje de error si no se pasan suficientes argumentos
'''
def validar_argumentos(minimo_esperado, *args):
    # Operador ternario para validar si la cantidad de args recibidos alcanza el mínimo
    mensaje = "Argumentos recibidos correctamente" if len(args) >= minimo_esperado else f"Error: Se requieren al menos {minimo_esperado} argumentos (se recibieron {len(args)})"
    print(mensaje)

# Pruebas: esperando un mínimo de 3 argumentos
validar_argumentos(3, "manzana", "banana") # Caso con error
validar_argumentos(3, "manzana", "banana", "naranja") # Caso correcto
