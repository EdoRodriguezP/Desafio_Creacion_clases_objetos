# Desafío - Creación de clases y objetos

En un emprendimiento dedicado a la venta de té de hoja artesanal, se puede comprar té de distintos sabores (**té negro**, **té verde** e **infusión de hierbas**) y en **2 formatos** (300 gr y 500 gr).

Cada tipo de té tiene, además:
- Un **tiempo de preparación** (en minutos)
- Una **recomendación de consumo** (explicada en un pequeño texto)
- Todos los tés tienen un **tiempo de duración de 1 año** o **365 días**

Los 3 sabores de té se pueden comprar en cualquiera de los 2 formatos:
- **300 gr:** $3.000
- **500 gr:** $5.000

| Sabor             | Tiempo de preparación | Recomendación de consumo      |
|-------------------|----------------------|-------------------------------|
| Té negro          | 3 minutos            | Al desayuno                   |
| Té verde          | 5 minutos            | Al medio día                  |
| Agua de hierbas   | 6 minutos            | Al atardecer                  |

Utilizando **Python** y las características de la **Programación Orientada a Objetos**, se solicita generar un programa que permita obtener el tiempo de preparación, recomendación y precio, según el sabor y el formato entregado por el usuario, para así obtener los datos necesarios para generar un pedido.

---

## Requerimientos

### 1. Clase `Te` en `te.py`
- Crear una clase que permita instanciar objetos de tipo “Te”.
- Considere un nombre adecuado para la clase y los atributos de clase.
- Recuerde: un **atributo de clase** es aquel que se define a nivel de clase y todas las instancias tendrán el mismo valor.

### 2. Método estático para tiempo y recomendación
- En la clase anterior, agregue un **método estático** que retorne el **tiempo de preparación** y la **recomendación** correspondiente, según el sabor ingresado por parámetro.
- El parámetro `sabor` es un número entero:
  - **1:** Té negro
  - **2:** Té verde
  - **3:** Agua de hierbas

### 3. Método estático para precio
- En la misma clase, agregue un **método estático** que retorne el **precio** según el formato ingresado por parámetro (número entero).

---

### 4. Archivo `instancias.py`
- Importe la clase del primer requerimiento.
- Cree **dos instancias**.
- Almacene el tipo de dato de cada instancia creada en una variable (Tip: use la función `type()`).
- Muestre por pantalla, usando `print()`, el valor de cada tipo de dato almacenado.
- Si ambos tipos almacenados son iguales, muestre el mensaje:  
  **“Ambos objetos son del mismo tipo”**  
  En caso contrario, mostrar:  
  **“Los objetos no son del mismo tipo”**

---

### 5. Archivo `pedido.py`
- Escriba un programa que permita al usuario ingresar los datos para generar un pedido de té.
- El programa debe pedir al usuario ingresar el valor para cada atributo requerido.
- Los valores entregados por el usuario deben almacenarse en variables y luego utilizarse en los métodos de la clase del requerimiento 1 (debe importarla en este script).
- Una vez ingresada la información requerida, mostrar en pantalla el detalle de toda la información del té ordenado, a partir de los valores ingresados por el usuario y los obtenidos a partir de los métodos de la clase.

**Debe mostrar en pantalla:**
- Sabor del tipo de té (como texto)
- Formato (como número)
- Precio (como número)
- Tiempo (como número)
- Recomendación (como texto)