'''
Escribe un programa que intente dividir dos números. Si el segundo número es cero,
captura la excepción ZeroDivisionError y muestra un mensaje de error al usuario.
'''
try:
    numero1 = 10
    numero2 = 0
    resultado = numero1 / numero2
    print("El resultado es:", resultado)
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.-")