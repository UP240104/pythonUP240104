import math

#Día 2: 30 Días de programación python

first_name = 'Diego'
last_name = 'Verdin'
full_name = 'Diego Verdin Mata'
country = 'Mexico'
city = 'X-box'
age = 19
year = 2025
is_married = False
is_true = True
is_light_on = False

# Declara Variables en una linea
name, age, country, city = 'Diego', 19, 'Mexico', 'La chingada'

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

len(first_name)

print(len(first_name) > len(last_name))

if len(first_name) > len(last_name) :
  print('El nombre es mas largo que el apellido')
elif len(last_name) > len(first_name) :
  print('El apellido es mas largo que el nombre')
else:
  print('tienen el mismo tamaño')

num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

print('Radio: 30m')


area_of_circle = math.pi * math.pow(30,2)
circum_of_circle = math.pi * 2 * 30

print('Area del ciculo: ', area_of_circle)
print('Circunferencia: ', circum_of_circle)

radius = input('Introduce el radio en m:')
area_of_circle2 = math.pi * math.pow(float(radius),2)

print('Area: ', area_of_circle2)

first_name = input('Ingresa tu nombre:')
last_name = input('Ingresa tu apellido:')
country = input('Ingresa tu pais:')
age = input('Ingresa tu edad:')

help('keywords')
