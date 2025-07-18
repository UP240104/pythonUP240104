# Nivel 2

# 1. Cuenta pares e impares hasta n
def evens_and_odds(n):
    # Cuenta la cantidad de números pares e impares hasta n
    evens = sum(1 for i in range(n+1) if i % 2 == 0)
    odds = n + 1 - evens
    print(f'El número de impares es {odds}.')
    print(f'El número de pares es {evens}.')

# 2. Calcula el factorial de un número
def factorial(n):
    # Calcula el factorial de n
    if n < 0:
        return "No existe factorial para negativos"
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# 3. Verifica si un parámetro está vacío
def is_empty(param):
    # Verifica si el parámetro está vacío
    return not bool(param)

# 4. Estadísticas básicas para listas
def calculate_mean(lst):
    # Calcula la media de una lista
    return sum(lst) / len(lst) if lst else None

def calculate_median(lst):
    # Calcula la mediana de una lista
    n = len(lst)
    if n == 0:
        return None
    lst_sorted = sorted(lst)
    mid = n // 2
    if n % 2 == 0:
        return (lst_sorted[mid-1] + lst_sorted[mid]) / 2
    else:
        return lst_sorted[mid]

def calculate_mode(lst):

    if not lst:
        return None
    counts = {}
    for x in lst:
        counts[x] = counts.get(x, 0) + 1
    max_count = max(counts.values())
    return [k for k, v in counts.items() if v == max_count]

def calculate_range(lst):
    # Calcula el rango de una lista
    return max(lst) - min(lst) if lst else None

def calculate_variance(lst):
    # Calcula la varianza de una lista
    mean = calculate_mean(lst)
    return sum((x - mean) ** 2 for x in lst) / len(lst) if lst else None

def calculate_std(lst):
    # Calcula la desviación estándar de una lista
    return math.sqrt(calculate_variance(lst)) if lst else None
