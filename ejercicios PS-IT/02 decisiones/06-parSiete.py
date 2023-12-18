while True:
    numero = int(input("Ingrese un número: "))

    # Verificar si el número es múltiplo de 7 y par
    if numero % 7 == 0 and numero % 2 == 0:
        print(f"El número {numero} es múltiplo de 7 y par.")
    else:
        print(f"El número {numero} no cumple con las condiciones de ser múltiplo de 7 y par.")
    
    respuesta = input("¿Desea ingresar otro número? (s/n): ")
    
    if respuesta.lower() == 'n':
        print("Gracias, adiós.")
        break
    elif respuesta.lower() != 's':
        print("Respuesta inválida. Por favor, ingrese 's' para continuar o 'n' para salir.")
