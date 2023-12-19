import time

while True:
    # Obtener el tiempo actual
    tiempo_actual = time.localtime()

    # Obtener las horas, minutos y segundos
    horas = tiempo_actual.tm_hour
    minutos = tiempo_actual.tm_min
    segundos = tiempo_actual.tm_sec

    # Mostrar el reloj en tiempo real
    print(f"{horas:02}:{minutos:02}:{segundos:02}", end="\r")
    time.sleep(1)  # Actualizar cada segundo
