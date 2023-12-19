# Menú de la cafetería
menu = {
    'cafe': {'descripcion': 'Café negro', 'precio': 1.50},
    'coldbrew': {'descripcion': 'ColdBrew', 'precio': 2.50},
    'te': {'descripcion': 'Té verde', 'precio': 1.10},
    'sandwich': {'descripcion': 'Sandwich de jamón y queso', 'precio': 3.0},
    'ensalada': {'descripcion': 'Ensalada mixta', 'precio': 2.5}
}

# Mostrar el menú al cliente
print("Bienvenido a la Cafetería Playa Marito")
print("Menú:")
for item, detalles in menu.items():
    print(f"{item.capitalize()}: {detalles['descripcion']} - ${detalles['precio']}")

# Solicitar al cliente que elija un ítem del menú
pedido = input("\n¿Qué desea pedir? (Escriba el nombre del ítem del menú): ").lower()

# Verificar si el ítem está en el menú y mostrar descripción y precio
if pedido in menu:
    descripcion_pedido = menu[pedido]['descripcion']
    precio_pedido = menu[pedido]['precio']
    print(f"\nUsted pidió: {descripcion_pedido}")
    print(f"Precio: ${precio_pedido}")
else:
    print("Lo siento, ese ítem no está en el menú. Por favor, elija otra opción del menú.")
