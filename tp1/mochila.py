import parser_mochila

# Queremos meter en una mochila de capacidad W el mayor valor posible.
# Contamos con N elementos N_i = [Peso_i, Valor_i]
#
# Como siempre en un problema combinatorio vamos a tener 2 opciones:
#   - Si uso el elemento
#   - No uso el elemento
#
# Pero que nos garantiza que este elemento N_i no va mejor con otra combinacion de elementos
# que podriamos no haber considerado?
#       Lo resolvemos pensando el problema en 2 dimensiones.
#       Para este N_i elemento elijo el maximo entre mis 2 opciones, pero con una magia mas:
#           - si lo uso --> considero: Valor_i + opt(N - 1, W - Peso_i)
#           - no lo uso --> considero: opt(N - 1, W)
#
#       Esto nos garantiza que los optimos anteriores chequedos son realmente
#       la mejor opcion que podriamos considerar.

def mochila(valores: list[int], pesos:list[int], cant_elems: int, capacidad_mochila: int):
    memo: list[list[int]] = []
    for i in range(cant_elems + 1):
        memo.append([0] * (capacidad_mochila + 1))

    for elem in range(1, cant_elems + 1):
        valor_actual: int = valores[elem - 1]
        peso_actual: int = pesos[elem - 1]

        for w in range(1, capacidad_mochila + 1):
            if (peso_actual <= w):
                memo[elem][w] = max((valor_actual + memo[elem-1][w-peso_actual]), memo[elem-1][w])
            else:
                memo[elem][w] = memo[elem-1][w]

    return memo[cant_elems][capacidad_mochila]

if __name__ == "__main__":
    v,p,n,w = parser_mochila.parsear_mochila("mochila10.txt")
    res = mochila(v,p,n,w)
    print(res)
