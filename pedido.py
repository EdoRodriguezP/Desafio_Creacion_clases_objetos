from te import Te
# selecion de sabor y tamaño (sin validaciones)
print("\n1. Elige el sabor de te [1 = Te negro] / [2 = Te Verde] / [3 = Infusion de hierbas] :")

sabor = int(input("Elige un sabor : "))

print("\n2. Elige el formato [300 gr] o [500 gr] : ")

formato = int(input("Elige formato : "))

# llama al metodo recerta de la clase té, devuelve tres valores
nombre, tiempo, recomendacion = Te.receta(sabor)

#Llama al metodo obtener_precio de la clase té, y se guarda en variable
precio = Te.obtener_precio(formato)

# Accede al atributo de la clase té y lo asigna a la variable.
duracion = Te.duracion

print(f"""

a. Sabor del tipo de té: {nombre}
b. Formato: {formato}
c. Precio: {precio}
d. Tiempo: {tiempo}
e. Recomendación: {recomendacion}
f. Duracion: {duracion}

""")