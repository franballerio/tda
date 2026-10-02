# Parser del archivo generado por crear_mochila.py
#
# Formato del archivo:
#   linea 1: capacidad de la mochila (W)
#   lineas siguientes: pares "peso,beneficio" de cada elemento
#
# Devuelve la tupla (v, p, n, w) que espera estrategias/pd/mochila.py:
#   v: lista de valores (beneficios)
#   p: lista de pesos
#   n: cantidad de elementos
#   w: capacidad de la mochila


def parsear_mochila(archivo: str) -> tuple[list[int], list[int], int, int]:
    with open(archivo, "r", encoding="utf-8") as arch:
        lineas = [linea.strip() for linea in arch if linea.strip()]

    w = int(lineas[0])

    p: list[int] = []
    v: list[int] = []
    for i, linea in enumerate(lineas[1:], start=2):
        partes = linea.split(",")
        p.append(int(partes[0]))
        v.append(int(partes[1]))

    n = len(p)
    return v, p, n, w


# if __name__ == "__main__":
#     v, p, n, w = parsear_mochila("mochila10.txt")
#     print(f"elementos: {n}")
#     print(f"capacidad: {w}")
#     print(f"suma pesos: {sum(p)}")
#     print(f"suma beneficios: {sum(v)}")
