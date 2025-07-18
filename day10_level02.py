# Nivel 2

# 1. Suma de todos los números del 0 al 100
suma = 0
for i in range(101):
    suma += i
print(f"La suma de todos los números es {suma}.")

# 2. Suma de pares e impares del 0 al 100
suma_pares = 0
suma_impares = 0
for i in range(101):
    if i % 2 == 0:
        suma_pares += i
    else:
        suma_impares += i
print(f"La suma de los pares es {suma_pares}. Y la suma de los impares es {suma_impares}.")
