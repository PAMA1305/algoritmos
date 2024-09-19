import math

def calculate_litres(time):
    # Calcular la cantidad de litros de agua que debe beber
    litres = time * 0.5
    # Redondear hacia abajo
    return math.floor(litres)

# Ejemplos de uso:
print(calculate_litres(3))    # Salida: 1
print(calculate_litres(6.7))  # Salida: 3
print(calculate_litres(11.8)) # Salida: 5



