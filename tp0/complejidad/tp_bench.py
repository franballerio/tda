import time
import math

def esprimo(n: int) -> bool:
    limite = math.isqrt(n) + 1
    for i in range(5, limite, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def buscar_cuartetos(limite: int):
    return 

def prog(limite: int = 1_000_000, mostrar: bool = True):
    t1 = time.perf_counter()
    resultados = [ 
        (i, i + 2, i + 6, i + 8)
        for i in range(11, limite, 30)
        if esprimo(i) and esprimo(i + 2) and esprimo(i + 6) and esprimo(i + 8)
    ]
    t2 = time.perf_counter() - t1

    if mostrar:
        print(2, 3, 5, 7)
        for r in resultados:
            print(*r)
        print(t2)

    return t2, resultados

if __name__ == "__main__":
    prog()
