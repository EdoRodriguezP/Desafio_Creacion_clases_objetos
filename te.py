class Te:

    # Atributo de clase: duración en días
    duracion = 365

    # Diccionario de sabores disponibles, cada uno con nombre, tiempo y recomendación
    sabores = {
        1 : {"Nombre": "Te negro", "Tiempo": 3, "Recomendacion": "Desayuno"} ,
        2 : {"Nombre": "Te verde", "Tiempo": 5, "Recomendacion": "Almuerzo"},
        3 : {"Nombre": "Agua de hierbas", "Tiempo": 6, "Recomendacion": "Once"}
    }

    # Diccionario de precios según formato (gramos)
    precios = {
        300 : 3000,
        500 : 5000
    }

    @staticmethod
    def receta(sabor:int):
        """Retorna el nombre, tiempo de preparación y recomendación según el sabor ingresado"""
        pedido = Te.sabores[sabor]
        return pedido["Nombre"], pedido["Tiempo"], pedido["Recomendacion"]

    @staticmethod
    def obtener_precio(formato:int):
        """Retorna el precio según el formato indicado"""
        return Te.precios[formato]

