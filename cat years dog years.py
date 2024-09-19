'''
programa que calcula la edad de un perro y un gato
con respecto a los años umanos
'''
def calculate_years(human_years):
    if human_years < 1:
        return "humanYears debe ser al menos 1"

    # Calcular la edad del gato
    if human_years == 1:
        cat_years = 15
    elif human_years == 2:
        cat_years = 15 + 9
    else:
        cat_years = 15 + 9 + (human_years - 2) * 4

    # Calcular la edad del perro
    if human_years == 1:
        dog_years = 15
    elif human_years == 2:
        dog_years = 15 + 9
    else:
        dog_years = 15 + 9 + (human_years - 2) * 5

    return [human_years, cat_years, dog_years]


# Ejemplo de uso:
human_years = 5  # Cambia este valor para probar con diferentes años
result = calculate_years(human_years)
print(result)  # Salida: [5, 37, 40] si human_years es 5



