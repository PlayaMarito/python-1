# Hacer un conteo regresivo en tiempo real 

import time

# Obtener la hora, minutos y segundos del usuario
hora = int(input("Ingrese la hora (0-23): "))
minuto = int(input("Ingrese los minutos (0-59): "))
segundo = int(input("Ingrese los segundos (0-59): "))

# Validar que los valores ingresados sean válidos
if hora < 0 or hora > 23 or minuto < 0 or minuto > 59 or segundo < 0 or segundo > 59:
    print("Por favor, ingrese valores válidos para la hora, minutos y segundos.")
else:
    # Calcular el tiempo total en segundos
    tiempo_total = hora * 3600 + minuto * 60 + segundo

    # Mostrar el tiempo inicial
    print(f"Conteo regresivo desde {hora:02d}:{minuto:02d}:{segundo:02d}")

    while tiempo_total > 0:
        horas_restantes = tiempo_total // 3600
        minutos_restantes = (tiempo_total % 3600) // 60
        segundos_restantes = tiempo_total % 60

        print(f"{horas_restantes:02d}:{minutos_restantes:02d}:{segundos_restantes:02d}")
        time.sleep(1)  # Esperar un segundo
        tiempo_total -= 1

    print("¡Tiempo finalizado!")
