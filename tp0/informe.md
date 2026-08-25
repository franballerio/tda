# INFORME TP0 - Francisco Oscar Ballerio

### Descripcion del codigo dado
La solucion al ejercicio esta compuesta por dos funciones: esPrimo y prog
- esPrimo recibe un numero entero n y busca la cantidad de divisores de este en el conjunto de numeros enteros [2, n-1] recorriendo cada elemento. Si esta cantidad es 0 significa que el numero es primo y de tener al menos 1 divisor, este numero no es primo.
- prog muestra el tiempo que tarda en imprimir por pantalla los cuartetos de numeros primos encontrados usando un bucle que va desde 11 hasta 1000000 y con cada iteracion llama a esPrimo para verificar si el numero y sus 3 hermanos son primos.

### Complejidad Temporal Pre Modificacion
- esPrimo loopea desde 2 hasta n-1, es decir, tiene una complejidad de O(n)
- prog tiene una complejidad de O(n^2) ya que llama a esPrimo para cada numero en el rango [11, 1000000]

### Limitaciones en el algoritmo dado
- esPrimo:
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
  - Cada vez que se encuentra un cuarteto, se imprime. Lo que genera operaciones de I/O que realentizan la busqueda de los mismos.

## Diseño y Mejora del Algoritmo

### Supuestos y Explicaciones Teoricas

Excluding the first prime quadruplet, the shortest possible distance between two quadruplets {p, p + 2, p + 6, p + 8} and {q, q + 2, q + 6, q + 8} is q − p = 30. The first occurrences of this are for p = 1006301, 2594951, 3919211, 9600551, 10531061, ... (OEIS: A059925).
https://en.wikipedia.org/wiki/Prime_quadruplet#Prime_k-tuples
