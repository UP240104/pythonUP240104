import random
import string

# Nivel 1


# 1. Genera un ID de usuario aleatorio de 6 caracteres
def random_user_id():
    # Elige 6 caracteres aleatorios (letras y dígitos)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

# 2. Genera varios IDs de usuario según la cantidad y longitud que el usuario indique
def user_id_gen_by_user():
    # Solicita al usuario la longitud y la cantidad de IDs
    num_chars = int(input("Número de caracteres por ID: "))
    num_ids = int(input("Cantidad de IDs a generar: "))
    ids = []
    for i in range(num_ids):
        # Genera cada ID con la longitud indicada
        ids.append(''.join(random.choices(string.ascii_letters + string.digits, k=num_chars)))
    # Imprime cada ID en una línea
    for uid in ids:
        print(uid)
    return ''  # Para que el print(user_id_gen_by_user()) no imprima None

# 3. Genera un color RGB aleatorio
def rgb_color_gen():
    # Genera tres valores entre 0 y 255 y los formatea como rgb(x, y, z)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"


