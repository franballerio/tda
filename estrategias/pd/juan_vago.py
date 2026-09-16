# Juan es freelancer. Juan tiene muchas ofertas laborales pero pocas ganas de trabajar.
# Juan tiene que organizar su semana y ver que dias trabajar. Pero se niega a trabajar 2 dias seguidos.
#
# Como organiza su semana si estos son los trabajos que tiene?
#               L   Ma  Mi  J   V
# ganancias = [100, 20, 30, 40, 50]
#
# La estrategia sera:
#   - Casos Base:
#       > 1 dia (dia 0) --> ganancias[0]
#       > 2 dias --> max(ganancias[0], ganancias[1])
#   - eq de recurrencia:
#       f(n) {
#           n == 0 devuelvo ganancias[0]
#           n == 1 devuelvo max(ganancias[0], ganancias[1])
#           si n >= 2 entonces
#           max( no trabajo ese dia -> f(n-1), trabajo ese dia (inhabilito el anterior) f(n-2) + ganancias[n] )
#       }
#
# Usaremos una estrategia bottom - up

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


# Ahora queremos saber que dias son los que juan decidio trabajar.
# Para ello reutilizamos la eq de recurrencia recorriendo la lista de optimos en reversa

def juan_vago_dias(optimos: list[int], ganancias: list[int]) -> list[str]:

    semana: dict[int, str] = {
        0: "Lunes",
        1: "Martes",
        2: "Miercoles",
        3: "Jueves",
        4: "Viernes",
        5: "Sabado",
        6: "Domingo"
    }
    dias = []
    idx: int = len(ganancias) - 1

    while idx >= 0:
        optimo_ayer: int = optimos[idx - 1] if idx > 0 else 0
        optimo_ante_ayer: int = optimos[idx - 2] if idx > 1 else 0
        ganancia_hoy: int = ganancias[idx]

        if optimo_ante_ayer + ganancia_hoy > optimo_ayer:
           dias.append(semana[idx])
           idx -= 2
        else:
            idx -= 1

    dias.reverse()
    return dias

if __name__ == "__main__":
    ganancias = [100, 20, 30, 40, 50]
    optimos = juan_vago(ganancias)
    print(optimos)
    print(juan_vago_dias(optimos, ganancias))
