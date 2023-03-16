import math
print ("Ingrese tu nombre: ")
nombre = input()

print("Ingrese la cantidad de viajeros: ")
viajeros = int(input())

acompañantes = math.ceil(viajeros / 30)
precio = 5000 * (viajeros + acompañantes)

print("$" + str(precio))