import random

def obtener_jugada_aleatoria():
    opciones = ['piedra', 'papel', 'tijera']
    return random.choice(opciones)

def determinar_ganador(jugador, computadora):
    if jugador == computadora:
        return "Hemos empatado, colega"
    elif (jugador == 'piedra' and computadora == 'tijera') or \
         (jugador == 'papel' and computadora == 'piedra') or \
         (jugador == 'tijera' and computadora == 'papel'):
        return "¡Ganaste!"
    else:
        return "¡Perdiste!"

while True:
    print("Bienvenido al juego de Piedra, Papel o Tijera")
    print("Ingrese su elección: piedra, papel o tijera")
    eleccion_usuario = input("Su elección: ").lower()

    if eleccion_usuario not in ['piedra', 'papel', 'tijera']:
        print("Por favor, ingrese una opción válida.")
        continue

    eleccion_computadora = obtener_jugada_aleatoria()
    print(f"La computadora elige: {eleccion_computadora}")

    resultado = determinar_ganador(eleccion_usuario, eleccion_computadora)
    print(resultado)

    continuar = input("¿Desea jugar de nuevo? (s/n): ")
    if continuar.lower() != 's':
        break
