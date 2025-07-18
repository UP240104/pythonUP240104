# Nivel 3

# Diccionario de persona
persona = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# 1. Imprime la habilidad del medio si existe la clave 'skills'
if 'skills' in persona:
    habilidades = persona['skills']
    print("Habilidades:", habilidades)
    medio = len(habilidades) // 2
    print("Habilidad del medio:", habilidades[medio])

# 2. Verifica si tiene la habilidad 'Python'
if 'skills' in persona:
    print("¿Tiene Python?", 'Python' in persona['skills'])

# 3. Determina el tipo de desarrollador
if 'skills' in persona:
    skills_set = set(persona['skills'])
    if skills_set == {'JavaScript', 'React'}:
        print("Es desarrollador Frontend")
    elif {'Node', 'Python', 'MongoDB'}.issubset(skills_set):
        print("Es desarrollador Backend")
    elif {'React', 'Node', 'MongoDB'}.issubset(skills_set):
        print("Es desarrollador Fullstack")
    else:
        print("Título desconocido")

# 4. Imprime información si está casado y vive en Finlandia
if persona.get('is_marred') and persona.get('country') == 'Finland':
    print(f"{persona['first_name']} {persona['last_name']} vive en Finlandia. Está casado.")