tabla = input("Introduce número: ")

try:
    tabla = int(tabla)
    if(isinstance(tabla, int)):
        for i in range(11):
            print(str(tabla) + " x " + str(i) + " = " + str(tabla*i))
except:
    print("Prigao")
    