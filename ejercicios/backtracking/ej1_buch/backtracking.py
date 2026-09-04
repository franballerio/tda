import time

# (★★) Implementar por backtracking un algoritmo que,
# dado un grafo no dirigido y un numero nn menor a ∣V∣,
# devuelva si es posible obtener un subconjunto de n vertices
# tal que ningun par de vertices sea adyacente entre si.
#
# fuerza bruta
#
# buscar todos los subconjuntos de n vertices

class Graph:
    def __init__(self, nodes: list[int], neighbors: list[tuple[int, int]]):
        self.nodes = nodes
        self.neighbors = neighbors

def sub_n_recu(nodes: list[int], neighbors: dict[int, set[int]], n: int, index: int = 0, sub: set[int] = None) -> bool:
    if sub is None:
        sub = set()

    if len(sub) == n:
        return True

    # PODA 1
    # si la cantidad de nodos en la solucion + la cantidad de nodos
    # que falta verificar es menore que n, entonces nunca podremos
    # llegar a una solucion optima
    if len(sub) + (len(nodes) - index) < n:
        return False

    node = nodes[index]

    # PODA 2
    # neighbors[node] & sub devuelve el conjunto interseccion entre los vecinos del nodo que
    # estamos viendo y los nodos ya elegidos en el subconjunto parcial.
    # Osea que si el conjunto interseccion no es vacio, entonces el nodo que estamos viendo
    # no puede ser agregado al subconjunto parcial sin romper la condicion de no vecinos.
    if not (neighbors[node] & sub):
        sub.add(node)
        if sub_n_recu(nodes, neighbors, n, index + 1, sub):
            return True
        # en este paso se aplica el backtracking real, pues volvemos al estado anterior
        # si no nos fue bien inluyendo este nodo
        sub.remove(node)

    return sub_n_recu(nodes, neighbors, n, index + 1, sub)

def sub_n(graph: Graph, n: int):
    t1 = time.perf_counter()
    # Casos borde inmediatos
    if n == 0:
        return True
    if n > len(graph.nodes):
        return False

    # creamos un diccionario de adyacencias
    edges: dict[int, set[int]] = {u: set() for u in graph.nodes}
    for u, v in graph.neighbors:
        edges[u].add(v)
        edges[v].add(u)

    res = sub_n_recu(graph.nodes, edges, n)
    t2 = time.perf_counter()
    print(res, t2 - t1)
    return res


graph = Graph(
            nodes=list(range(25)),
            neighbors=[(0, i) for i in range(1, 25)] + [
                (i, i + 1 if i < 24 else 1) for i in range(1, 25)
            ]
        )
sub_n(graph, 12)
