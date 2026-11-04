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

# Quiero guardar k elementos en un grafo de n vertices.
# Pero con la condicion de que ninguno de los n vertices sean adyacentes entre si.

# Es lo mismo que pedir si existe independent set de k vertices

#####################################
############ FUERZA BRUTA ###########
#####################################
def idps_fb(vertices: list[int], k: int, vecinos: list[tuple[int, int]], elegidos: list[int], index: int = 0) -> bool:
    if elegidos is None:
        elegidos = []

    if len(vertices) == index:
        return len(elegidos) >= k and is_independent_set(vecinos, elegidos)

    candidato = vertices[index]

    # incluyo al vertice
    elegidos.append(candidato)
    if idps_fb(vertices, k, vecinos, elegidos, index + 1):
        return True

    # no incluyo al vertice
    pop = elegidos.pop()
    return idps_fb(vertices, k, vecinos, elegidos, index + 1)

def independet_set_fb(g: Graph, k: int):
    return idps_fb(g.nodes, k, g.neighbors, [], 0)


#####################################
########### BACKTRACKING ############
#####################################
def idps_bt(vertices: list[int], k: int, vecinos: list[tuple[int, int]], elegidos: list[int], index: int = 0) -> bool:
    if elegidos is None:
        elegidos = []

    # PODA 2: como ya verificamos que en elegidos solo haya independent sets de tamano < k
    # cuando sea k sera la solucion
    if (len(elegidos) == k):
        return True

    # PODA 3: si la cantidad de vertices que elegi + los restantes no suman k
    # entonces no puedo encontrar la solucion
    if len(elegidos) + (len(vertices) - index) < k:
       return False

    candidato = vertices[index]

    # incluyo al vertice
    elegidos.append(candidato)

    # PODA 1: cada nuevo vertice debe respetar que elegidos sea un independent set de i+1 elementos
    if is_independent_set(vecinos, elegidos) and idps_bt(vertices, k, vecinos, elegidos, index + 1):
        return True

    # no incluyo al vertice
    _ = elegidos.pop()
    return idps_bt(vertices, k, vecinos, elegidos, index + 1)

def independet_set_bt(g: Graph, k: int):
    return idps_bt(g.nodes, k, g.neighbors, [], 0)


# OPTIMIZADO PARA RPL FIUBA
def is_ids(vecinos, vertices):
    for v in vertices:
        for vecino_v in vecinos[v]:
            if vecino_v in vertices:
                return False
    return True

def idps_bt_rpl(vertices, k, vecinos, elegidos, index) -> bool:
    if elegidos is None:
        elegidos = []

    # PODA 2: como ya verificamos que en elegidos solo haya independent sets de tamano < k
    # cuando sea k sera la solucion
    if (len(elegidos) == k):
        return True

    # PODA 3: si la cantidad de vertices que elegi + los restantes no suman k
    # entonces no puedo encontrar la solucion
    if len(elegidos) + (len(vertices) - index) < k:
       return False

    candidato = vertices[index]

    # incluyo al vertice
    elegidos.append(candidato)

    # PODA 1: cada nuevo vertice debe respetar que elegidos sea un independent set de i+1 elementos
    if is_ids(vecinos, elegidos) and idps_bt_rpl(vertices, k, vecinos, elegidos, index + 1):
        return True

    # no incluyo al vertice
    _ = elegidos.pop()
    return idps_bt_rpl(vertices, k, vecinos, elegidos, index + 1)

def no_adyacentes(g, n):
    elegidos = []
    vertices = g.obtener_vertices()
    adyacentes = {}
    for v in vertices:
        adyacentes[v] = g.adyacentes(v)

    # dentro de la funcion modificamos mejor_candidato
    if not idps_bt_rpl(vertices, n, adyacentes, elegidos, 0):
        elegidos = None
    return elegidos
