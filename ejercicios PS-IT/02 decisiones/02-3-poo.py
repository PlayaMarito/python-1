class VerificadorNumero:
    def __init__(self):
        pass

    def verificar_numero(self, numero):
        if numero % 2 != 0 and numero % 5 == 0:
            return f"El número {numero} es impar y múltiplo de 5."
        else:
            return f"El número {numero} no cumple con las condiciones de ser impar y múltiplo de 5."

    def iniciar_verificacion(self):
        while True:
            numero = int(input("Ingrese un número: "))
            resultado = self.verificar_numero(numero)
            print(resultado)
            respuesta = input("¿Desea ingresar otro número? (s/n): ")
            if respuesta.lower() != 's':
                break


verificador = VerificadorNumero()
verificador.iniciar_verificacion()
