# Tenemos un negocio con sede en Londres y California
# Dados 2 listados con los costos operativos de atender en cada sede, debemos conseguir
# el gasto minimo posible, pudiendo atender en uno u otro en el mes actual.
# Obviamente al cambiar de locacion de un mes a otro tendremos un costo M por mudanza.
#
# Lo primero que se nos ocurre es un enfoque greedy, que ve mes a mes cual es el costo minimo
# teniendo en cuenta costos de mudanza.
#
# La forma correcta es forzar trabajar en una y la otra, trackeando esto con 2 arreglos.
# De esta manera exploramos todo el espacio de soluciones, trabajando en una o la otra
# segun que fue mas conveniente. Pues sin sumar complejidad estamos analizando
# todas las posibles variantes.
#
# eq rec:
#   res_L --> fuerzo trabajar en Londres
#   res_C --> fuerzo trabajar en California
#
#       Para el dia i:
#           - res_L[i] = L[i] + min(res_L[i-1], M + res_C[i-1])
#           - res_C[i] = C[i] + min(res_C[i-1], M + res_L[i-1])
#           finalmente: res = min(res_L[n], res_C[n])

def min_cost(l: list[int], c: list[int], m: int, n: int) -> tuple[int, list[int], list[int]]:
    if n == 0:
        return (0,[0],[0])

    res_c = [0] * (n)
    res_l = [0] * (n)

    # Casos Base --> forzando trabajar en una ciudad
    res_l[0] = l[0]
    res_c[0] = c[0]

    for i in range(1,n):
        res_l[i] = l[i] + min(res_l[i-1], m + res_c[i-1])
        res_c[i] = c[i] + min(res_c[i-1], m + res_l[i-1])

    return (min(res_l[n-1], res_c[n-1]), res_l, res_c)


# Reconstruimos la solucion para ver que secuencia debemos seguir
def min_cost_back(res_l, res_c, l, c, n):
    res = []

    ciudad_actual = ""
    if res_c[n-1] < res_l[n-1]:
        ciudad_actual = 'California'
    else:
        ciudad_actual = 'Londres'

    res.append(ciudad_actual)

    for i in range(n - 1, 0, -1):
        if ciudad_actual == 'California':
            if res_c[i] == c[i] + res_c[i-1]:
                ciudad_actual = 'California'
            else:
                ciudad_actual = 'Londres'
        else:
            if res_l[i] == l[i] + res_l[i-1]:
                ciudad_actual = 'Londres'
            else:
                ciudad_actual = 'California'
        res.append(ciudad_actual)

    res.reverse()
    return res

if __name__ == "__main__":
    l = [5, 4, 30, 30, 30]
    c = [20, 20, 5, 5, 5]
    m = 10
    n = 5
    minim, res_l, res_c = min_cost(l, c, m, n)
    print(minim, res_l, res_c)
    print(min_cost_back(res_l, res_c, l, c, n))
