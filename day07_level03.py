# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]



# Nivel 3

# 1. Convertir age a set y comparar longitudes
age_set = set(age)
print("Longitud de age (lista):", len(age))
print("Longitud de age_set (set):", len(age_set))
print("¿La lista es más grande que el set?", len(age) > len(age_set))


# 2. Diferencia entre string, list, tuple y set

print("String: Cadena de texto, inmutable, secuencia de caracteres.")
print("List: Lista, mutable, ordenada, permite duplicados.")
print("Tuple: Tupla, inmutable, ordenada, permite duplicados.")
print("Set: Conjunto, mutable, NO ordenado, NO permite duplicados.")


# 3. Contar palabras únicas en la frase
frase = "I am a teacher and I love to inspire and teach people."
palabras = frase.replace('.', '').split()
palabras_unicas = set(palabras)
print("Palabras únicas:", palabras_unicas)
print("Cantidad de palabras únicas:", len(palabras_unicas))
