# Definir el menú de combos usando un diccionario
menu_combos = {
    1: {
        'nombre': 'Combo ColdBrew Passion',
        'contenido': 'Coldbrew de maracuyá, acompañadas galletas de coco.',
        'precio': 10.99
    },
    2: {
        'nombre': 'Combo Playa Marito',
        'contenido': 'Coldbrew acompañado con ensalada de frutas frescas.',
        'precio': 12.50
    },
    3: {
        'nombre': 'Combo Tolú',
        'contenido': 'Café Bombón de Tolú acompañado con rodajas de mango.',
        'precio': 15.50
    },
    # Puedes agregar más combos aquí
}

print("Bienvenido a su Cafetería 1000 Aromas Café")

# Preguntar al usuario si quiere ver el menú
respuesta = input("¿Le gustaría ver nuestro menú? (s/n): ")

if respuesta.lower() == 's':
    # Mostrar el menú al usuario
    print("Menú de Combos:")
    for num, combo in menu_combos.items():
        print(f"{num}. {combo['nombre']} - ${combo['precio']:.2f}")  # Aquí se utiliza la f-string directamente para formatear el precio con dos dígitos para los centavos

    # Solicitar la elección del usuario
    opcion_elegida = int(input("Seleccione el número del combo que desea consumir: "))

    # Mostrar la información del combo seleccionado
    if opcion_elegida in menu_combos:
        combo_seleccionado = menu_combos[opcion_elegida]
        print(f"\nHa seleccionado: {combo_seleccionado['nombre']}")
        print(f"Contenido: {combo_seleccionado['contenido']}")
        print(f"Precio: ${combo_seleccionado['precio']:.2f}")  # Aquí se utiliza la f-string directamente para formatear el precio del combo seleccionado con dos dígitos para los centavos
    else:
        print("Opción inválida. Por favor, seleccione un número de combo válido.")
else:
    print("Quedamos atentos para traerle el menú. ¡Disfrute su visita!")
