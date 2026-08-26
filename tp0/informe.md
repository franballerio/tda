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

### Optimizando esPrimo
1. De bucle while pasaremos a usar un for. Pues el bucle for directamente ejecuta la iteración sobre los números en el rango usando un iterador implementado en C, mientras que el bucle while requiere una condición que se verifique en cada iteración, verificando codigo de Python.

2. 

1. Excluding the first prime quadruplet, the shortest possible distance between two quadruplets {p, p + 2, p + 6, p + 8} and {q, q + 2, q + 6, q + 8} is q − p = 30. The first occurrences of this are for p = 1006301, 2594951, 3919211, 9600551, 10531061, ... (OEIS: A059925).
https://en.wikipedia.org/wiki/Prime_quadruplet#Prime_k-tuples
- Esto nos permite decir que entre un candidato y el siguiente tendremos al menos 30 números no primos entre ellos. Ademas sabiendo que $p>5$ puedo decir que ninguno de los elementos del cuarteto puede ser divisible por 2, 3 o 5 lo que justamente es 30 ($2*3*5=30$) justificando que la distancia entre un candidato y el otro es minimo 30 y siempre sera multiplo de 30.

2. Optimized Square Root Trial Division - O(√n) Time and O(1) Space

    Numbers that are divisible by 2 or 3 are not prime, so we can skip them entirely. To check whether a number is prime, it is sufficient to test only the numbers of the form 6k ± 1 up to √n.

Why all prime greater than 3 can be expressed in the form 6k ± 1?

    The forms 6k, 6k+2 and 6k + 4 are all even and greater than, so they are composite. The form is a multiple of and greater than , so it is composite.
    The form 6K + 3 is a multiple of 3
    The only remaining forms are 6k + 1 and 6K + 5. The form 6K + 5 can can be rewritten as 6(k + 1) - 1, so it is covered under (6k - 1) for k = k + 1.
https://www.geeksforgeeks.org/dsa/check-for-prime-number/#expected-approach-2-optimized-trial-division-method
- Esto nos permite optimizar el algoritmo esPrimo y reducir la cantidad de operaciones necesarias para determinar si un número es primo.
