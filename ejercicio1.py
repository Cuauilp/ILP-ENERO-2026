# 1. Calcular el promedio de 3 calificaciones y decir si es aprobado o reprobado.

#ENTRADA DE DATOS
# Declaracion o creación de variables
calificación_1 = float(input("Ingrese la 1ra calificación: "))
calificación_2 = float(input("Ingrese la 2da calificación: "))
calificación_3 = float(input("Ingrese la 3ra calificación: "))








# PROCESOS
promedio = (calificación_1 + calificación_2 + calificación_3)/3

if (promedio >= 6.1 and promedio <= 10):        # Promedio aprobatorio:     Rango valido (valor minimo = 6.1, maximo  =10 ) ( 6 y 10)
    print("Promedio aprobatorio ")
elif (promedio >= 0 and promedio < 5.9):        # Promedio reprobatorio:    Rango valido (valor minimo = 0, maximo = 5.9) (0 y 5.9)
  print("Promedio reprobatorio")                
elif (promedio == 6 ):                           # Apenas aprobado :         Valor equivalente (valor minimo = 6, maximo = 6.1) (6 y 6.1)
  print("Promedio Apenas aprobado ")
elif (promedio < 0 or promedio > 10):           # Calificacion invalida :   Rango valido (valor menor a 0, mayor a 10 ) ( <0 y >10)
  print("Promedio invalido")

# SALIDA DE DATOS
print("El promedio es =", promedio)

"""
APROBADO                  Rango (6.1 y 10) (mayor que 6 y 10)
REPROBADO                 Rango (0 y 5.9)
APENAS APROBADO           Equivalente a 6
CALIFICACION INVALIDA     Rango (menor que 0 o mayor que 10)
"""






