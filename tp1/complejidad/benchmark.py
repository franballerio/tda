"""
Benchmark de complejidad para el Problema 3 del TP1 (programación dinámica).

Compara empíricamente los dos planteos de programación dinámica pedidos por el
enunciado, tal como se pide: "aplicarlos a diferentes sets de datos obtenidos
con crear_mochila.py ... para comparar la curva de tiempos teórica y real en
ambos algoritmos" y "aplicarlos ambos algoritmos a los mismos sets de datos
para comparar los tiempos de ejecución de ambos algoritmos".

  1. `mochila.py` — planteo tradicional: maximizar el beneficio para una
     capacidad fija W. Tabla de (n+1) x (W+1)  =>  O(n * W).
  2. `mochila_alt.py` — planteo alternativo: minimizar el peso para un beneficio
     fijo B. Tabla de (n+1) x (B+1)  =>  O(n * B).

Instancias: se usan los archivos ya generados con `crear_mochila.py` y guardados
en `complejidad/data/mochila*.txt` (mismos rangos del enunciado: capacidad
W = n * 50, pesos 1-200, beneficios 1-1000). Cada archivo se parsea una sola vez
con `parser_mochila` y **los dos algoritmos reciben exactamente la misma
instancia**; los tamaños medidos salen de los archivos disponibles, así que el
benchmark no genera datos nuevos y es determinístico.

Decisión metodológica: el beneficio fijo del planteo alternativo es la misma
capacidad, B = W = 50 * n. Así las dos tablas tienen el mismo ancho (comparación
pareja memoria/tiempo) y ambos casos son O(n * W) = O(n * B) = O(n^2) para esta
familia de instancias; lo que cambia es la constante. Se chequea además que
B sea alcanzable (suma de beneficios >= B).

Para medir los tiempos se reutiliza `time_algorithm` de `util.py`, tal como se
hace en el notebook de cuadrados mínimos, y el ajuste es por cuadrados mínimos
con `scipy.optimize.curve_fit`. El modelo ajustado es c1 * (n * W) + c2 (y
c1 * (n * B) + c2 para el alternativo), ajustando contra el trabajo real
celdas = n * capacidad de cada archivo; con W = B = 50n ese trabajo es 50 * n^2
y el modelo es cuadrático en n.

Salidas generadas (en este mismo directorio):
  - tiempos_tradicional.csv        (N, capacidad, tiempo_promedio_seg)
  - tiempos_alternativo.csv        (N, capacidad, tiempo_promedio_seg)
  - resumen_ajustes.csv            (coeficientes del ajuste y error cuadrático
    total, útil para armar la tabla en el informe)
  - grafico_tradicional.png        (medición + ajuste O(n*W))
  - grafico_alternativo.png        (medición + ajuste O(n*B))
  - grafico_comparacion.png        (ambos algoritmos, misma escala log-log)
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path
from typing import Callable

import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

BASE_DIR = Path(__file__).resolve().parent
TP1_DIR = BASE_DIR.parent

# `util` vive junto a este script; parser_mochila / mochila / mochila_alt viven
# en la raíz del TP1. Se agregan ambos directorios para poder correr el script
# desde cualquier cwd (python complejidad/benchmark.py).
sys.path[:0] = [str(BASE_DIR), str(TP1_DIR)]

import util  # noqa: E402
from parser_mochila import parsear_mochila  # noqa: E402
from mochila import mochila as mochila_tradicional  # noqa: E402
from mochila_alt import mochila as mochila_alternativo  # noqa: E402

sns.set_theme()

# Instancias ya generadas con crear_mochila.py: data/mochilaN.txt (la primera
# línea del archivo es la capacidad W = N * 50, que además es el beneficio
# fijo B del planteo alternativo).
DATA_DIR = BASE_DIR / "data"

# Corridas por tamaño. util.time_algorithm promedia estos tiempos para bajar el
# error estadístico (el default de util.py es 10; con tablas de hasta
# 1001 x 50001 celdas alcanzan 3 para tener curvas estables).
util.RUNS_PER_SIZE = 3

# instancia por tamaño: n -> (capacidad, pesos, beneficios)
INSTANCIAS: dict[int, tuple[int, list[int], list[int]]] = {}


def descubrir_instancias() -> dict[int, tuple[int, list[int], list[int]]]:
    """
    Carga todos los archivos `data/mochilaN.txt` con `parser_mochila`: el
    nombre del archivo define el tamaño (mochilaN.txt => n) y la primera línea
    la capacidad W, que es a la vez el beneficio fijo B del planteo
    alternativo. Se chequea que B sea alcanzable: si la suma de los beneficios
    fuera menor que B, el planteo alternativo no tendría solución y la
    comparación no tendría sentido.
    """
    if not DATA_DIR.is_dir():
        raise FileNotFoundError(f"No existe el directorio de datos: {DATA_DIR}")

    instancias: dict[int, tuple[int, list[int], list[int]]] = {}
    for archivo in DATA_DIR.glob("mochila*.txt"):
        sufijo = archivo.stem[len("mochila") :]
        if not sufijo.isdigit():
            continue
        n = int(sufijo)
        beneficios, pesos, n_archivo, cap = parsear_mochila(str(archivo))
        if n_archivo != n:
            raise RuntimeError(
                f"{archivo.name}: declara {n_archivo} elementos pero el nombre dice {n}."
            )
        if sum(beneficios) < cap:
            raise RuntimeError(
                f"{archivo.name}: beneficio total {sum(beneficios)} < capacidad (B) {cap}; "
                "el planteo alternativo no tendría solución."
            )
        instancias[n] = (cap, pesos, beneficios)

    if not instancias:
        raise FileNotFoundError(f"Sin instancias en {DATA_DIR} (se esperan archivos mochilaN.txt).")
    return instancias


INSTANCIAS = descubrir_instancias()

# Los tamaños medidos salen de los archivos disponibles en data/.
SIZES: np.ndarray = np.array(sorted(INSTANCIAS), dtype=int)


def get_args(n) -> list:
    """
    Argumentos compartidos por los dos algoritmos: misma instancia, mismo orden
    de parámetros (valores, pesos, cant_elems, capacidad|beneficio).
    Con B = W = la capacidad, las dos firmas se alimentan igual.
    """
    cap, pesos, beneficios = INSTANCIAS[int(n)]
    return [beneficios, pesos, int(n), cap]


def guardar_csv(path: Path, sizes: np.ndarray, tiempos: dict) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["N", "capacidad_W_y_B", "tiempo_promedio_seg"])
        for n in sizes:
            cap = INSTANCIAS[int(n)][0]
            writer.writerow([int(n), cap, tiempos[n]])
    print(f"  CSV guardado en {path.name}")


def ajustar_y_graficar(
    *,
    nombre_archivo: str,
    titulo: str,
    sizes: np.ndarray,
    trabajo: np.ndarray,
    tiempos: dict,
    funcion_ajuste: Callable[..., np.ndarray],
    etiqueta_ajuste: str,
    color_ajuste: str = "r",
) -> tuple[np.ndarray, float]:
    """
    Ajusta `funcion_ajuste` a los tiempos medidos por cuadrados mínimos
    (usando `scipy.optimize.curve_fit`, contra `trabajo` = celdas de tabla),
    grafica la medición contra el tamaño n junto con el ajuste y devuelve los
    coeficientes encontrados junto con el error cuadrático total del ajuste.
    """
    y = np.array([tiempos[n] for n in sizes], dtype=float)
    coeficientes, _ = curve_fit(funcion_ajuste, trabajo, y, maxfev=20000)
    y_ajustada = funcion_ajuste(trabajo, *coeficientes)
    error_cuadratico = float(np.sum((y_ajustada - y) ** 2))

    fig, ax = plt.subplots()
    ax.plot(sizes, y, marker="o", label="Medición")
    ax.plot(sizes, y_ajustada, "--", color=color_ajuste, label=etiqueta_ajuste)
    ax.set_title(titulo)
    ax.set_xlabel("Tamaño de entrada (n)")
    ax.set_ylabel("Tiempo de ejecución (s)")
    ax.legend()
    fig.savefig(BASE_DIR / nombre_archivo, dpi=150, bbox_inches="tight")
    plt.close(fig)

    return coeficientes, error_cuadratico


def graficar_comparacion(*, nombre_archivo: str, titulo: str, series: list[tuple[str, np.ndarray, dict]]) -> None:
    fig, ax = plt.subplots()
    for etiqueta, sizes, tiempos in series:
        ax.plot(sizes, [tiempos[n] for n in sizes], marker="o", label=etiqueta)
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_title(titulo)
    ax.set_xlabel("Tamaño de entrada (n)")
    ax.set_ylabel("Tiempo de ejecución (s)")
    ax.legend()
    fig.savefig(BASE_DIR / nombre_archivo, dpi=150, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    resumen = []

    print(f"Instancias: {DATA_DIR.name}/mochila*.txt (generadas con crear_mochila.py)")
    print(f"Tamaños medidos: {[int(n) for n in SIZES]}")
    print(f"Corridas por tamaño: {util.RUNS_PER_SIZE}")
    for n in sorted(INSTANCIAS):
        cap = INSTANCIAS[n][0]
        print(f"  n={n:4d}  W=B={cap:6d}  beneficio_total={sum(INSTANCIAS[n][2]):7d}")

    # Trabajo de ambos algoritmos en cada tamaño: celdas de la tabla,
    # n * W para el tradicional y n * B para el alternativo (W = B = capacidad).
    trabajo = np.array([int(n) * INSTANCIAS[int(n)][0] for n in SIZES], dtype=float)

    # ------------------------------------------------------------------
    # 1) planteo tradicional (mochila.py): O(n*W), W = 50n
    #    planteo alternativo  (mochila_alt.py): O(n*B), B = 50n
    # ------------------------------------------------------------------
    print("\nMidiendo planteo tradicional (mochila.py, O(n*W)) ...")
    tiempos_tradicional = util.time_algorithm(mochila_tradicional, SIZES, get_args)
    guardar_csv(BASE_DIR / "tiempos_tradicional.csv", SIZES, tiempos_tradicional)

    print("Midiendo planteo alternativo (mochila_alt.py, O(n*B)) ...")
    tiempos_alternativo = util.time_algorithm(mochila_alternativo, SIZES, get_args)
    guardar_csv(BASE_DIR / "tiempos_alternativo.csv", SIZES, tiempos_alternativo)

    # Mismo modelo teórico para ambos (cantidad de celdas recorridas),
    # distinta constante.
    def f_celdas(celdas, c1, c2):
        return c1 * celdas + c2

    c_trad, error_trad = ajustar_y_graficar(
        nombre_archivo="grafico_tradicional.png",
        titulo="Mochila tradicional (mochila.py) — ajuste $O(n \\cdot W)$",
        sizes=SIZES,
        trabajo=trabajo,
        tiempos=tiempos_tradicional,
        funcion_ajuste=f_celdas,
        etiqueta_ajuste="Ajuste $O(n \\cdot W)$",
    )
    c_alt, error_alt = ajustar_y_graficar(
        nombre_archivo="grafico_alternativo.png",
        titulo="Mochila alternativa (mochila_alt.py) — ajuste $O(n \\cdot B)$",
        sizes=SIZES,
        trabajo=trabajo,
        tiempos=tiempos_alternativo,
        funcion_ajuste=f_celdas,
        etiqueta_ajuste="Ajuste $O(n \\cdot B)$",
        color_ajuste="g",
    )
    graficar_comparacion(
        nombre_archivo="grafico_comparacion.png",
        titulo="Mochila: planteo tradicional vs planteo alternativo (mismas instancias)",
        series=[
            ("mochila.py — O(n*W)", SIZES, tiempos_tradicional),
            ("mochila_alt.py — O(n*B)", SIZES, tiempos_alternativo),
        ],
    )

    resumen.append({"algoritmo": "mochila_tradicional", "modelo": "c1*n*W + c2", "c1": c_trad[0], "c2": c_trad[1], "error_cuadratico": error_trad})
    resumen.append({"algoritmo": "mochila_alternativo", "modelo": "c1*n*B + c2", "c1": c_alt[0], "c2": c_alt[1], "error_cuadratico": error_alt})

    # ------------------------------------------------------------------
    # Resumen final (útil para la tabla del informe)
    # ------------------------------------------------------------------
    resumen_path = BASE_DIR / "resumen_ajustes.csv"
    with resumen_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["algoritmo", "modelo", "c1", "c2", "error_cuadratico"])
        writer.writeheader()
        writer.writerows(resumen)

    print(f"\nListo. Resultados guardados en: {BASE_DIR}")
    for fila in resumen:
        print(
            f"  {fila['algoritmo']:22s} {fila['modelo']:16s} "
            f"c1={fila['c1']:.3e}  c2={fila['c2']:.3e}  error={fila['error_cuadratico']:.3e}"
        )


if __name__ == "__main__":
    main()
