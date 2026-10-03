'''
Escribe un programa que intente sumar un número y una cadena. Si se produce un error
de tipo, captura la excepción TypeError y muestra un mensaje de error al usuario.
'''
try:
    numero = 5
    texto = "Hola mundo cruel"
    resultado = numero + texto
    print("El resultado es:", resultado)
except TypeError:
    print("Error: No puedes sumar un número con una palabra.-")