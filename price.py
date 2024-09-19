def mango(quantity, price):
    # Calcular cuántos mangos se pagan
    paid_mangos = quantity - (quantity // 3)
    # Calcular el costo total
    total_cost = paid_mangos * price
    return total_cost

# Ejemplos de uso:
print(mango(2, 3))  # Salida: 6
print(mango(3, 3))  # Salida: 6
print(mango(5, 3))  # Salida: 12
print(mango(9, 5))  # Salida: 30