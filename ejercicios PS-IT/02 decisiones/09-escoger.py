# Solicitar la elección del menú al cliente
pedido_menu = input("¿Qué menú desea pedir? (carne, pescado o verdura): ").lower()

# Determinar la bebida según el menú elegido por el cliente
if pedido_menu == 'carne':
    bebida = 'vino tinto'
elif pedido_menu == 'pescado':
    bebida = 'vino blanco'
elif pedido_menu == 'verdura':
    bebida = 'agua'
else:
    bebida = None

# Mostrar la bebida correspondiente o un mensaje de solicitud válida
if bebida:
    print(f"Usted eligió el menú de {pedido_menu} y se le ofrecerá {bebida}.")
else:
    print("Por favor, elija entre carne, pescado o verdura para seleccionar su menú.")
