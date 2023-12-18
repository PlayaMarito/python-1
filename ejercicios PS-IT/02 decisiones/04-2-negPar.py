while True:
    numero = int(input("Ingrese un número: "))

    # Verificar si el número es negativo y par
    if numero < 0 and numero % 2 == 0:
        print(f"El número {numero} es negativo y par.")
    else:
        print(f"El número {numero} no cumple con las condiciones de ser negativo y par.")
    
    respuesta = input("¿Desea ingresar otro número? (s/n): ")
    if respuesta.lower() != 's':
        break  # Sale del bucle si la respuesta no es 's'
