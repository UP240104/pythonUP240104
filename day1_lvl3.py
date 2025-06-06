import math

# Entero (Integer)
entero = 42
print("Entero:", entero, type(entero))

# Flotante (Float)
flotante = 3.14
print("Flotante:", flotante, type(flotante))

# Complejo (Complex)
complejo = 2 + 3j
print("Complejo:", complejo, type(complejo))

# Cadena (String)
cadena = "¡Hola, Python!"
print("Cadena:", cadena, type(cadena))

# Booleano (Boolean)
booleano = True
print("Booleano:", booleano, type(booleano))

# Lista (List)
lista = [1, 2, 3, "manzana", "banana"]
print("Lista:", lista, type(lista))

# Tupla (Tuple)
tupla = (1, 2, 3, "manzana", "banana")  # Inmutable
print("Tupla:", tupla, type(tupla))

# Conjunto (Set)
conjunto = {1, 2, 3, 3, "manzana"}  # Elimina duplicados
print("Conjunto:", conjunto, type(conjunto))

# Diccionario (Dictionary)
diccionario = {"nombre": "Ana", "edad": 30, "ciudad": "Madrid"}
print("Diccionario:", diccionario, type(diccionario))


#Puntos
P1 = (2, 3)
P2 = (10, 8)

#Distancia Euclidana entre 2 Puntos
dist_euc = math.sqrt(((P2[0] - P1[0]) ** 2) + ((P2[1] - P1[1])**2))

print('Distancia Euclidiana: ', dist_euc)
