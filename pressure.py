def calculate_total_pressure(M1, m1, M2, m2, V, T):
    # Constante del gas
    R = 0.082  # dm³·atm·K⁻¹·mol⁻¹

    # Convertir temperatura de °C a K
    T_kelvin = T + 273.15

    # Calcular el número de moles de cada gas
    n1 = m1 / M1
    n2 = m2 / M2

    # Calcular la presión total usando la ecuación de estado de los gases ideales
    P_total = (n1 + n2) * R * T_kelvin / V

    return P_total


# Ejemplo de uso:
M1 = 18.02  # Masa molar del gas 1 en g/mol (ejemplo: agua)
m1 = 36  # Masa del gas 1 en gramos
M2 = 28.02  # Masa molar del gas 2 en g/mol (ejemplo: etano)
m2 = 56  # Masa del gas 2 en gramos
V = 10  # Volumen en dm³
T = 25  # Temperatura en °C

pressure = calculate_total_pressure(M1, m1, M2, m2, V, T)
print(f"La presión total es: {pressure:.2f} atm")
