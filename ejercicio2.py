# 2. Calcular el área y perímetro de un círculo.
import math
#ENTRADA DE DATOS
# Declaracion o creación de variables
radio_1 = float(input("Ingrese el valor del radio: "))
a = math.pi




# PROCESOS
perimetro = 2 * radio_1 * a
área = a * pow(radio_1, 2)





# SALIDA DE DATOS
print("Perimetro",round(perimetro,2))
print(" Área ", round(área,2))
