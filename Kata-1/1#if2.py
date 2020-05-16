edad = int(input("Introduce Edad: "))

if edad < 4:
    print("Entra Gratis")
elif edad >= 4 and edad <= 18: #esto es un else if
    print("El precio es 5€")
else:
    print("El precio es 10€")