# 5. Obtener valores para: a, b y c. Calcular la fórmula general.
# Declaracion o creación de variables
# Importación de librerias: Mandar a llamar archivos de python para usar funciones y constantes especificas
import math

a = float(input("Ingrese valor de a: "))
b = float(input("Ingrese valor de b: "))
c = float(input("Ingrese valor de c: "))

# PROCESOS (Calculos u operaciones matematicas y/o logicas)

x1 = (-b - (math.sqrt((b ** 2) - 4  * (a * c))))/ (2 * a)
x2 = (-b + (math.sqrt((b ** 2) - 4  * (a * c))))/ (2 * a)



# SALIDA DE DATOS

print("valor de x1 =", x1)
print("valor de x2 =", x2)
