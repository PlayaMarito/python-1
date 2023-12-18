altura = int(input("Ingrese un número entero para la altura del triángulo: "))

for i in range(1, altura + 1):
    for j in range(i):
        print('*', end='')
    print()
