# INFORME TP0 - Francisco Oscar Ballerio

### Descripcion del codigo dado
La solucion al ejercicio esta compuesta por dos funciones: esprimo y prog
- esPrimo recibe un numero entero n y busca la cantidad de divisores de este en el conjunto de numeros enteros [2, n-1] recorriendo cada elemento. Si esta cantidad es 0 significa que el numero es primo y de tener al menos 1 divisor, este numero no es primo.
- prog muestra el tiempo que tarda en imprimir por pantalla los cuartetos de numeros primos encontrados usando un bucle que va desde 11 hasta 1000000 y con cada iteracion llama a esPrimo para verificar si el numero y sus 3 hermanos son primos.

### Complejidad Temporal Pre Modificacion
- esPrimo loopea desde 2 hasta n-1, es decir, tiene una complejidad de O(n)
- prog tiene una complejidad de O(n^2) ya que llama a esPrimo para cada numero en el rango [11, 1000000]

### Limitaciones en el algoritmo dado
- esprimo:
  - Recorre todos los numeros hasta n-1.
  - El bucle while es menos eficiente que un for.
  - Cuenta la cantidad de divisores que tiene el numero.
  - Compara si la cantidad de divisores es 0 para devolver algo cuando podria devolver directamente la comparacion, pues devuelve un bool.

- prog:
  - El bucle recorre todos los numeros de 11 a 1000000. Lo que genera:
    - Se saltea el primer cuarteto de primos.
    - Chequea si un numero es primo varias veces.
    - Sobrepasa la decena. ej.  
    i = 11 --> esprimo(11) and esprimo(13) and esprimo(17) and esprimo(19)  
    i = 13 --> esprimo(13) and esprimo(15) and esprimo(19) and esprimo(21)  
  - Cada vez que se encuentra un cuarteto, se imprime. Lo que genera operaciones de I/O que realentizan la busqueda de los mismos. Imprimir causa que el OS tenga que manejar operaciones de I/O, llamadas al kernel y cambios de contexto para poder hacerlo en cada iteración.  

## Diseño y Mejora del Algoritmo

### Optimizando esprimo
1. De bucle while pasaremos a usar un for que directamente ejecuta la iteración en C. while requiere una condición que se verifique en cada iteración con Python.

2. De la mano del cambio del for, agregamos un range(inicio, fin, salto) que devuelve una lista con el intervalo [inicio, fin].

3. Buscamos divisores entre 2 y $\sqrt{x}$, pues si n = a * b entonces alguno de los dos es menor o igual a $\sqrt{x}$. En este caso lo que queremos es encontrar al menos 1 divisor para n, entonces si en [1, $\sqrt{n}$] no encontramos ninguno, en [$\sqrt{n}$, n-1] tampoco habra. Pues si a,b alguno es mayor a $\sqrt{n}$ entonces necesariamente el otro debe se menor a $\sqrt{n}$.
De la mano de este cambio viene el uso de la biblioteca integrada *math* para calcular la raíz. Esta implementa el calculo y el casteo a int en C.

4. Si al menos un numero de [1, $\sqrt{n}$] divide a n, entonces no es primo. Por eso al encontrar un divisor cortamos el bucle.

5. División optimizada:  
> Cualquier número entero mayor a 3 puede representarse algebraicamente bajo una de las formas $6k$, $6k+1$, $6k+2$, $6k+3$, $6k+4$ o $6k+5$ (para $k \ge 1$):
> * Las formas $6k$, $6k+2$ y $6k+4$ son pares (divisibles por 2), por lo que son números compuestos.
> * La forma $6k+3$ es divisible por 3, siendo también compuesta.
> * Las únicas formas restantes son $6k+1$ y $6k+5$, donde $6k+5$ equivale algebraicamente a $6(k+1)-1$, quedando ambas cubiertas bajo el patrón $6k \pm 1$.
> Dado que los números divisibles por 2 o 3 se pueden descartar en una verificación inicial (en este caso los obviamos por conveniencia del algoritmo), para determinar la primalidad basta con evaluar únicamente los divisores de la forma $6k \pm 1$ hasta el límite $\sqrt{n}$ (GeeksforGeeks, 2026).  
Esto nos permite optimizar el algoritmo `esPrimo` y reducir significativamente la cantidad de operaciones necesarias.  
  
Finalmente lo mejor que se pudo mejorar la complejidad de este algoritmo es O($\sqrt{n}$).

### Optimizando prog

1. Restricción del espacio de búsqueda para cuartetos de primos:
> Un cuarteto de números primos es un conjunto de la forma $\{p, p+2, p+6, p+8\}$. A excepción del primer cuarteto $(\{5, 7, 11, 13\})$, todo cuarteto con $p > 5$ cumple con las siguientes propiedades aritméticas:
> * Ninguno de sus elementos puede ser divisible por 2, 3 o 5.
> * En aritmética modular, esto restringe la posición del primer elemento a una única clase de congruencia módulo 30 ($2 \times 3 \times 5 = 30$), específicamente $p \equiv 11 \pmod{30}$.
> Como consecuencia, la distancia mínima entre el inicio de dos cuartetos consecutivos $\{p, \dots\}$ y $\{q, \dots\}$ es $q - p = 30$, y toda separación entre candidatos válidos debe ser forzosamente un múltiplo de 30 (*Prime quadruplet* (Wikipedia), s.f.). 

Esta propiedad permite optimizar el algoritmo de búsqueda, descartando la evaluación de valores intermedios y avanzando las iteraciones en saltos de 30 (o evaluando únicamente candidatos $p \equiv 11 \pmod{30}$).

2. Para solucionar la realentización de I/O metemos los candidatos en una lista de cuatruplas (i, i+2, i+6, i+8) para imprimirlas todas juntas luego de encontrar *todos* los cuartetos.

3. El crear la lista de cuartetos inline aumenta la performance del código. La implementación de este método es en CPython.

## Pseudocódigo

### esprimo
recibo numero
limite = raiz_cuadrada(numero)
para cada num (desde 5, hasta limite, incrementando 6) {
  si resto(n / num) == 0 o si resto(n / num + 2) == 0 {
    devuelvo Falso
  }
}
devuelvo verdadero

### prog
resultados = lista[tupla(int,int,int,int)]
para cada i (desde 11, hasta 1000000, incrementando 30) {
  si esprimo(i) y esprimo(i + 2) y esprimo(i + 6) y esprimo(i + 8) {
    lista.agregar(tupla(i, i+2, i+6, i+8))
  }
}
para cada tupla de resultados {
  imprimir tupla
}
imprimir tiempo de ejecucion

## Referencias

GeeksforGeeks. (2026, 25 de agosto). *Program for prime number check*. https://www.geeksforgeeks.org/dsa/check-for-prime-number/

Prime quadruplet. (s.f.). En *Wikipedia*. Recuperado el 26 de agosto de 2026, de https://en.wikipedia.org/wiki/Prime_quadruplet#Prime_k-tuples
