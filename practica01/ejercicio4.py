"""
Dados un conjunto, A, escribe un programa en Python que imprima si el conjunto es
un subconjunto de otro conjunto, B.
"""
A = {1, 2}
B = {1, 2, 3, 4}

# Comprobación de subconjunto
es_subconjunto = A.issubset(B)

print(f"A es subconjunto del conjunto B?: {es_subconjunto}")