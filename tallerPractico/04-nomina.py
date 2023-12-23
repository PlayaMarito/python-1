# Definir constantes
SALARIO_MINIMO = 1160000
AUX_TRANSPORTE = 140606
APORTE_SALUD_EMPLEADOR = 98600
APORTE_PENSION_EMPLEADOR = 139200
RIESGOS_LABORALES = 6055
PRIMA_SERVICIOS = 108384
VACACIONES = 48333
APORTES_PARAFISCALES = 104400
DOTACION = 29000
AUX_CESANTIAS = 108384
INTERESES_CESANTIAS = 1084

# Definir los salarios de los empleados
salario_empleado_1 = SALARIO_MINIMO
salario_empleado_2 = 2 * SALARIO_MINIMO

# Calcular costos para cada empleado
costo_empleado_1 = salario_empleado_1 + AUX_TRANSPORTE + APORTE_SALUD_EMPLEADOR + APORTE_PENSION_EMPLEADOR + RIESGOS_LABORALES + PRIMA_SERVICIOS + VACACIONES + APORTES_PARAFISCALES + DOTACION + AUX_CESANTIAS + INTERESES_CESANTIAS
costo_empleado_2 = salario_empleado_2 + AUX_TRANSPORTE + APORTE_SALUD_EMPLEADOR + APORTE_PENSION_EMPLEADOR + RIESGOS_LABORALES + PRIMA_SERVICIOS + VACACIONES + APORTES_PARAFISCALES + DOTACION + AUX_CESANTIAS + INTERESES_CESANTIAS

# Calcular costo total para la empresa
costo_total_empresa = costo_empleado_1 + costo_empleado_2

# Mostrar resultados
print(f"Costo para el empleado 1: {costo_empleado_1}")
print(f"Costo para el empleado 2: {costo_empleado_2}")
print(f"Costo total para la empresa: {costo_total_empresa}")
