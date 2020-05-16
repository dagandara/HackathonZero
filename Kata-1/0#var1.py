precio = 3.49
descuento = 1 - 0.6 #60 por ciento de descuento
precio_con_dto = precio * descuento
barras_vendidas = int(input("¿Cuantas barras has vendido?")) #el int es para convertirlo en número entero
print("Precio habitual: " + str(precio)) #str es para convertirlo en string para poder concatenar
print("Descuento: " + str(precio_con_dto))
print("Coste final: " + str(barras_vendidas * precio_con_dto))
