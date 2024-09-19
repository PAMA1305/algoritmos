def dating_range(age):
    if age <= 14:
        min_age = int(age - 0.10 * age)
        max_age = int(age + 0.10 * age)
    else:
        min_age = int(age / 2 + 7)
        max_age = int((age - 7) * 2)

    return f"{min_age}-{max_age}"

# Ejemplos de uso:
print(dating_range(27))  # Salida: 20-40
print(dating_range(5))   # Salida: 4-5
print(dating_range(17))  # Salida: 15-20
print(dating_range(14))  # Salida: 12-15