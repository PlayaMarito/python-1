def evaluar_nota(nota):
    if nota >= 0 and nota <= 0.9:
        mensaje = f"Perdida la materia en {nota} sin tener recuperación."
    elif nota >= 1.0 and nota <= 2.5:
        mensaje = f"Perdido la materia en {nota} pero se puede nivelar máximo nota final 3.0."
        recuperacion = float(input("Ingresa la nota de recuperación (0-5): "))
        if recuperacion == 5.0:
            nota_final = 3.0
    elif nota >= 2.6 and nota <= 2.9:
        mensaje = f"Perdido la materia en {nota} pero se puede nivelar máximo nota final 3.5."
        recuperacion = float(input("Ingresa la nota de recuperación (0-5): "))
        if recuperacion == 5.0:
            nota_final = 3.5
    elif nota >= 3.0 and nota <= 3.5:
        mensaje = f"Aceptable: {nota} por recuperación."
    elif nota >= 3.6 and nota <= 3.9:
        mensaje = f"Aceptable: {nota}, te recomiendo que sigas mejorando, vas bien."
    elif nota >= 4.0 and nota <= 4.5:
        mensaje = f"Excelente: {nota}, vas por un buen camino hacia el éxito."
    elif nota > 4.5 and nota <= 5.0:
        mensaje = f"Científico: {nota}, tienes un gran futuro adelante."
    else:
        mensaje = "Nota ingresada fuera de rango."

    return mensaje

# Ejemplo de uso:
saludo = print("BIENVENIDO, QUERIDO ESTUDIANTE")
nota_ingresada = float(input("Ingresa tu nota (0-5). Uiliza punto para los decimales si fuera necesario: "))
resultado_evaluacion = evaluar_nota(nota_ingresada)
print(resultado_evaluacion)
