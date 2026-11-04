# Vamos a ver si un grafo es bipartito.
# Un grafo es bipartito si se pueden crear 2 independent sets X e Y, donde
# cada vertice de X se conecta con uno de Y, y viceversa. 
# Ademas de que ningun vertice de X o Y conecta con uno de su mismo set.

class Graph:
    def __init__(self, g: dict[int, list[int]]):
        self.edges = g

# La complejidad de este algoritmo es polinomial. Pues recorre todos los vertices una vez + todas las aristas
def bigraph(g: Graph):
    colors = {nodo: 0 for nodo in g.edges}
    stack = []
    
    for v in g.edges:
        # vertice ya visitado
        if colors[v] != 0:
            continue

        stack.append(v)
        colors[v] = 1

        while len(stack) > 0:
            u = stack.pop()
            for neigh in g.edges[u]:
                if colors[u] == colors[neigh]:
                    return False
                if colors[neigh] == 0:
                    colors[neigh] = -colors[u]
                    stack.append(neigh)
    return True