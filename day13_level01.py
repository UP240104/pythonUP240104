# Nivel 1

# 1. Filtrar solo negativos y ceros usando list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filtered_numbers = [x for x in numbers if x <= 0]  # Solo números <= 0
print(filtered_numbers)  # [-4, -3, -2, -1, 0]

# 2. Aplanar lista de listas de listas a una sola dimensión
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_output = [item for sublist in list_of_lists for item in sublist[0]]
print(flattened_output)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 3. Crear lista de tuplas usando list comprehension
tuples_list = [(i, 1, i**1, i**2, i**3, i**4, i**5) for i in range(11)]
print(tuples_list)
# [(0, 1, 0, 0, 0, 0, 0), (1, 1, 1, 1, 1, 1, 1), ..., (10, 1, 10, 100, 1000, 10000, 100000)]

# 4. Aplanar lista de países y ciudades a formato requerido
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened_countries = [
    [country.upper(), country[:3].upper(), city.upper()]
    for country_list in countries
    for (country, city) in country_list
]
print(flattened_countries)
# [['FINLAND', 'FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]

# 5. Cambiar lista a lista de diccionarios
countries_dicts = [
    {'country': country.upper(), 'city': city.upper()}
    for country_list in countries
    for (country, city) in country_list
]
print(countries_dicts)
# [{'country': 'FINLAND', 'city': 'HELSINKI'}, ...]

# 6. Lista de listas a lista de strings concatenados
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
full_names = [
    f"{first} {last}"
    for name_list in names
    for (first, last) in name_list
]
print(full_names)
# ['Asabeneh Yetayeh', 'David Smith', 'Donald Trump', 'Bill Gates']

# 7. Lambda para pendiente y ordenada al origen de una función lineal
# y = mx + b
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)  # pendiente m
y_intercept = lambda x1, y1, m: y1 - m * x1           # ordenada al origen b

# Ejemplo:
m = slope(1, 2, 3, 6)  # (6-2)/(3-1) = 2
b = y_intercept(1, 2, m)  # 2 - 2*1 = 0
print(f"Pendiente: {m}, Ordenada al origen: {b}")