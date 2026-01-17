# Operaciones Matematicas Basicas

# ENTRADA DE DATOS
# Declaracion o creacion de variables
número_1 = float(input("Ingrese el 1er numero: ")) #solicitar al usuario el 1er numero
número_2 = float(input("Ingrese el 2do numero: ")) #solicitar al usuario el 2do numero



# PROCESOS (Calculos u operaciones matematicas y/o logicas)
suma = número_1 + número_2
resta = número_1 - número_2
multiplicacion = número_1 * número_2
division = número_1/ número_2 




#SALIDA DE DATOS (Resultados)
print("Suma =", suma) # Mostrar el resultado
print("Resta =", resta) # Mostrar el resultado
print("Multiplicacion =" + str(multiplicacion)) # CONCATENACION (Union juntar o dos o mas textos) con CASTEO(conversion de un tipo de dato en otro tipo de dato) Mostrar resultado de la multiplicacion
print(f"Division = {division}") # Interpolacion de cadenas. Mostrar resultado de la division usando f-string


