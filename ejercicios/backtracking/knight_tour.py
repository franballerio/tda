SALTOS = [
    (2,1), (2,-1), (-2,1), (-2,-1),
    (1,2), (1,-2), (-1,2), (-1,-2)
]

def valid_mov(fila, columna, casilleros):
    return (0 <= fila < 5) and (0 <= columna < 5) and (not casilleros[fila][columna])

def back(fila: int, columna: int, casilleros: list[list[bool]], movimientos: list[tuple[int, int]]):
    # PRIMERO SIEMPRE EL CAMBIO DE ESTADO
    movimientos.append((fila, columna))
    casilleros[fila][columna] = True

    if len(movimientos) == 25:
        return True

    # movimientos posibles
    for df, dc in SALTOS:
        if (valid_mov(fila+df, columna+dc, casilleros)) and back(fila+df, columna+dc, casilleros, movimientos):
            return True

    # BACKTRACING REAL
    movimientos.pop()
    casilleros[fila][columna] = False
    return False

def knight(fila: int, columna:int):
    movs: list[tuple[int, int]] = []
    casilleros: list[list[bool]] = [[False for _ in range(5)] for _ in range(5)]

    if back(fila, columna, casilleros, movs):
        return movs

if __name__ == "__main__":
    print(knight(2,4))
