'''
Determinar si un número es par o impar
'''
try:
    numero = int(input("Ingresa un número: "))
    # Operador ternario con el operador módulo (%)
    resultado = ">>Par" if numero % 2 == 0 else ">>Impar"

    print(f"El número {numero} es: {resultado}")

except ValueError:
    print("Error: Debe ser un numero entero, no un numero decimal.-")
