"""
Benchmark de complejidad para el TP0.

Este script sigue el mismo enfoque explicado en `cuadrados_minimos.ipynb`
(ajuste por cuadrados mínimos con `scipy.optimize.curve_fit`) para comparar
empíricamente la complejidad de:

  1. La búsqueda completa de cuartetos de números primos usando cada una
     de esas versiones (O(n^2) contra O(n^1.5)).

Para medir los tiempos se reutiliza `time_algorithm` de `util.py`, tal como
se hace en el notebook.

Salidas generadas (en este mismo directorio):
  - tiempos_base.csv
  - tiempos_optimizado.csv
  - resumen_ajustes.csv (coeficientes del ajuste y error cuadrático total,
    útil para armar una tabla en el informe)
  - grafico_base.png
  - grafico_optimizado.png
"""

from __future__ import annotations

import ast
import csv
import sys
import types
from pathlib import Path
from typing import Callable

import math
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

from util import time_algorithm

# Reproducibilidad
np.random.seed(12345)
sns.set_theme()

BASE_DIR = Path(__file__).resolve().parent
TP0_DIR = BASE_DIR.parent

def esprimo_base(n):
    i = 2
    cd=0
    while i<=n-1:
        if n%i == 0:
            cd = cd+1
        i = i+1
    if cd == 0:
        return True
    else:
        return False

def prog_base(n: int):
    # t1=time.time()
    for i in range (11,n):
        if esprimo_base(i) and esprimo_base(i+2) and esprimo_base(i+6) and esprimo_base(i+8):
            print (i, i+2, i+6,i+8)
    # t2=time.time()
    # print(t2-t1)

def esprimo(n: int) -> bool:
    limite = math.isqrt(n) + 1
    for i in range(5, limite, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def prog_opt(n: int):
    # t1 = time.time()
    resultados = [
        (i, i + 2, i + 6, i + 8)
        for i in range(11, n, 30)
        if esprimo(i) and esprimo(i + 2) and esprimo(i + 6) and esprimo(i + 8)
    ]
    print(2, 3, 5, 7)
    for r in resultados:
        print(*r)

    # t2 = time.time() - t1
    # print(t2)


def guardar_csv(path: Path, sizes: np.ndarray, tiempos: dict) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["N", "tiempo_promedio_seg"])
        for n in sizes:
            writer.writerow([int(n), tiempos[n]])
    print(f"  CSV guardado en {path.name}")


def ajustar_y_graficar(
    *,
    nombre_archivo: str,
    titulo: str,
    sizes: np.ndarray,
    tiempos: dict,
    funcion_ajuste: Callable[..., np.ndarray],
    etiqueta_ajuste: str,
    color_ajuste: str = "r",
) -> tuple[np.ndarray, float]:
    """
    Ajusta `funcion_ajuste` a los tiempos medidos por cuadrados mínimos
    (usando `scipy.optimize.curve_fit`), grafica la medición junto con el
    ajuste y devuelve los coeficientes encontrados junto con el error
    cuadrático total del ajuste.
    """
    y = np.array([tiempos[n] for n in sizes], dtype=float)
    coeficientes, _ = curve_fit(funcion_ajuste, sizes, y, maxfev=20000)
    y_ajustada = funcion_ajuste(sizes, *coeficientes)
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
    # ------------------------------------------------------------------
    # 2) búsqueda de cuartetos: O(n^2) (base.py) vs O(n^1.5) (tp.py)
    # ------------------------------------------------------------------
    sizes_busqueda_base = np.logspace(np.log10(500), np.log10(6_000), 12).astype(int)
    sizes_busqueda_opt  = np.logspace(np.log10(1e5), np.log10(5e6), 12).astype(int)

    print("Midiendo búsqueda de cuartetos (base.py, O(n^2)) ...")
    tiempos_busqueda_base = time_algorithm(prog_base, sizes_busqueda_base, lambda n: [n])
    guardar_csv(BASE_DIR / "tiempos_busqueda_base.csv", sizes_busqueda_base, tiempos_busqueda_base)

    print("Midiendo búsqueda de cuartetos (tp.py, O(n^1.5)) ...")
    tiempos_busqueda_opt = time_algorithm(prog_opt, sizes_busqueda_opt, lambda n: [n])
    guardar_csv(BASE_DIR / "tiempos_busqueda_optimizada.csv", sizes_busqueda_opt, tiempos_busqueda_opt)

    f_cuadratica = lambda n, c1, c2: c1 * n**2 + c2
    f_n_por_raiz_n = lambda n, c1, c2: c1 * n**1.5 + c2

    c_busq_base, error_busq_base = ajustar_y_graficar(
        nombre_archivo="grafico_busqueda_base.png",
        titulo="Búsqueda de cuartetos (base.py) — ajuste O(n^2)",
        sizes=sizes_busqueda_base,
        tiempos=tiempos_busqueda_base,
        funcion_ajuste=f_cuadratica,
        etiqueta_ajuste="Ajuste $O(n^2)$",
    )
    c_busq_opt, error_busq_opt = ajustar_y_graficar(
        nombre_archivo="grafico_busqueda_optimizada.png",
        titulo="Búsqueda de cuartetos (tp.py) — ajuste O(n^1.5)",
        sizes=sizes_busqueda_opt,
        tiempos=tiempos_busqueda_opt,
        funcion_ajuste=f_n_por_raiz_n,
        etiqueta_ajuste="Ajuste $O(n^{1.5})$",
        color_ajuste="g",
    )
    graficar_comparacion(
        nombre_archivo="grafico_busqueda_comparacion.png",
        titulo="Búsqueda de cuartetos: base.py vs tp.py",
        series=[
            ("base.py — O(n^2)", sizes_busqueda_base, tiempos_busqueda_base),
            ("tp.py — O(n^1.5)", sizes_busqueda_opt, tiempos_busqueda_opt),
        ],
    )

    resumen.append({"algoritmo": "busqueda_base", "modelo": "c1*n^2 + c2", "c1": c_busq_base[0], "c2": c_busq_base[1], "error_cuadratico": error_busq_base})
    resumen.append({"algoritmo": "busqueda_optimizada", "modelo": "c1*n^1.5 + c2", "c1": c_busq_opt[0], "c2": c_busq_opt[1], "error_cuadratico": error_busq_opt})

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
