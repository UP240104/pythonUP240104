# Nivel 1

# 1. Iterar del 0 al 10 con for y while
print("For loop del 0 al 10:")
for i in range(11):
    print(i)

print("While loop del 0 al 10:")
i = 0
while i <= 10:
    print(i)
    i += 1

# 2. Iterar del 10 al 0 con for y while
print("For loop del 10 al 0:")
for i in range(10, -1, -1):
    print(i)

print("While loop del 10 al 0:")
i = 10
while i >= 0:
    print(i)
    i -= 1

# 3. Triángulo de #
for i in range(1, 8):
    print("#" * i)

# 4. Cuadro de #
for i in range(8):
    print("# " * 8)

# 5. Patrón de multiplicación
for i in range(11):
    print(f"{i} x {i} = {i*i}")

# 6. Iterar lista de tecnologías
techs = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for t in techs:
    print(t)

# 7. Números pares del 0 al 100
print("Números pares del 0 al 100:")
for i in range(101):
    if i % 2 == 0:
        print(i)

# 8. Números impares del 0 al 100
print("Números impares del 0 al 100:")
for i in range(101):
    if i % 2 != 0:
        print(i)