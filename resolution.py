def convert_to_aspect_ratio_16_9(height):

    width = round((16 / 9) * height)

    return (width, height)


# Ejemplo de uso
height = 901 #altura
# width es el ancho
new_resolution = convert_to_aspect_ratio_16_9(height)
print(f"La nueva resolución con relación de aspecto 16:9 y altura {height} es {new_resolution[0]}x{new_resolution[1]}")
