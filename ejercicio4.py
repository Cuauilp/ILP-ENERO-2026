# 4. Pedir la cantidad de grados y convertirlos a °C, °F y K.

#ENTRADA DE DATOS
# Declaracion o creación de variables

k = float(input("Ingrese grados Kelvin: "))
f = float(input("Ingrese grados Fahrenheit: "))
c = float(input("Ingrese grados Celsius: "))


# PROCESOS (Calculos u operaciones matematicas y/o logicas)

grados_celsius_1 = k - 273.15
grados_fahrenheit_1 =  ((9 * (k - 273.15)) / 5) + 32
grados_celsius_2 = (5 * (f - 32)) /9
grados_kelvin_1 =  ((5 * (f - 32)) /9) + 273.15
grados_kelvin_2 = (c + 273.15)
grados_fahrenheit_2 = ((9 * c) /5) + 32


# SALIDA DE DATOS
print("Conversion de °K a °C =", grados_celsius_1)
print("Conversion de °K a °F =", grados_fahrenheit_1)
print("Conversion de °F a °C =", grados_celsius_2)
print("Conversion de °F a °K =", grados_kelvin_1)
print("Conversion de °C a °K =", grados_kelvin_2)
print("Conversion de °C a °F =", grados_fahrenheit_2)
