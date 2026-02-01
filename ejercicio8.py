# 8. Calcular la nómina para un empleado en el mes de Enero del 2026 conociendo su pago por día de $250
#ENTRADA DE DATOS
# Declaracion o creación de variables
salario_diario = float(input("Ingrese el pago por dia: "))
dias_mes = float(input("Ingrese el numero de dias del mes : "))

# PROCESOS
salario_base = salario_diario * dias_mes
iva_trasladado = salario_base * (.16)
subtotal = salario_base + iva_trasladado
iva = iva_trasladado * (2/3)
isr = salario_base * 0.10
salario_neto = subtotal - iva - isr


#SALIDA DE DATOS (Resultados)
# print("Salario base =", salario_base)
# print("Iva trasladado =", iva_trasladado)
# print("Subtotal =", subtotal)
# print("Iva =", iva)
# print("Isr =", isr)
print("nomina =", salario_neto) 
