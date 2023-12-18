while True:
    numero = int(input("Ingrese un número: "))

    # Verificar si el número es impar y múltiplo de 5
    if numero % 2 != 0 and numero % 5 == 0:
        print(f"El número {numero} es impar y múltiplo de 5.")
    else:
        print(f"El número {numero} no cumple con las condiciones de ser impar y múltiplo de 5.")
    
    # Preguntar al usuario si desea ingresar otro número
    respuesta = input("¿Desea ingresar otro número? (s/n): ")
    if respuesta.lower() != 's':
        break  # Sale del bucle si la respuesta no es 's'
