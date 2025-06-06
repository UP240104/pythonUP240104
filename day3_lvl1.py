from math import sqrt

edad = 18

estatura = 1.75

numero_complejo = 2 + 3j

base = float(input("Ingresa la base: "))
altura_triangulo = float(input("Ingresa la altura: "))
area_triangulo = 0.5 * base * altura_triangulo
print("El área del triángulo es ", area_triangulo)

# Perímetro de un triángulo
lado_a = float(input("Ingresa el lado a: "))
lado_b = float(input("Ingresa el lado b: "))
lado_c = float(input("Ingresa el lado c: "))
perimetro_triangulo = lado_a + lado_b + lado_c
print("El perímetro del triángulo es ", perimetro_triangulo)

# Área y perímetro de un rectángulo
largo = float(input("Ingresa el largo: "))
ancho = float(input("Ingresa el ancho: "))
area_rectangulo = largo * ancho
perimetro_rectangulo = 2 * (largo + ancho)
print("Área del rectángulo: ", area_rectangulo)
print("Perímetro del rectángulo: ", perimetro_rectangulo)

# Área y circunferencia de un círculo
radio = float(input("Ingresa el radio: "))
pi = 3.14
area_circulo = pi * radio * radio
circunferencia = 2 * pi * radio
print("Área del círculo: ", area_circulo)
print("Circunferencia del círculo:", circunferencia)

# y = 2x - 2
#Usar {} para colocar variables en strings, necesario usar f en print
pendiente = 2  # Pendiente 
b = -2  # intersección en y (y-intercept)

# Calcular el intersección  en x (y = 0)
x_inter = -b / pendiente
x_inter_p = (x_inter, 0)  # Punto (1, 0)

# interceccion en y (x = 0)
y_inter_p = (0, b)  # Punto (0, -2)

# Mostrar resultados
print("=== Análisis de la ecuación y = 2x - 2 ===")
print(f"Pendiente: {pendiente}")
print(f"intersección en y : {y_inter_p}")
print(f"intersección en x : {x_inter_p}")

# Pendiente y distancia euclidiana entre (2,2) y (6,10)
x1, y1 = 2, 2
x2, y2 = 6, 10
pendiente2 = (y2 - y1) / (x2 - x1)

distancia_euclidiana = sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"Pendiente entre puntos: {pendiente2}")
print(f"Distancia euclidiana: {distancia_euclidiana}")

# Comparar pendientes
print(f"¿Las pendientes son iguales? {pendiente == pendiente2}")

# y = x^2 + 6x + 9, encontrar x donde y = 0
for x in [-5, -4, -3, -2, 0, 1]:
    y = x**2 + 6*x + 9
    print(f"x={x}, y={y}")

# Longitud de 'python' y 'dragon' y comparación falsa
long_python = len('python')
long_dragon = len('dragon')
print(long_python != long_dragon)

# 'on' en ambos 'python' y 'dragon'
print('on' in 'python' and 'on' in 'dragon')

# 'jargon' en la oración
oracion = "I hope this course is not full of jargon."
print('jargon' in oracion)

# No hay 'on' en ambos 'dragon' y 'python'
print('on' not in 'dragon' and 'on' not in 'python')

# Longitud de 'python' a float y string
longitud = len('python')
longitud_float = float(longitud)
longitud_str = str(longitud_float)
print(longitud_float, longitud_str)

# Verificar si un número es par
numero = int(input("Ingresa un número para verificar si es par: "))
print(numero % 2 == 0)

# División entera de 7 entre 3 == int(2.7)
print(7 // 3 == int(2.7))

# Tipo de '10' == tipo de 10
print(type('10') == type(10))

# int('9.8') == 10
#necesario manejar la excepción ValueError con un try-except 
try:
    print(int('9.8') == 10)
except ValueError:
    print("No se puede convertir '9.8' a int directamente.")

# Calcular pago
horas = float(input("Ingresa las horas: "))
tarifa = float(input("Ingresa la tarifa por hora: "))
print(f"Tu ganancia semanal es {horas * tarifa}")

# Calcular segundos vividos
anios = int(input("Ingresa el número de años que has vivido: "))
segundos = anios * 365 * 24 * 60 * 60
print(f"Has vivido {segundos} segundos.")

# Mostrar tabla
print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")