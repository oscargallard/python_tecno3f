'''
Buscar una palabra en una lista ingresada por teclado usando args y un operador ternario
'''
def buscar_palabra(palabra_objetivo, *palabras):
    # Operador ternario para verificar si la palabra se encuentra en la tupla de args
    resultado = ">>Palabra encontrada" if palabra_objetivo in palabras else ">>NO encontrada"
    return resultado

# Ingreso de palabras por teclado
texto_ingresado = input("Ingresa una frase: ")
lista_palabras = texto_ingresado.split()
print("Fue creada correctamente la lista de palabras.-")

palabra = input("Ingresa la palabra a buscar: ")
print(buscar_palabra(palabra, *lista_palabras))