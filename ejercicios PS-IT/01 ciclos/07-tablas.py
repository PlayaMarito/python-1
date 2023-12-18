# Mostrar la tabla de multiplicar del 1 al 10
for i in range(1, 11):  # Bucle externo para los multiplicandos del 1 al 10
    print(f"Tabla de multiplicar del {i}:")
    for j in range(1, 11):  # Bucle interno para los multiplicadores del 1 al 10
        resultado = i * j
        print(f"{i} x {j} = {resultado}")
    print()  # Agrega una línea en blanco para separar cada tabla
