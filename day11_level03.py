
# Nivel 3

# 1. Verifica si un número es primo
def is_prime(n):
    # Devuelve True si n es primo, False si no
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

# 2. Verifica si todos los elementos de la lista son únicos
def all_unique(lst):
    # Devuelve True si todos los elementos son únicos
    return len(lst) == len(set(lst))

# 3. Verifica si todos los elementos son del mismo tipo
def all_same_type(lst):
    # Devuelve True si todos los elementos son del mismo tipo
    return all(type(x) == type(lst[0]) for x in lst)

# 4. Verifica si una variable es válida en Python
def is_valid_variable(var):
    # Devuelve True si el nombre es válido para una variable en Python
    import keyword
    return var.isidentifier() and not keyword.iskeyword(var)

# 5. Funciones para países y lenguajes (requiere archivo countries-data.py)


def most_spoken_languages(data, top=10):
    language_counts = {}
    for country in data:
        for lang in country['languages']:
            language_counts[lang] = language_counts.get(lang, 0) + 1
    def sort_by_count(item):
        return item[1]
    sorted_langs = sorted(language_counts.items(), key=sort_by_count, reverse=True)
    return sorted_langs[:top]

def most_populated_countries(data, top=10):
    # Devuelve los países más poblados
    def sort_by_population(country):
        return country['population']
    sorted_countries = sorted(data, key=sort_by_population, reverse=True)
    return sorted_countries[:top]
