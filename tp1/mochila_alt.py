# Queremos meter en una mochila la cantidad B de beneficio, con el menor peso posible.
# Contamos con N elementos N_i = [Peso_i, Valor_i]
#
# Como siempre en un problema combinatorio vamos a tener 2 opciones:
#   - Si uso el elemento
#   - No uso el elemento
#
# Pero que nos garantiza que este elemento N_i no va mejor con otra combinacion de elementos
# que podriamos no haber considerado?
#       Lo resolvemos pensando el problema en 2 dimensiones.
#       Para este N_i elemento elijo el minimo entre mis 2 opciones, pero con una magia mas:
#           - si lo uso --> considero: Valor_i + opt(N - 1, B - Valor_i)
#           - no lo uso --> considero: opt(N - 1, B)
#
#       Esto nos garantiza que los optimos anteriores chequedos son realmente
#       la mejor opcion que podriamos considerar.

import parser_mochila


def mochila(valores: list[int], pesos:list[int], cant_elems: int, beneficio: int):
    inf = float('inf')

    memo = []
    for i in range(cant_elems + 1):
        # no inicializamos en 0, pues estamos buscando el minimo.
        # al tener nuestros valores >= 1, nunca obtendremos algo < 0
        # por ende el 0 siempre ganaria en nuestra eq de recurrencia
        memo.append([inf] * (beneficio + 1))

    for i in range(cant_elems + 1):
        # conseguir beneficio 0 cuesta 0
        memo[i][0] = 0

    for elem in range(1, cant_elems + 1):
        valor_actual: int = valores[elem - 1]
        peso_actual: int = pesos[elem - 1]

        for b in range(1, beneficio + 1):
            # usamos max(0, b-valor_actual) pues queremos al menos B de beneficio
            # si valor actual > B entonces al restarlo obtendriamos un indice negativo
            # lo que romperia el codigo y el problema
            memo[elem][b] = min((peso_actual + memo[elem-1][max(0, b-valor_actual)]), memo[elem-1][b])

    return memo[cant_elems][beneficio]

if __name__ == "__main__":
    v,p,n,w = parser_mochila.parsear_mochila("mochila10.txt")
    res = mochila(v,p,n,w)
    print(res)
