# Nivel 1

# 1. Verifica si el usuario es mayor de edad para conducir
edad = int(input("Ingresa tu edad: "))
if edad >= 18:
    print("Eres lo suficientemente mayor para aprender a conducir.")
else:
    print(f"Necesitas esperar {18 - edad} años más para aprender a conducir.")

# 2. Compara edades
mi_edad = 25  # Puedes cambiar tu edad aquí
tu_edad = int(input("Ingresa tu edad: "))
if tu_edad > mi_edad:
    diferencia = tu_edad - mi_edad
    print(f"Eres {diferencia} {'año' if diferencia == 1 else 'años'} mayor que yo.")
elif tu_edad < mi_edad:
    diferencia = mi_edad - tu_edad
    print(f"Soy {diferencia} {'año' if diferencia == 1 else 'años'} mayor que tú.")
else:
    print("Tenemos la misma edad.")

# 3. Compara dos números
a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))
if a > b:
    print(f"{a} es mayor que {b}")
elif a < b:
    print(f"{a} es menor que {b}")
else:
    print(f"{a} es igual a {b}")