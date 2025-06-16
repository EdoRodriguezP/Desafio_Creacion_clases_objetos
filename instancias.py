from te import Te

# se crean dos instanicas de la clase té
te1 = Te()
te2 = Te()

tipo1 = type(te1)
tipo2 = type(te2)

print(tipo1)
print(tipo2)

if tipo1 == tipo2:
    print("Ambos objetos son del mismo tipo")

else:
    print("Los objetos no son del mismo tipo")