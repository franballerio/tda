# Feature: benchmark de complejidad para las dos DP de la mochila

Fecha de creación: 2026-10-02
Rama: `main` (repo `/home/fballerio/uba/tda`) — los commits de work unit se proponen al cierre.

## Objetivo

Adaptar `complejidad/benchmark.py` (hoy clon del benchmark de TP0 sobre cuartetos de
primos) para comparar empíricamente los dos algoritmos de Programación Dinámica del
Problema 3 del TP1:

- `mochila.py` — planteo tradicional: maximizar beneficio con capacidad fija W. Tabla
  `(n+1) x (W+1)` => O(n*W).
- `mochila_alt.py` — planteo alternativo: minimizar peso con beneficio fijo B. Tabla
  `(n+1) x (B+1)` => O(n*B).

Las instancias salen del generador de `crear_mochila.py` (cap = 50n, pesos 1-200,
beneficios 1-1000).

## Decisiones (tomadas con el usuario)

1. **B = capacidad** que devuelve `crear_mochila` (B = W = 50n): ambas tablas tienen el
   mismo ancho, la comparación de tiempos es pareja y ambos casos son O(n^2).
2. **Escala equilibrada**: 8 tamaños `logspace(100, 500)`, 3 corridas por tamaño
   (`RUNS_PER_SIZE`), 8 GB de RAM disponibles, 3 workers.
3. **Verificación real**: venv con `uv` + `numpy/scipy/matplotlib/seaborn`, correr el
   benchmark completo y entregar CSV/PNG.

## Tareas

- [x] 1. Refactorizar `crear_mochila.py`: extraer `generar_mochila(n) -> (cap, pesos,
      beneficios)` y proteger la llamada `crear_mochila(1000)` con
      `if __name__ == "__main__"` para que sea importable sin efectos secundarios.
- [x] 2. Depurar `mochila_alt.py`: eliminar el `for row in memo: print(row)` de debug
      (destruiría la medición) y unificar el import con `mochila.py`
      (`import parser_mochila`).
- [x] 3. Reescribir `complejidad/benchmark.py`: importar las dos DP y el generador,
      generar una instancia por tamaño (semilla fija), medir ambos algoritmos con
      `util.time_algorithm`, ajustar por cuadrados mínimos (modelo c1*n^2 + c2, con
      W = B = 50n) y producir CSV + gráficos + `resumen_ajustes.csv`.
- [x] 4. Preparar entorno: `uv venv tp1/.venv` (`.venv` ya está en `.gitignore`) e
      instalar `numpy scipy matplotlib seaborn` (CPython 3.12.14, scipy 1.18.1).
- [x] 5. Ejecutar el benchmark completo y verificar salidas:
      `tiempos_tradicional.csv`, `tiempos_alternativo.csv`, `grafico_tradicional.png`,
      `grafico_alternativo.png`, `grafico_comparacion.png`, `resumen_ajustes.csv`;
      validar que las dos DP devuelven resultados coherentes sobre una instancia
      chica y que los ajustes tienen error razonable.
- [x] 6. Cierre: preflight de revisión nativa (`gentle_review inspect` si el switch
      está activo), reporte de checks y decisión de commit con el usuario.

## Evidencia

- Tarea 1: import de `crear_mochila` no escribe archivos (`mochila1000.txt` intacto);
  `generar_mochila(10)` devuelve (500, 10 pesos, 10 beneficios) dentro de los rangos.
- Tarea 2: `python3 mochila.py` -> 2787 y `python3 mochila_alt.py` -> 90 sobre
  `mochila10.txt` (sin volcado de tablas).
- Tarea 5: benchmark completo en 24.6 s (8 tamaños, 3 corridas).
  - Ajustes: tradicional c1=2.408e-07 (error 3.96e-03), alternativo c1=3.162e-07
    (error 1.05e-02). El alternativo tarda ~31% más por celda de tabla.
  - Contra fuerza bruta (n=16, semilla 999): `mochila` 6552 == 6552 OK,
    `mochila_alt` 21 == 21 OK (script en /tmp/check_dps.py, no versionado).
  - Salidas inspeccionadas: los 3 PNG se ven correctos (ajuste pegado a la
    medición, comparación log-log con ambas curvas paralelas).
- Checks no ejecutados / pendientes: ninguno. No se corrió ningún test suite
  (el TP no tiene); la verificación fue funcional (fuerza bruta) + ejecución real.
- Tarea 6 (preflight de revisión): RDD está activo (`gentle-ai review mode status`
  -> on). `gentle_review inspect` corrió sobre el candidato (8 paths, 452 líneas,
  riesgo medium); el consentimiento de START para este candidato volvió
  **declined** (candidate-scoped, `lineage_created: false`), así que esta corrida
  queda sin revisión nativa. No se reintentó START para no insistir sobre una
  decisión ya tomada.

## Iteración 2 — mismos tests con los datos de `complejidad/data/` (2026-10-02)

Contexto: se revirtió `crear_mochila.py` a su forma original (ya no expone
`generar_mochila`) y se creó `complejidad/data/mochila{10,50,100,200,500,700,1000}.txt`
(moviendo ahí los `mochila*.txt` que estaban en la raíz de tp1). El benchmark dejó
de funcionar porque importaba `generar_mochila`.

- [x] 7. Reorientar `complejidad/benchmark.py`: cargar las instancias con
      `parser_mochila` desde `data/mochila*.txt` (los tamaños salen de los
      archivos) y ajustar contra el trabajo real `n * capacidad`.
- [x] 8. Re-correr el benchmark completo y la verificación (fuerza bruta +
      DP 1D independiente + DP arriba-abajo independiente) con esos datos.
- [ ] 9. Commit (espera decisión del usuario).

Verificación de datos previa: los 7 archivos tienen n coherente con el nombre,
capacidad = 50n y beneficio total >= capacidad (B factible en todos).

### Evidencia iteración 2

- `benchmark.py` ya no toca `crear_mochila.py`: descubre `data/mochila*.txt`
  con `parser_mochila`, valida nombre vs contenido y factibilidad de B, y mide
  `[10, 50, 100, 200, 500, 700, 1000]`. El ajuste ahora es contra el trabajo
  real `celdas = n * capacidad` (no contra 50n² supuesto).
- Benchmark completo en 55 s (3 corridas por tamaño). Tiempos (s): trad
  0.001 → 13.02, alt 0.002 → 16.55. Ajustes: `c1_trad = 2.595e-07`,
  `c1_alt = 3.312e-07` s/celda (alternativo ~28% más lento), errores 7.82e-02 y
  7.08e-02 sobre tiempos de hasta 16 s (relativos < 1%).
- Verificación con datos de `data/` (script /tmp/check_dps_data.py, no
  versionado): las dos DP coinciden con implementaciones 1D independientes en
  las 7 instancias; fuerza bruta en `mochila10.txt` coincide (trad 2787,
  alt 90). Todo OK.
- Salidas regeneradas (complejidad/*.csv y 3 PNG); el gráfico de comparación
  cubre 4 órdenes de magnitud en n con pendiente ~2 en log-log.
- Preflight iteración 2: candidato nuevo (target sha256:70fb8a9e…, 15 paths —
  código + doc + 3 CSV + los 7 archivos de `data/`; los PNG siguen fuera por
  ser binarios reproducibles). `inspect` → `start` y el consentimiento volvió
  **declined** otra vez para este candidato (`lineage_created: false`). No se
  reintentó: la decisión es candidate-scoped y ya está tomada.
