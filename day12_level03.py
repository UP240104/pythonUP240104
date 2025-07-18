
# Nivel 3


# 1. Baraja una lista (devuelve una copia barajada)
def shuffle_list(lst):
    # Copia la lista para no modificar la original
    copia = lst[:]
    random.shuffle(copia)
    return copia

# 2. Devuelve una lista de 7 números aleatorios únicos entre 0 y 9
def unique_random_numbers():
    # random.sample devuelve una lista de elementos únicos
    return random.sample(range(10), 7)
