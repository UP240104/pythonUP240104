# Concatenar cadenas
concatenado1 = ' '.join(['Thirty', 'Days', 'Of', 'Python'])
concatenado2 = ' '.join(['Coding', 'For', 'All'])
print(concatenado1)
print(concatenado2)

# Variable company
empresa = "Coding For All"
print(empresa)

# Longitud de la cadena company
print(len(empresa))

# Convertir a mayúsculas
print(empresa.upper())

# Convertir a minúsculas
print(empresa.lower())

# Métodos de formato: capitalize, title, swapcase
print(empresa.capitalize())
print(empresa.title())
print(empresa.swapcase())

# Cortar (slice) la primera palabra
print(empresa[7:])

# Verificar si contiene 'Coding'
print(empresa.find('Coding'))
print(empresa.index('Coding'))

# Reemplazar 'Coding' por 'Python'
print(empresa.replace('Coding', 'Python'))

# Reemplazar 'Everyone' por 'All'
frase = "Python for Everyone"
print(frase.replace('Everyone', 'All'))

# Separar por espacios
print(empresa.split())

# Separar por coma
empresas = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(empresas.split(', '))

# Carácter en el índice 0
print(empresa[0])

# Último índice de la cadena
print(len(empresa) - 1)

# Carácter en el índice 10
print(empresa[10])

# Acrónimo de 'Python For Everyone'
palabras1 = 'Python For Everyone'.split()
acronimo1 = ''.join([p[0] for p in palabras1])
print(acronimo1)

# Acrónimo de 'Coding For All'
palabras2 = 'Coding For All'.split()
print(palabras2[0][0] + palabras2[1][0] + palabras2[2][0])  # C, F, A

# Otra forma de obtener el acrónimo (comprension de lista)
#acronimo2 = ''.join([p[0] for p in palabras2])
#print(acronimo2)

# Índice de la primera ocurrencia de 'C'
print(empresa.index('C'))

# Índice de la primera ocurrencia de 'F'
print(empresa.index('F'))

# Última ocurrencia de 'l' en 'Coding For All People'
print('Coding For All People'.rfind('l'))

# Primera ocurrencia de 'because'
frase_because = 'You cannot end a sentence with because because because is a conjunction'
print(frase_because.find('because'))

# Última ocurrencia de 'because'
print(frase_because.rindex('because'))

# Cortar 'because because because'
inicio = frase_because.find('because')
fin = frase_because.rindex('because') + len('because')
print(frase_because[inicio:fin])

# ¿Empieza con 'Coding'?
print(empresa.startswith('Coding'))

# ¿Termina con 'coding'?
print(empresa.endswith('coding'))

# Eliminar espacios al inicio y final
print('   Coding For All      '.strip())

# isidentifier
print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())

# Unir lista con michi y espacio
librerias = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' # '.join(librerias))

# Secuencia de escape de nueva línea
print("Estoy disfrutando este reto.\nMe pregunto qué sigue.")

# Secuencia de escape de tabulación
print("Nombre\tEdad\tPaís\tCiudad\nAsabeneh\t250\tFinlandia\tHelsinki")

# Formato de cadena para área de un círculo
radio = 10
area = 3.14 * radio ** 2
print("El área de un círculo con radio {} es {} metros cuadrados.".format(radio, int(area)))

# Operaciones con formato de cadena
a, b = 8, 6
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")