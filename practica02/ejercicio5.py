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