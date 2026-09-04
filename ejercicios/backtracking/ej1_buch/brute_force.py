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

def es_valido(sub: list[int], neighbors: list[tuple[int, int]]):
    for u, v in neighbors:
        if u in sub and v in sub:
            return False
    return True

def sub_n_recu(nodes: list[int], neighbors: list[tuple[int, int]], n: int, index: int = 0, sub: list[int] = []) -> bool:
    # if (len(sub) >= n):
    #     return False

    if len(sub) == n or index >= len(nodes):
        return len(sub) == n and es_valido(sub, neighbors)

    node = nodes[index]
    sub.append(node)
    if sub_n_recu(nodes, neighbors, n, index + 1, sub):
        return True

    _ = sub.pop()
    return sub_n_recu(nodes, neighbors, n, index + 1, sub)

def sub_n(graph: Graph, n: int):
    t1 = time.time()
    res = sub_n_recu(graph.nodes, graph.neighbors, n)
    t2 = time.time()
    print(res, t2 - t1)


graph = Graph(
            nodes=list(range(25)),
            neighbors=[(0, i) for i in range(1, 25)] + [
                (i, i + 1 if i < 24 else 1) for i in range(1, 25)
            ]
        )
sub_n(graph, 12)
