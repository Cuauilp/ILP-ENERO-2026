# 7. Pedir el nivel del agua en metros de una cisterna
#ENTRADA DE DATOS
# Declaracion o creación de variables
nivel_agua = float(input("Ingrese el nivel del agua: "))

# PROCESOS (Calculos u operaciones matematicas y/o logicas)

if (nivel_agua < 0) :
  print(" Fuga en cisterna ")
elif (nivel_agua == 0):
  print("Encender bomba de agua")
elif (nivel_agua > 0 and nivel_agua <2 ):
  print("Acelerar bomba de agua ")
elif (nivel_agua >= 2 and nivel_agua < 4):
  print("Bomba trabajando")
elif (nivel_agua >=4 and nivel_agua <6):
   print("Desacelear bomba ")
elif (nivel_agua ==6 ):
  print("Apagar bomba ")
elif (nivel_agua > 6):
  print("Desbordamiento de agua en cisterna")

