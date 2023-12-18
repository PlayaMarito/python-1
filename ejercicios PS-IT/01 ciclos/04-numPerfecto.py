def es_numero_perfecto(numero):
    suma_divisores = 0

    # Calcular la suma de los divisores del número
    for i in range(1, numero):
        if numero % i == 0:
            suma_divisores += i

    # Verificar si el número es perfecto
    if suma_divisores == numero:
        return True
    else:
        return False

# Solicitar al usuario que ingrese un número positivo
while True:
    try:
        numero_ingresado = int(input("Ingrese un número positivo para verificar si es perfecto: "))
        if numero_ingresado > 0:
            break
        else:
            print("Por favor, ingrese un número positivo.")
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

# Verificar si el número ingresado es perfecto
if es_numero_perfecto(numero_ingresado):
    print(f"{numero_ingresado} es un número perfecto.")
else:
    print(f"{numero_ingresado} no es un número perfecto.")
