from collections import deque

class Graph:
    def __init__(self, nodes: set[int], edges: dict[int, list[int]]):
        self.nodes = nodes
        self.edges = edges

def bfs(g, node):
    q = deque([node])
    visited = [node]

    while q:
        actual = q.popleft()
        for neigh in g[actual]:
            if neigh not in visited:
                visited.append(neigh)
                q.append(neigh)
    return visited

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print(bfs(graph, 'A'))
