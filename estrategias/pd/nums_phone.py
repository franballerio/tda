from ejercicios.grafos.cicle import Graph
# Dado el teclado de un telefono
#        1  2  3
#        4  5  6
#        7  8  9
#           0
# Queremos saber cuantas combinaciones de nums
# de tamano N existen, partiendo desde k -> [0,1,2,3,4,5,6,7,8,9]
# solamente pudiendo teclear los numeros que estan arriba, abajo,
# izq, der del numero actual.
#
# La solucion sera del estilo [cant combinaciones, tecla inicial]
# Como los nums que puedo teclear son los adyacentes al actual, puedo
# representar el teclado como un grafo, donde los nums a los que puedo ir
# son los adyacentes del actual
#        1---2---3
#        |   |   |
#        4---5---6
#        |   |   |
#        7---8---9
#            |
#            0
# Eq de recurr:
#
# f(N, K) = sumatoria(f(N-1,Ki))
#           ki = vecinos(K)
#
# en el codigo usamos un arreglo de listas. que tendra pasos + 1 posiciones (pasos + 1 listas)
# cada lista representa las cantidades de combinaciones que se pueden formar con la cantidad
# de pasos que representa su posicion en la lista principal.
# con pasos = 4
# cada posicion son las combinaciones que puedo hacer con n teclas, empezando desde la tecla cant[n][tecla]
# cant[0] = [0,0,0,0,0,0,0,0,0,0]
# cant[1] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
# cant[2] = [1, 2, 3, 2, 3, 4, 3, 2, 4, 2],
# cant[3] = [4, 6, 8, 6, 8, 13, 8, 7, 9, 7],
# cant[4] = [9, 16, 25, 16, 26, 33, 26, 17, 31, 17]

def phone_nums(graph: Graph, pasos, tecla_inicial):
    cant = [][]
    # Casos Base
    for tecla in range(0, 9):
        cant[0][tecla] = 0
        cant[1][tecla] = 1

    # Construimos las soluciones de atras para adelante
    for paso in range(2, pasos+1):
        # calculamos para cada tecla
        for tecla in range(0,9):
            # contador sera la sumatoria
            contador = 0
            # sumamos las combinaciones de paso - 1 para cada vecino de la tecla actual
            for vecino in graph.adyacentes(tecla):
                contador += cant[paso-1][vecino]
            cant[paso][tecla] = contador

    return cant[pasos][tecla_inicial]
