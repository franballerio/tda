def juan_vago(ganancias: list[int]) -> list[int]:
    dias: int = len(ganancias)
    optimos: list[int] = [0] * (dias)

    # Casos Base
    optimos[0] = ganancias[0]
    optimos[1] = max(ganancias[0], ganancias[1])

    # n >= 2
    for dia in range(2, dias):
        optimos[dia] = max(optimos[dia - 1], ganancias[dia] + optimos[dia - 2])

    # optimos[dias - 1] --> ganancia maxima que Juan puede conseguir
    return optimos

def dias_trabajados(optimos, ganancias):
    dias = [False] * len(ganancias)

    i = len(ganancias) - 1
    while i >= 0:

        ganancia_prev = optimos[i-2] if i-2 > 0 else 0

        if optimos[i] == ganancia_prev + ganancias[i]:
            dias[i] = True
            i = i - 2
        else:
            i = i - 1

    return dias

if __name__ == "__main__":
    ganancias = [1000, 200, 30, 400, 50]
    optimos = juan_vago(ganancias)
    print(optimos)
    print(dias_trabajados(optimos, ganancias))
