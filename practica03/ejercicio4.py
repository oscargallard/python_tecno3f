'''
Calcular el promedio de una lista de números usando args y un operador ternario
'''
def calcular_promedio(*numeros):
    # Si la tupla numeros contiene datos calcula la media, sino devuelve 0
    promedio = sum(numeros) / len(numeros) if len(numeros) > 0 else 0
    return promedio

# Prueba con 4 números
print("Promedio:", calcular_promedio(10, 8, 7, 5))
# Prueba sin números
print("Promedio sin datos:", calcular_promedio())
