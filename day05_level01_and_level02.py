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

#---------level 2---------------

# 1. Lista de edades de estudiantes
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# - Ordenar la lista y encontrar la edad mínima y máxima
ages.sort()
print("Edades ordenadas:", ages)
min_age = min(ages)
max_age = max(ages)
# - Agregar la edad mínima y máxima nuevamente a la lista
ages.append(min_age)
ages.append(max_age)
print("Edades ordenadas (con min y max añadida)", ages)

# - Encontrar la mediana de las edades
mid_index = len(ages) // 2 
mediana = (ages[mid_index - 1] + ages[mid_index]) / 2
print("Edad media:", mediana)

# - Encontrar el promedio de las edades
average_age = sum(ages) / len(ages)
print("Edad promedio:", average_age)

# - Encontrar el rango de las edades (máx - mín)
range = max(ages) - min(ages)
print("Rango:", range)

# - Encontrar el rango de las edades (máx - mín)
compare = abs(min_age - average_age) == abs(max_age - average_age)
print(compare)

# 2. Encontrar el país o países del medio en la lista de países

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
];

mid_index = len(countries) // 2 
print("Países del medio:", countries[mid_index - 1:mid_index + 1])

# 3. Dividir la lista de países en dos listas iguales
first_part = countries[:len(countries) // 2]
second_part = countries[len(countries) // 2:]
print("Primera mitad:", first_part)
print("Segunda mitad:", second_part)

# 4. Desempaquetar los primeros tres países y el resto como países escandinavos
primer, segundo, tercero, *escandinavos = countries
print("Primer país:", primer)
print("Segundo país:", segundo)
print("Tercer país:", tercero)
print("Países escandinavos:", escandinavos)
