# (★★★) Un bodegón tiene una única mesa larga con W lugares.
# Hay una persona en la puerta que anota los grupos que quieren sentarse a comer,
# y la cantidad de integrantes que conforma a cada uno. Para simplificar su trabajo,
# se los anota en un vector P donde P[i] contiene la cantidad de personas que integran el grupo i,
# siendo en total n grupos. Como se trata de un restaurante familiar,
# las personas sólo se sientan en la mesa si todos los integrantes de su grupo pueden sentarse.
# Implementar un algoritmo que, mediante programación dinámica,
# obtenga el conjunto de grupos que ocupan la mayor cantidad de espacios en la mesa
# (o en otras palabras, que dejan la menor cantidad de espacios vacíos).
# Indicar y justificar la complejidad del algoritmo.

def w_table(w: int, n: int, grupos: list[int]):
    opts = [[0 for _ in range(w+1)] for _ in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,w+1):
            # el grupo entra en la mesa
            if grupos[i-1] <= j:
                opts[i][j] = max(opts[i-1][j], grupos[i-1] + opts[i-1][j-grupos[i-1]])
            else:
                opts[i][j] = opts[i-1][j]

    elegidos = [False] * n
    j = w
    for i in range(n,0,-1):
        # el grupo fue elegido
        if opts[i][j] != opts[i-1][j]:
            elegidos[i-1] = True
            j = j - grupos[i-1]

    print(opts)
    return opts[n][w], elegidos

# (0, [2, 3, 5], 0, "Mesa de tamaño 0"),
# (10, [], 0, "Sin grupos en espera"),
# (4, [5, 6, 8], 0, "Ningún grupo entra"),
# (20, [3, 4, 5], 12, "Todos entran con holgura"),
# (10, [6, 5, 5], 10, "Trampa Greedy (más grandes primero)"),
# (10, [1, 2, 8], 10, "Trampa Greedy (más chicos primero)"),
# (15, [2, 4, 7, 9], 15, "Llenado exacto salteando elementos"),
# (13, [4, 6, 8], 12, "Sobrante inevitable (deja 1 lugar vacío)"),
# (11, [3, 3, 3, 3], 9, "Elementos repetidos"),

if __name__ == "__main__":
    w, grupos = 11, [3, 3, 3, 3]
    n = len(grupos)
    print(w_table(w, n, grupos))
