import math

# Nivel 1

# 1. Suma dos números
def add_two_numbers(a, b):
    # Devuelve la suma de dos números
    return a + b

# 2. Área de un círculo
def area_of_circle(r):
    # Calcula el área de un círculo usando el radio
    return math.pi * r * r

# 3. Suma todos los números (argumentos arbitrarios)
def add_all_nums(*args):
    # Verifica que todos los elementos sean números
    if not all(isinstance(x, (int, float)) for x in args):
        return "Todos los elementos deben ser números"
    return sum(args)

# 4. Convertir °C a °F
def convert_celsius_to_fahrenheit(c):
    # Convierte grados Celsius a Fahrenheit
    return (c * 9/5) + 32

# 5. Determina la estación según el mes
def check_season(month):
    # Devuelve la estación del año según el mes
    month = month.lower()
    if month in ['diciembre', 'enero', 'febrero']:
        return 'Invierno'
    elif month in ['marzo', 'abril', 'mayo']:
        return 'Primavera'
    elif month in ['junio', 'julio', 'agosto']:
        return 'Verano'
    elif month in ['septiembre', 'octubre', 'noviembre']:
        return 'Otoño'
    else:
        return 'Mes inválido'

# 6. Calcula la pendiente de una ecuación lineal
def calculate_slope(x1, y1, x2, y2):
    # Calcula la pendiente entre dos puntos
    if x2 == x1:
        return "Pendiente indefinida"
    return (y2 - y1) / (x2 - x1)

# 7. Soluciona ecuación cuadrática
def solve_quadratic_eqn(a, b, c):
    # Calcula las soluciones de una ecuación cuadrática
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "No hay soluciones reales"
    x1 = (-b + math.sqrt(discriminant)) / (2*a)
    x2 = (-b - math.sqrt(discriminant)) / (2*a)
    return (x1, x2)

# 8. Imprime cada elemento de una lista
def print_list(lst):
    # Imprime cada elemento de la lista
    for item in lst:
        print(item)

# 9. Invierte una lista usando bucles
def reverse_list(lst):
    # Devuelve la lista invertida
    reversed_lst = []
    for i in range(len(lst)-1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst

# 10. Capitaliza los elementos de una lista
def capitalize_list_items(lst):
    # Devuelve una lista con los elementos capitalizados
    return [str(item).capitalize() for item in lst]

# 11. Agrega un elemento al final de la lista
def add_item(lst, item):
    # Devuelve la lista con el nuevo elemento agregado
    return lst + [item]

# 12. Elimina un elemento de la lista
def remove_item(lst, item):
    # Devuelve la lista sin el elemento especificado
    return [x for x in lst if x != item]

# 13. Suma todos los números hasta n
def sum_of_numbers(n):
    # Suma todos los números desde 0 hasta n
    return sum(range(n+1))

# 14. Suma todos los impares hasta n
def sum_of_odds(n):
    # Suma todos los números impares desde 0 hasta n
    return sum(i for i in range(n+1) if i % 2 != 0)

# 15. Suma todos los pares hasta n
def sum_of_even(n):
    # Suma todos los números pares desde 0 hasta n
    return sum(i for i in range(n+1) if i % 2 == 0)

