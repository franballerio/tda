---
Date: 2026-08-19
tags:
  - Algoritmos
  - TDA
---
---

Drive de la materia: 
https://drive.google.com/drive/u/1/folders/1KarLqknqmyIMZvTDdXGdrgmBJyvnaGUL?hl=es-419

## Temas
Se veran a lo largo de la cursada las siguientes estrategias de diseno de algoritmos para la resolucion de problemas un poco mas complejos a los que estamos acostumbrados

|    Programacion Dinamica     |        Grafos        |
| :--------------------------: | :------------------: |
|       **Backtracking**       |  **Redes de flujo**  |
|    **Divide and conquer**    | **Reducciones**<br>  |
|          **Greedy**          | **Randomizadas**<br> |
|   **Programacion lineal**    | **Heuristicas**<br>  |
| **Programacion Concurrente** |  **Automatas**<br>   |

---

### Primer Problema

![[Primer Problema.png|430]]

El problema no aclara, pero los valores son 0 - 9. Y no pueden repetirse los valores.

Sabiendo esto, la unica opcion que tenemos es probar todas y cada una de las combinaciones. **FUERZA BRUTA**

![[Fuerza Bruta.png]]

Esta solucion toma 75 segundos en finalizar. Dirias que esta solucion es eficiente?
Con medir el tiempo no podemos lograr darle una eficiencia objetiva, pues el tiempo es relativo (chiste robado al Pablo).

Debemos analizar la complejidad:

> Vemos las operaciones del algoritmo:
> 	- cant de fors == cant de letras == 8
> 	- cada for tiene 10 iteraciones
> 	- cada comparacion se ejecuta $10^8$ veces

Entonces si agrego mas letras la complejidad crece.
Al igual que si cada letra pudiera representar mas simbolos.
Ej: 15 letras que pueden representar 0-9 tendremos $10^{15}$
Osea que la complejidad es O($10^n$)

### Problemas

A lo largo de la materia tendremos una problema (como toda la historia de la computacion P vs NP).
Dividiremos los problemas a resolver de la siguiente manera:
- Polinomiales ("Faciles") 
- No Polinomiales ("Dificiles")

Lo demostramos de esta manera $$\lim_{n \to \infty} {n^b \over a^n} = 0$$
Cumpliendose para todo $a > 1$ que $a^n$ (exponencial) crece mas rapido que $n^b$ (polinomial)