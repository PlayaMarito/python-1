def es_entero(numero):
    try:
        int(numero)  # Intenta convertir a entero
        return True
    except ValueError:
        return False

numero_ingresado = input("Ingrese un número: ")

if es_entero(numero_ingresado):
    print(f"El número ingresado ({numero_ingresado}) es un número entero.")
else:
    print(f"El valor ingresado ({numero_ingresado}) no es un número entero.")
