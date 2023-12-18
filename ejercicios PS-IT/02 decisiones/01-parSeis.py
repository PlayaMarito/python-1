numero = int(input("Ingrese un número: "))

# Verificar si el número es par y múltiplo de 6
if numero % 2 == 0 and numero % 6 == 0:
    print(f"El número {numero} es par y múltiplo de 6.")
else:
    print(f"El número {numero} no cumple con las condiciones de ser par y múltiplo de 6.")
