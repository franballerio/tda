class Graph:
    def __init__(self, nodos: list[int], vecinos: list[tuple[int, int]]):
        self.nodes = nodos
        self.neighbors = vecinos


# VERIFICAR
def is_independent_set(vecinos: list[tuple[int, int]], vertices: list[int]):
    # Si ambos vertices, de todos los pares de vertices adyacentes,
    # estan en la lista de vertices recibida: Entonces no es un independent set
    for u, v in vecinos:
        if u in vertices and v in vertices:
            return False
    return True

# PROBLEMA:
# Quiero encontrar el mayor independent set posible en un grafo

# SOLUCION:
# Usamos el mismo algoritmo, pero sin alcanzar un k fijo.
# Recorremos todos los vertices y buscamos un candidato a mejor (mas grande) independent set
# Pues ya sabemos verificar si es independent set y ya tenemos las cotas adecuadas

#####################################
########### BACKTRACKING ############
#####################################
def idps_bt(vertices: list[int], k: int, vecinos: list[tuple[int, int]], elegidos: list[int], index: int, mejor_candidato: list[int]):
    if elegidos is None:
        elegidos = []

    # recorrimos todos los vertices
    if len(vertices) == index and len(elegidos) > len(mejor_candidato):
            mejor_candidato.clear()
            mejor_candidato.extend(elegidos)

    # PODA 2: si la cantidad de vertices que elegi + los restantes no superan nuestro candidato
    # entonces no puedo mejorar la
    cant_vertices_restantes = len(vertices) - index
    if len(elegidos) + cant_vertices_restantes <= len(mejor_candidato) :
       return

    candidato = vertices[index]

    # incluyo al vertice
    elegidos.append(candidato)

    # PODA 1: cada nuevo vertice debe respetar que elegidos sea un independent set de i+1 elementos
    if is_independent_set(vecinos, elegidos) and idps_bt(vertices, k, vecinos, elegidos, index + 1, mejor_candidato):
        return True

    # no incluyo al vertice
    _ = elegidos.pop()
    return idps_bt(vertices, k, vecinos, elegidos, index + 1, mejor_candidato)

def independet_set_bt(g: Graph, k: int):
    mejor_candidato = []
    # dentro de la funcion modificamos mejor_candidato
    idps_bt(g.nodes, k, g.neighbors, [], 0, mejor_candidato)
    return mejor_candidato


# OPTIMIZADO PARA RPL FIUBA
# 
# 
# 
# 


def is_ids(vecinos, vertices):
    for v in vertices:
        for vecino_v in vecinos[v]:
            if vecino_v in vertices:
                return False
    return True
    

def idps_bt(vertices, vecinos, elegidos, index, mejor_candidato):
    if elegidos is None:
        elegidos = []

    # recorrimos todos los vertices
    if len(vertices) == index and  len(elegidos) > len(mejor_candidato):
            mejor_candidato.clear()
            mejor_candidato.extend(elegidos)

    # PODA 2: si la cantidad de vertices que elegi + los restantes no superan nuestro candidato
    # entonces no puedo mejorar la
    cant_vertices_restantes = len(vertices) - index
    if len(elegidos) + cant_vertices_restantes <= len(mejor_candidato) :
       return

    candidato = vertices[index]

    # incluyo al vertice
    elegidos.append(candidato)

    # PODA 1: cada nuevo vertice debe respetar que elegidos sea un independent set de i+1 elementos
    if is_ids(vecinos, elegidos) and idps_bt(vertices, vecinos, elegidos, index + 1, mejor_candidato):
        return True

    # no incluyo al vertice
    _ = elegidos.pop()
    return idps_bt(vertices, vecinos, elegidos, index + 1, mejor_candidato)

def independet_set(g: Graph):
    mejor_candidato = []
    vertices = g.obtener_vertices() 
    adyacentes = {}
    for v in vertices:
        adyacentes[v] = g.adyacentes(v)
    
    # dentro de la funcion modificamos mejor_candidato
    idps_bt(vertices, adyacentes, [], 0, mejor_candidato)
    return mejor_candidato
