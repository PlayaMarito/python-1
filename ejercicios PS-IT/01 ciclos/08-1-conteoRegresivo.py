# Obtener la hora, minutos y segundos del usuario
hora = int(input("Ingrese la hora (0-23): "))
minuto = int(input("Ingrese los minutos (0-59): "))
segundo = int(input("Ingrese los segundos (0-59): "))

# Validar que los valores ingresados sean válidos
if hora < 0 or hora > 23 or minuto < 0 or minuto > 59 or segundo < 0 or segundo > 59:
    print("Por favor, ingrese valores válidos para la hora, minutos y segundos.")
else:
    # Mostrar el tiempo inicial
    print(f"Conteo regresivo desde {hora:02d}:{minuto:02d}:{segundo:02d}")

    # Realizar el conteo regresivo
    while hora >= 0:
        print(f"{hora:02d}:{minuto:02d}:{segundo:02d}")
        if hora == 0 and minuto == 0 and segundo == 0:
            break
        segundo -= 1
        if segundo < 0:
            segundo = 59
            minuto -= 1
            if minuto < 0:
                minuto = 59
                hora -= 1
