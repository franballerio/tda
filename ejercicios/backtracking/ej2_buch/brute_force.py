from modulefinder import test
import time

# (★★) Implementar un algoritmo que reciba un grafo y
# un número n que, utilizando backtracking,
# indique si es posible pintar cada vértice con n colores
# de tal forma que no hayan dos vértices adyacentes con el mismo color.
#
# buscar todas las combinaciones posibles de colores para cada vértice

class Graph:
    def __init__(self, nodes: list[int], neighbors: list[tuple[int, int]]):
        self.nodes = nodes
        self.neighbors = neighbors

def colores_validos(nodes_colors: dict[int, int], neighbors: dict[int, set[int]], colors: set[int]) -> bool:
    for node in nodes_colors:
        for neighbor in neighbors[node]:
            if nodes_colors[neighbor] == nodes_colors[node]:
                return False
    return True

def colors_fb(nodes: list[int], neighbors: dict[int, set[int]], n: int, index: int = 0, res: dict[int, int] = None, colors: set[int] = None) -> bool:
    if res is None:
        res: dict[int, int] = {}

    if colors is None:
        colors = set()

    if index >= len(nodes):
        return colores_validos(res, neighbors, colors)

    node = nodes[index]
    for color in range(n):
        res[node] = color
        colors.add(color)
        if (colors_fb(nodes, neighbors, n, index + 1, res, colors)):
            _ = colors.discard(color)
            return True

    return False

def colors(graph: Graph, n: int) -> bool:
    # creamos un diccionario de adyacencias
    edges: dict[int, set[int]] = {u: set() for u in graph.nodes}
    for u, v in graph.neighbors:
        edges[u].add(v)
        edges[v].add(u)

    return colors_fb(graph.nodes, edges, n)

def test_calibrado(fn_colorear):
    # -------------------------------------------------------------------------
    # CASO A: Ciclo impar C_19 con n = 2 colores
    # - Espacio: 2^19 = 524.288 combinaciones en las hojas.
    # - Tu fuerza bruta: va a evaluar medio millón de veces la función
    #   colores_validos(). Vas a sentir una pausa clara de ~2 a 4 segundos.
    # - Backtracking con poda: debería resolverlo en menos de 0.001 segundos.
    # -------------------------------------------------------------------------
    c19 = Graph(
        nodes=list(range(19)),
        neighbors=[(i, (i + 1) % 19) for i in range(19)],
    )

    print("Midiendo C_19 con n=2 (debería dar False)...")
    t0 = time.perf_counter()
    resultado = fn_colorear(c19, 2)
    t1 = time.perf_counter()

    assert resultado == False
    print(f"Resultado correcto en {t1 - t0:.3f} segundos.")


# -------------------------------------------------------------------------
# CASO B: Rueda W_11 (Ciclo C_11 + 1 centro) con n = 3 colores
# - Total nodos: 12 nodos.
# - Espacio: 3^12 = 531.441 combinaciones.
# - El ciclo impar C_11 necesita 3 colores; el centro fuerza un 4to.
# - Fuerza bruta: tarda entre 3 y 5 segundos.
# -------------------------------------------------------------------------
def test_rueda_calibrada(fn_colorear):
    n_ciclo = 11
    centro = 11
    aristas = [(i, (i + 1) % n_ciclo) for i in range(n_ciclo)] + [
        (centro, i) for i in range(n_ciclo)
    ]
    w11 = Graph(nodes=list(range(12)), neighbors=aristas)

    print("Midiendo W_11 con n=3 (debería dar False)...")
    t0 = time.perf_counter()
    resultado = fn_colorear(w11, 3)
    t1 = time.perf_counter()

    assert resultado == False
    print(f"Resultado correcto en {t1 - t0:.3f} segundos.")

if __name__ == "__main__":
    test_calibrado(colors)
    test_rueda_calibrada(colors)
