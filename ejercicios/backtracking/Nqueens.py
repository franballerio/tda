# Queremos colocar N reinas en un tablero de NxN casillas (ajedrez like)

# en cada fila podremos colocar una reina, entonces trackeamos en numero
# de columna en el que ubicamos la reina en una lista con cada posicion como
# la fila correspondiente

# la recursion sera en las filas y dentro veremos si podemos colocar la reina
# en esa fila

def not_valid_queen(row, col, queen_row, queen_col):
    return (row == queen_row or col == queen_col or row+col == queen_row+queen_col or row-col == queen_row-queen_col)


def n_queens(n):
    queens = [999] * n

    def back(queens, r):
        if r == n:
            return True

        for col in range(n):
            valida = True
            for queen_row in range(r):
                if not_valid_queen(r, col, queen_row, queens[queen_row]):
                    valida = False

            if (valida):
                queens[r] = col
                if back(queens, r + 1):
                    return True

        return False

    if back(queens, 0):
        return queens

if __name__ == "__main__":
    print(n_queens(20))
