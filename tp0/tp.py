import time
import math

def esprimo(n: int) -> bool:
    limite = math.isqrt(n) + 1
    for i in range(5, limite, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def prog():
    t1 = time.time()

    resultados = [
        (i, i + 2, i + 6, i + 8)
        for i in range(11, 1000000, 30)
        if esprimo(i) and esprimo(i + 2) and esprimo(i + 6) and esprimo(i + 8)
    ]

    print(2, 3, 5, 7)
    for r in resultados:
        print(*r)

    t2 = time.time() - t1
    print(t2)

# if __name__ == "__main__":
#     prog()
