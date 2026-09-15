class Graph:
    def __init__(self, nodes: set[int], edges: dict[int, list[int]]):
        self.nodes = nodes
        self.edges = edges

    def dfs(self) -> set[int]:
        visited: set[int] = set()
        nodes = self.edges
        edges = self.nodes

        def dfs_aux(node, edges, visited) -> None:
            # trackeamos los nodos ya visitados metiendolos en el set
            visited.add(node)
            for neigh in edges.get(node, set()):
                # si ya visitamos un nodo no seguimos recorriendo su camino
                if neigh not in visited:
                    dfs_aux(neigh, edges, visited)

        for node in nodes:
            dfs_aux(node, edges, visited)

        return visited
