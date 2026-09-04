def no_adyacentes(grafo: list[tuple[int, int]], solucion: list[int]):
    for vertice1 in solucion:
        for vertice2 in solucion:
            tupla: tuple[int, int] = (vertice1, vertice2)
            if (tupla in grafo):
                return False
    print(solucion)
    return True

def no_adyacentesV2(grafo: list[tuple[int, int]], solucion: list[int]):
    for u, v in grafo:
        if u in solucion and v in solucion:
            return False
    return True

# Quiero guardar k elementos en un grafo de n vertices.
# Pero con la condicion de que ninguno de los n vertices sean adyacentes entre si.
# Fuerza Bruta:
def independent_set(vertices: list[int], k: int, grafo: list[tuple[int, int]], elegidos: list[int] = None, index: int = 0) -> bool:
    if elegidos is None:
        elegidos = []

    if len(vertices) == index:
        return len(elegidos)>=k and no_adyacentes(grafo, elegidos)

    candidato = vertices[index]

    # incluyo al vertice
    elegidos.append(candidato)
    if independent_set(vertices, k, grafo, elegidos, index + 1):
        return True

    # no incluyo al vertice
    pop = elegidos.pop()
    return independent_set(vertices, k, grafo, elegidos, index + 1)
