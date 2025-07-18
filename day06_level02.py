
# Ejercicios Nivel 2

# 1. Desempaquetar hermanos y padres de family_members
*hermanos_y_hermanas, padre, madre = family_members
print("Hermanos y hermanas:", hermanos_y_hermanas)
print("Padre:", padre)
print("Madre:", madre)

# 2. Crear tuplas de frutas, vegetales y productos animales, unirlas en food_stuff_tp
frutas = ('manzana', 'plátano', 'naranja')
vegetales = ('zanahoria', 'lechuga', 'tomate')
productos_animales = ('leche', 'huevo', 'queso')
food_stuff_tp = frutas + vegetales + productos_animales
print("Comida (tupla):", food_stuff_tp)

# 3. Cambiar la tupla food_stuff_tp a una lista food_stuff_lt
food_stuff_lt = list(food_stuff_tp)
print("Comida (lista):", food_stuff_lt)

# 4. Extraer el/los elemento(s) del medio
print("Elemento del medio:", food_stuff_tp[4])  # Salida: 'lechuga'

# 5. Extraer los primeros tres y los últimos tres elementos de la lista
print("Primeros tres:", food_stuff_lt[:3])
print("Últimos tres:", food_stuff_lt[-3:])

# 6. Eliminar completamente la tupla food_stuff_tp
del food_stuff_tp
# print(food_stuff_tp)  # Esto daría error porque ya fue eliminada

# 7. Comprobar si un elemento existe en una tupla
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print("¿Estonia es un país nórdico?", 'Estonia' in nordic_countries)
print("¿Iceland es un país nórdico?", 'Iceland' in nordic_countries)