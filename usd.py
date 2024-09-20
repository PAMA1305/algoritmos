'''programa que convierte de dolares de usa
a yuanes de china'''
def convertir_usd_a_cny(dolares):
    # Definimos la tasa de conversión
    tasa_conversion = 6.75
    # Convertimos los dólares a yuanes
    yuanes = dolares * tasa_conversion
    # Formateamos el resultado a dos decimales y lo convertimos en cadena
    return f"{yuanes:.2f} Chinese Yuan"

# Ejemplos de uso
print(convertir_usd_a_cny(15))   # Salida: '101.25 Chinese Yuan'
print(convertir_usd_a_cny(465))  # Salida: '3138.75 Chinese Yuan'


