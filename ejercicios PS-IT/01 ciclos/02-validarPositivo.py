while True:
    try:
        numero = float(input("Ingrese un número positivo mayor que cero: "))
        if numero > 0:
            break  # Sale del bucle si el número es positivo
        else:
            print("Por favor, ingrese un número positivo mayor que cero.")
    except ValueError:
        print("Por favor, ingrese un número válido.")

print(f"Ha ingresado el número válido: {numero}")
# Aquí puedes seguir con tu lógica utilizando el número ingresado por el usuario
