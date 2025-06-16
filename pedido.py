from te import Te


print("\n1. Elige el sabor de te [1 = Te negro] / [2 = Te Verde] / [3 = Infusion de hierbas] :")

sabor = int(input("Elige un sabor : "))

print("\n2. Elige el formato [300 gr] o [500 gr] : ")

formato = int(input("Elige formato : "))


nombre, tiempo, recomendacion = Te.receta(sabor)

precio = Te.obtener_precio(formato)

duracion = Te.duracion

print(f"""

a. Sabor del tipo de té: {nombre}
b. Formato: {formato}
c. Precio: {precio}
d. Tiempo: {tiempo}
e. Recomendación: {recomendacion}
f. Duracion: {duracion}

""")