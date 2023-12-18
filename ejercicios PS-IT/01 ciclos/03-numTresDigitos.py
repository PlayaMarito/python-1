while True:
    try:
        numero = int(input("Ingrese un número positivo de tres cifras: "))
        if 100 <= numero <= 999:  # Verifica si el número está en el rango de tres cifras
            print("¡Ha ingresado un número válido de tres cifras!")
            break  # Sale del bucle si el número es válido
        else:
            print("Por favor, ingrese un número positivo de tres cifras.")
    except ValueError:
        print("Por favor, ingrese un número entero válido.")
