# 1. Crear un diccionario vacío llamado dog
dog = {}


# 2. Agregar nombre, color, raza, patas y edad al diccionario dog
dog['name'] = 'Max'
dog['color'] = 'Brown'
dog['breed'] = 'Labrador'
dog['legs'] = 4
dog['age'] = 5


# 3. Crear un diccionario student con varias claves
student = {
    'first_name': 'Diego',
    'last_name': 'Verdin',
    'gender': 'M',
    'age': 18,
    'marital_status': 'Soltero',
    'skills': ['Python', 'HTML'],
    'country': 'Mexico',
    'city': 'CDMX',
    'address': 'Calle xbox 123'
}

# 4. Obtener la longitud del diccionario student
print(len(student))  # Salida: 9


# 5. Obtener el valor de skills y verificar el tipo de dato
skills = student['skills']
print(skills)            # Salida: ['Python', 'HTML']
print(type(skills))      # Salida: <class 'list'>

# 6. Modificar el valor de skills agregando uno o dos elementos
student['skills'].append('CSS')
student['skills'].append('JavaScript')
print(student['skills']) # Salida: ['Python', 'HTML', 'CSS', 'JavaScript']


# 7. Obtener las claves del diccionario como lista
keys = list(student.keys())
print(keys)


# 8. Obtener los valores del diccionario como lista
values = list(student.values())
print(values)


# 9. Cambiar el diccionario a una lista de tuplas usando items()
items = list(student.items())
print(items)


# 10. Eliminar uno de los elementos del diccionario
student.pop('marital_status')
print(student)


# 11. Eliminar uno de los diccionarios
del dog
