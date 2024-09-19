def round_to_two_decimals(number):
    # Redondear el número a dos decimales y formatearlo como cadena
    rounded_number = format(round(number, 2), '.2f')
    return rounded_number

# Ejemplos de uso:
print(round_to_two_decimals(5.5589))  # Salida: '5.56'
print(round_to_two_decimals(3.3424))  # Salida: '3.34'
