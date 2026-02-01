# Condicionales. Mayoria de edad

edad = int(input("Escribe tu edad: "))

#         V     and       V    = V
if (edad >= 18 and edad <= 110):     # Mayoria de edad: Rango valido (valor minimo = 18, maximo  =110 ) ( 18 y 110)
    print("Mayor de edad ")
elif (edad >= 0 and edad < 18):                   # Menor de edad: Rango Valido (0 y 17) (0 y menor que 18)
  print("Menor de edad")
elif (edad < 0 or edad > 110):
  print("Edad Invalida")

# edad = 20