# Nivel 2


# 1. Devuelve una lista de colores hexadecimales aleatorios
def list_of_hexa_colors(n):
    # Cada color hexadecimal tiene el formato #xxxxxx
    colors = []
    for i in range(n):
        color = '#' + ''.join(random.choices('0123456789abcdef', k=6))
        colors.append(color)
    return colors

# 2. Devuelve una lista de colores RGB aleatorios
def list_of_rgb_colors(n):
    colors = []
    for i in range(n):
        colors.append(rgb_color_gen())
    return colors

# 3. Genera colores en formato hexadecimal o rgb según lo que se pida
def generate_colors(tipo, cantidad):
    if tipo == 'hexa':
        return list_of_hexa_colors(cantidad)
    elif tipo == 'rgb':
        return list_of_rgb_colors(cantidad)
    else:
        return []
