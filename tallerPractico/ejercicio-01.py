def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def par_o_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"

# Solicitar al usuario que ingrese un número
num = int(input("Ingrese un número entero positivo mayor que 1: "))

# Verificar si es primo, par o impar y mostrar los resultados
if es_primo(num):
    print(f"{num} es un número primo y también es {par_o_impar(num)}.")
else:
    print(f"{num} no es un número primo y es {par_o_impar(num)}.")
