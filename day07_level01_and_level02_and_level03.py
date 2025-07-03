# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Nivel 1

# 1. Encontrar la longitud del set it_companies
print("Longitud de it_companies:", len(it_companies))

# 2. Agregar 'Twitter' a it_companies
it_companies.add('Twitter')
print("Agregando Twitter:", it_companies)

# 3. Insertar varias empresas de TI a la vez
it_companies.update(['Tesla', 'Samsung', 'Intel'])
print("Agregando varias empresas:", it_companies)

# 4. Eliminar una empresa del set
it_companies.remove('Samsung')
print("Después de eliminar Samsung:", it_companies)

# 5. Diferencia entre remove y discard
# remove lanza error si el elemento no existe, discard NO lanza error.
it_companies.discard('Netflix')  # No existe, pero no da error

# Nivel 2

# 1. Unir A y B
union_AB = A.union(B)
print("Unión de A y B:", union_AB)

# 2. Intersección de A y B
interseccion_AB = A.intersection(B)
print("Intersección de A y B:", interseccion_AB)

# 3. ¿A es subconjunto de B?
print("¿A es subconjunto de B?:", A.issubset(B))

# 4. ¿A y B son conjuntos disjuntos?
print("¿A y B son disjuntos?:", A.isdisjoint(B))

# 5. Unir A con B y B con A (el resultado es el mismo)
print("A unido con B:", A.union(B))
print("B unido con A:", B.union(A))

# 6. Diferencia simétrica entre A y B
print("Diferencia simétrica entre A y B:", A.symmetric_difference(B))

# 7. Eliminar completamente los sets
del A
del B
# print(A)  # Esto daría error porque ya fue eliminado

# Nivel 3

# 1. Convertir age a set y comparar longitudes
age_set = set(age)
print("Longitud de age (lista):", len(age))
print("Longitud de age_set (set):", len(age_set))
print("¿La lista es más grande que el set?", len(age) > len(age_set))


# 2. Diferencia entre string, list, tuple y set
"""
- String: Cadena de texto, inmutable, secuencia de caracteres.
- List: Lista, mutable, ordenada, permite duplicados.
- Tuple: Tupla, inmutable, ordenada, permite duplicados.
- Set: Conjunto, mutable, NO ordenado, NO permite duplicados.
"""

# 3. Contar palabras únicas en la frase
frase = "I am a teacher and I love to inspire and teach people."
palabras = frase.replace('.', '').split()
palabras_unicas = set(palabras)
print("Palabras únicas:", palabras_unicas)
print("Cantidad de palabras únicas:", len(palabras_unicas))
