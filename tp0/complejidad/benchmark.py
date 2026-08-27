import csv
import matplotlib.pyplot as plt
from tp_bench import prog

LIMITES = [200_000, 400_000, 600_000, 800_000, 1_000_000, 3_000_000, 6_000_000, 10_000_000]
REPETICIONES = 10  # promediar corridas para estabilidad

def medir():
    resultados = []
    for limite in LIMITES:
        tiempos = []
        for _ in range(REPETICIONES):
            t, _ = prog(limite=limite, mostrar=False)
            tiempos.append(t)
        promedio = sum(tiempos) / len(tiempos)
        resultados.append((limite, promedio))
        print(f"N={limite:>8}  promedio={promedio:.4f}s  corridas={[f'{x:.4f}' for x in tiempos]}")
    return resultados

def guardar_csv(resultados, archivo="tiempos.csv"):
    with open(archivo, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["N", "tiempo_promedio_seg"])
        writer.writerows(resultados)

def graficar(resultados):
    xs = [r[0] for r in resultados]
    ys = [r[1] for r in resultados]

    # curva teorica O(N^1.5) normalizada contra el ultimo punto medido,
    # para comparar la forma de crecimiento (no los valores absolutos)
    c = ys[-1] / (xs[-1] ** 1.5)
    teoricos = [c * (x ** 1.5) for x in xs]

    plt.figure(figsize=(8, 5))
    plt.plot(xs, ys, marker="o", label="Tiempo medido")
    plt.plot(xs, teoricos, linestyle="--", label="O(N^1.5) teórico (normalizado)")
    plt.xlabel("N (límite superior)")
    plt.ylabel("Tiempo (segundos)")
    plt.title("Tiempo de ejecución vs N")
    plt.grid(True)
    plt.legend()
    plt.savefig("tiempos.png", dpi=150)
    print("Gráfico guardado en tiempos.png")

if __name__ == "__main__":
    resultados = medir()
    guardar_csv(resultados)
    graficar(resultados)
