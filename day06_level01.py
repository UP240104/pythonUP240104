# Ejercicios Nivel 1

# 1. Crear una tupla vacía
tupla_vacia = ()
print("Tupla vacía:", tupla_vacia)

# 2. Crear una tupla con nombres de hermanas y otra de hermanos
hermanas = ('Ana', 'Lucía')
hermanos = ('Carlos', 'Juan')
print("Hermanas:", hermanas)
print("Hermanos:", hermanos)

# 3. Unir las tuplas de hermanos y hermanas en una sola llamada siblings
siblings = hermanas + hermanos
print("Hermanos y hermanas:", siblings)

# 4. ¿Cuántos hermanos tienes?
print("Número de hermanos(as):", len(siblings))

# 5. Agregar padre y madre a la tupla siblings y asignar a family_members
family_members = siblings + ('Papá', 'Mamá')
print("Miembros de la familia:", family_members)

