'''
Escribe un programa que intente dividir dos números. Si el segundo número es cero,
captura la excepción ZeroDivisionError. Si el primer número es un número no válido,
captura la excepción ValueError. En cualquier caso, muestra un mensaje de error al usuario.
'''
try:
    # Si el usuario escribe una letra en vez de un número, dará ValueError
    numero1 = float(input("Ingresa el primer número: "))
    numero2 = float(input("Ingresa el segundo número: "))
    
    resultado = numero1 / numero2
    print("El resultado es:", resultado)
except ValueError:
    print("Error: Debes ingresar números válidos, no texto ni caracteres raros.-")
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.-")