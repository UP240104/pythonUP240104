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

