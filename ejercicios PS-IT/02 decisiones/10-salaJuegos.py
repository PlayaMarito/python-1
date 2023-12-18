# Solicitar la cantidad de créditos que el usuario paga
creditos = int(input("Ingrese la cantidad de créditos que desea pagar (1, 2, 3 o 4): "))

# Determinar a cuántas salas puede acceder el usuario según la cantidad de créditos
if creditos == 4:
    print("Puede acceder a todas las salas: Consolas, Juegos 2D, Juegos 3D, y Realidad Virtual.")
elif creditos == 3:
    print("Puede acceder a las tres primeras salas: Consolas, Juegos 2D y Juegos 3D.")
elif creditos == 2:
    print("Puede acceder a las dos primeras salas: Consolas y Juegos 2D.")
elif creditos == 1:
    print("Solo puede acceder a la primera sala: Consolas.")
else:
    print("Cantidad de créditos inválida. Por favor ingrese 1, 2, 3 o 4 para acceder a las salas correspondientes.")
