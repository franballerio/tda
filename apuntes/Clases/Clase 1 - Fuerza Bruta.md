---
Date: 2026-08-19
tags:
  - Algoritmos
  - TDA
  - Estrategia
---
---

Recorrer todo el espacio de soluciones de un problema combinatorio probando y analizando todas y cada una de las soluciones.

> Es la forma mas simple e ineficiente de resolver un problema

Un algoritmo genérico de fuerza bruta tiene más o menos esta forma:

1. Repetir:
	1. Generar la próxima solución
	2. Probar si la solución es válida
		1. Si es válida, ver si es mejor que la mejor solución hasta ahora.
2. Mientras queden soluciones sin probar.

- Funciona mientras el problema tenga una cantidad finita de soluciones, posibles de enumerar.    
- Pero es terriblemente lento.
- Vamos a ver estrategias para evitar probar todas las soluciones.