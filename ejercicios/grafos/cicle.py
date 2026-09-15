# Verificamos si un grafo no dirigido tiene ciclos

class Graph:
    def __init__(self, g: dict[int, list[int]]):
        self.edges = g

    def has_cicles(self) -> bool:
        visited: set[int] = set()
        nodes = self.obtener_vertices()
        edges = self.edges

        # para verificar si el ciclo existe, necesito trackear que nodo fue el que llamo a la recursion
        # de este modo si alguno de los nodos hijos de ese arbol
        def dfs_cicles(current, parent) -> bool:
            # trackeamos los nodos ya visitados metiendolos en el set
            visited.add(current)
            for neigh in self.edges.get(current, set()):
                # esta condicion es la clave para ver si existe o no un ciclo
                # Caso 1: Rama no visitada -> descender en profundidad
                if neigh not in visited:
                    if dfs_cicles(neigh, current):
                        return True
                # Caso 2: Rama ya visitada -> ciclo si no es el nodo de procedencia
                elif neigh != parent:
                    return True
            return False

        for node in nodes:
            if node not in visited and dfs_cicles(node, None):
                    return True

        return False

    def obtener_vertices(self) -> list[int]:
        return list(self.edges.keys())

    def adyacentes(self, nodo) -> list[int]:
        return list(self.edges.get(nodo, []))

def encontrar_ciclo(g: Graph) -> list[int]:
    '''
    Devuelve una lista de vertices que conforman el ciclo. En el segundo ejemplo,
    debería devolver [A, B, C] (o [B, C, A], etc...).
    Si no hay ciclo, debe devolver None.
    '''
    nodes = g.obtener_vertices()
    visited: set[int] = set()
    stack: list[int] = []

    # para verificar si el ciclo existe, necesito trackear que nodo fue el que llamo a la recursion
    # de este modo si alguno de los nodos hijos de ese arbol
    def dfs_cicles(current, parent) -> list[int] | None:
        # trackeamos los nodos ya visitados metiendolos en el set
        visited.add(current)
        # ahora trackeamos los nodos que estan en el recorrido actual
        stack.append(current)
        for neigh in g.adyacentes(current):
            # esta condicion es la clave para ver si existe o no un ciclo
            # Caso 1: Rama no visitada -> descender en profundidad
            if neigh not in visited:
                cycle = dfs_cicles(neigh, current)
                if cycle is not None:
                    return cycle
            # Caso 2: Rama ya visitada -> ciclo si no es el nodo de procedencia
            elif neigh != parent:
                idx = stack.index(neigh)
                return stack[idx:]
        stack.pop()
        return None

    for node in nodes:
        if node not in visited:
            cycle = dfs_cicles(node, None)
            if cycle is not None:
                return cycle

    return []

A = 1
B = 2
C = 3
D = 4

if __name__ == "__main__":
    g = Graph({A:[B], B:[C], C:[D], D:[B]})
    cicles = g.has_cicles()
    print(cicles)
    print(encontrar_ciclo(g))
