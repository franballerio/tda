# INFORME TP0
Francisco Oscar Ballerio

## Descripcion del codigo dado
La solucion al ejercicio esta compuesta por dos funciones: esPrimo y prog
1. esPrimo recibe un numero entero n y busca la cantidad de divisores de este en el conjunto de numeros enteros [2, n-1] recorriendo cada elemento. Si esta cantidad es 0 significa que el numero es primo y de tener al menos 1 divisor, este numero no es primo.
2. prog muestra el tiempo que tarda en imprimir por pantalla los cuartetos de numeros primos encontrados usando un bucle que va desde 11 hasta 1000000 y con cada iteracion llama a esPrimo para verificar si el numero y sus 3 hermanos son primos.

## Complejidad Temporal Pre Modificacion
- esPrimo loopea desde 2 hasta n-1, es decir, tiene una complejidad de O(n)
- prog tiene una complejidad de O(n^2) ya que llama a esPrimo para cada numero en el rango [11, 1000000]

##
