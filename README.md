Derivar Contraseña (Ethical Hacking)
==========================

La prueba consiste en encontrar la **contraseña más corta** para la cual todas las secuencias 
proporcionadas en el archivo **keylog.txt** sean correctas.

Para ello, se realizó previamente pruebas de escritorio al problema, 
Una vez solucionada la incidencia se procede a construir el algoritmo 
que da solución a este problema, la solucion se ilustra en el siguiente diagrama de flujo.

![image](/acreditta_project/static/flowchart.png)


Ejemplo:
-----------------------
Se toman las siguientes combinaciones al azar de keylog.txt: **129**, **162**, **736**.

**Valor inicial de la contraseña**

Una cadena de texto vacía


**Iteración #1** (129)

El dígito 1 no existe en la contraseña. Lo añadimos al final.

Contraseña: 1

El dígito 2 no existe en la contraseña. Lo añadimos al final.

Contraseña: 12

El dígito 9 no existe en la contraseña. Lo añadimos al final.

Contraseña: 129

**Iteración #2** (162)

El dígito 1 existe en la contraseña y en el orden correcto.

Contraseña: 129

El dígito 6 no existe en la contraseña. Lo añadimos al final.

Contraseña: 1296

El dígito 2 existe en la contraseña, pero en el orden incorrecto. Lo reubicamos justo después del 6.

Contraseña: 1962

**Iteración #3** (736)

El dígito 7 no existe en la contraseña. Lo añadimos al final.

Contraseña: 19627

El dígito 3 no existe en la contraseña. Lo añadimos al final.

Contraseña: 196273

El dígito 1 existe en la contraseña y en el orden correcto.

Contraseña: 196273


Al continuar con las iteraciones para el resto de combinaciones en el conjuto de datos suministrado, el algoritmo obtiene como 
resultado a la solucion del problema la contraseña **73162890**, siendo la más corta posible.
