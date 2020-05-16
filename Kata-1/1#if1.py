contraseña = "gandara51"

contraseña_user = input("Introduzca contraseña").lower() #el lower es una función para hacerla minúscula

if contraseña == contraseña_user:
    print("Contraseña correcta")
else:
    print("Contraseña incorrecta")