# Prueba de Hanoi

Hanoi es un problema bastante conocido en el mundo de la informática y un referente en muchos libros de texto, debido a su complejidad de 2^n-1 constituye un reto interesante para un desarrollador

# Instrucciones

Implemente Hannoi para n = 4 mostrando todos los pasos seguidos por el algoritmo, para esto:

* Debe compartir pantalla con el entrevistador
* Cree un fork de este repositorio
* Desarrolle su implementación en Python 3.
* Haga commit y push al menos 2 veces durante el tiempo de la entevista
* Imprima cada paso del algoritmo en la pantalla como por ejemplo

        Borigen)      4, 3
        Bintermedia)  2
        Bdestino)     1



# Descripción del problema

El juego, en su forma más tradicional, consiste en tres varillas verticales. En una de las varillas se apila un número indeterminado de discos (elaborados de madera) que determinará la complejidad de la solución, por regla general se consideran ocho discos. Los discos se apilan sobre una varilla en tamaño decreciente. No hay dos discos iguales, y todos ellos están apilados de mayor a menor radio en una de las varillas, quedando las otras dos varillas vacantes. El juego consiste en pasar todos los discos de la varilla ocupada (es decir la que posee la torre) a una de las otras varillas vacantes. Para realizar este objetivo, es necesario seguir tres simples reglas:

* Sólo se puede mover un disco cada vez.
* Un disco de mayor tamaño no puede descansar sobre uno más pequeño que él mismo.
* Sólo puedes desplazar el disco que se encuentre arriba en cada varilla.

![hanoi](https://upload.wikimedia.org/wikipedia/commons/6/60/Tower_of_Hanoi_4.gif)
