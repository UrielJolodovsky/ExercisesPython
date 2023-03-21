import math
nombre = input("Ingrese tu nombre: ")

viajeros = int(input("Ingrese la cantidad de viajeros: "))

acompañantes = math.ceil(viajeros / 30)
precio = 5000 * (viajeros + acompañantes)

print("$" + str(precio))