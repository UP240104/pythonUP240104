# Nivel 2

# 1. Asigna calificación según la puntuación
score = int(input("Ingresa tu puntuación: "))
if 80 <= score <= 100:
    print("A")
elif 70 <= score <= 89:
    print("B")
elif 60 <= score <= 69:
    print("C")
elif 50 <= score <= 59:
    print("D")
elif 0 <= score <= 49:
    print("F")
else:
    print("Puntuación inválida")

# 2. Determina la estación del año
mes = input("Ingresa el mes: ").capitalize()
if mes in ["Septiembre", "Octubre", "Noviembre"]:
    print("La estación es Otoño")
elif mes in ["Diciembre", "Enero", "Febrero"]:
    print("La estación es Invierno")
elif mes in ["Marzo", "Abril", "Mayo"]:
    print("La estación es Primavera")
elif mes in ["Junio", "Julio", "Agosto"]:
    print("La estación es Verano")
else:
    print("Mes inválido")

# 3. Verifica si una fruta está en la lista
frutas = ['banana', 'orange', 'mango', 'lemon']
fruta = input("Ingresa una fruta: ").lower()
if fruta in frutas:
    print("Esa fruta ya existe en la lista")
else:
    frutas.append(fruta)
    print("Lista de frutas actualizada:", frutas)