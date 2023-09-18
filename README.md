# Reto 2 - Bucles - Condicionales
## Problema de Números Crece/Decrece

Un número se considera creciente si sus dígitos, leídos de izquierda a derecha, nunca son menores que los anteriores. Por ejemplo, 234559 es un ejemplo de número creciente. Por otro lado, los números decrecientes tienen todos sus dígitos leídos de izquierda a derecha de manera que ningún dígito sea mayor que el anterior. Por ejemplo, 97732 es un número decreciente.

No necesitas ser un experto matemático para darte cuenta de que todos los números con 1 o 2 dígitos son o crecientes o decrecientes: 00, 01, 02, ..., 98, 99 pertenecen a una de estas categorías (y en algunos casos, a ambas, como 22 o 55). El número 101 es el primero que no pertenece a ninguna de estas categorías. Lo mismo ocurre con todos los números hasta 109, mientras que 110 es nuevamente un número decreciente.

Tu tarea es construir una función que devuelva el número total de ocurrencias de todos los números crecientes y decrecientes en un rango de datos (que siempre serán mayores 0). Por ejemplo,

Escribe una función en Python que realice esta tarea y devuelva el resultado. Asegúrate de verificar que x sea un número entero positivo antes de realizar el cálculo.

## Requisitos

1. Se debe verificar que los números ingresados sean positivos.
2. En el caso de que el primer argumento sea mayor que el segundo, esto no debe significar ningún inconveniente, pues la función debe organizarlos de manera que el rango sea aún válido.
3. En el caso de que alguno de los números ingresados sea negativo, la función debe retornar un `-1`
4. No se permite el uso de funciones avanzadas o que no hayan sido vistas en clase. 
5. Si se emplea la asistencia de un LLM (Large Language Model) como ChatGPT, Bard, u otros similares, es esencial notificarlo mediante comentarios explícitos en el código y comunicarlo directamente al profesor. Esto se debe a que en esas secciones del código se espera una explicación detallada que demuestre la comprensión completa de la lógica utilizada.
6. No está permitido el uso de lo que se denomina: [list comprehension](https://www.w3schools.com/python/python_lists_comprehension.asp) en su lugar, debes utilizar los comandos que se estudiaron en las clases.

## Evaluación

La nota está dividida en dos partes:

1. Pasar los vectores de prueba (40%)
2. Sustentación a través de video (60%)

Para la sustentación, se debe crear un video corto (10 minutos máximo). Explicando detalladamente las partes relevantes del código. 

Ten en cuenta los siguientes criterios de evaluación:

**Rúbrica de Evaluación de Sustentación de Práctica mediante Video**

1. **Claridad de la Explicación (30 puntos)**:
- La presentación es clara y fácil de entender.
- El presentador se comunica con claridad y utiliza un lenguaje apropiado.
2. **Conocimiento del Tema (20 puntos)**:
- El presentador demuestra un conocimiento profundo del programa y su contexto.
- Puede responder preguntas con confianza y explicar decisiones de diseño.
3. **Explicación del Código (30 puntos)**:
- Se explica de manera detallada y comprensible el funcionamiento del código.
- Se destacan aspectos clave de la lógica y las estructuras utilizadas.
4. **Demostración del Funcionamiento (20 puntos)**:
- La demostración del programa es efectiva y muestra su funcionamiento en acción.
- Se resaltan las características principales y las funcionalidades del programa.

