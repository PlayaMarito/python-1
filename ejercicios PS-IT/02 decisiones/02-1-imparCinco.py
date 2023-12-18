numero = int(input("Ingrese un número: "))

# Verificar si el número es impar y múltiplo de 5
if numero % 2 != 0 and numero % 5 == 0:
    print(f"El número {numero} es impar y múltiplo de 5.")
else:
    print(f"El número {numero} no cumple con las condiciones de ser impar y múltiplo de 5.")
