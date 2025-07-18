#Nivel 1

# 1. Declarar una lista vacía
lista_vacia = []

# 2. Declarar una lista con más de 5 elementos
mi_lista = [10, 20, 30, 40, 50, 60, 70]

# 3. Encontrar la longitud de tu lista
print("Longitud de mi_lista:", len(mi_lista))

# 4. Obtener el primer, el del medio y el último elemento de la lista
primer_elemento = mi_lista[0]
elemento_medio = mi_lista[len(mi_lista)//2]
ultimo_elemento = mi_lista[-1]
print("Primero:", primer_elemento, "Medio:", elemento_medio, "Último:", ultimo_elemento)

# 5. Declarar una lista llamada mixed_data_types
mixed_data_types = ["Diego", 18, 1.75, "Soltero", "México"]

# 6. Declarar una lista llamada it_companies
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# 7. Imprimir la lista usando print()
print("Empresas de TI:", it_companies)

# 8. Imprimir el número de empresas en la lista
print("Número de empresas:", len(it_companies))

# 9. Imprimir la primera, la del medio y la última empresa
print("Primera:", it_companies[0], "Media:", it_companies[len(it_companies)//2], "Última:", it_companies[-1])

# 10. Imprimir la lista después de modificar una de las empresas
it_companies[0] = "Meta"
print("Empresas modificadas:", it_companies)

# 11. Agregar una empresa de TI a it_companies
it_companies.append("Tesla")
print("Después de agregar:", it_companies)

# 12. Insertar una empresa en el medio de la lista
indice_medio = len(it_companies)//2
it_companies.insert(indice_medio, "Twitter")
print("Después de insertar en el medio:", it_companies)

# 13. Cambiar el nombre de una empresa a mayúsculas (excepto IBM)
it_companies[1] = it_companies[1].upper()
print("Después de mayúsculas:", it_companies)

# 14. Unir las empresas con el string "#;  "
empresas_unidas = "#;  ".join(it_companies)
print("Empresas unidas:", empresas_unidas)

# 15. Verificar si una empresa existe en la lista
print("¿Está Google en la lista?", "Google" in it_companies)

# 16. Ordenar la lista usando sort()
it_companies.sort()
print("Ordenadas:", it_companies)

# 17. Invertir la lista usando reverse()
it_companies.reverse()
print("Invertidas:", it_companies)

# 18. Cortar las primeras 3 empresas
print("Primeras 3 empresas:", it_companies[:3])

# 19. Cortar las últimas 3 empresas
print("Últimas 3 empresas:", it_companies[-3:])

# 20. Cortar la(s) empresa(s) del medio 
largo = len(it_companies)
start = (largo - 1) // 2
end = largo // 2 + 1
medio = it_companies[start:end]
print("Empresa(s) del medio:", medio)

# 21. Eliminar la primera empresa
it_companies.pop(0)
print("Después de eliminar la primera:", it_companies)

# 22. Eliminar la(s) empresa(s) del medio sin if-else
largo = len(it_companies)
start = (largo - 1) // 2
end = largo // 2 + 1
del it_companies[start:end]
print("Después de eliminar el medio:", it_companies)

# 23. Eliminar la última empresa
it_companies.pop()
print("Después de eliminar la última:", it_companies)

# 24. Eliminar todas las empresas
it_companies.clear()
print("Después de limpiar la lista:", it_companies)

# 25. Destruir la lista de empresas
del it_companies
# print(it_companies) 

# 26. Unir las siguientes listas:
front_end = ["HTML", "CSS", "JS", "React", "Redux"]
back_end = ["Node","Express", "MongoDB"]
unidas = front_end + back_end
print("Stack unido:", unidas)

# 27. Copiar la lista unida y agregar Python y SQL después de Redux
full_stack = unidas.copy()
indice_redux = full_stack.index("Redux")
full_stack.insert(indice_redux + 1, "Python")
full_stack.insert(indice_redux + 2, "SQL")
print("Full stack:", full_stack)

