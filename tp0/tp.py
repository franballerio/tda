import time
import math

# posibles divisores hasta raiz n
# def esprimo(n):
#     i = 2
#     cd = 0
#     while i <= n**0.5:
#         if n%i == 0:
#             cd = cd+1
#         i = i+1
#     return cd == 0

# con un solo divisor ya no es primo
# def esprimo(n):
#     i = 2
#     while i <= n**0.5:
#         if n%i == 0:
#             return False
#         i = i+1
#     return True

# def esprimoV2(n):
#     for i in range(2,int(n**0.5)):
#         if n%i == 0:
#              return False
#     return True

def esprimo(n: int):
    limite = math.isqrt(n) + 1
    for i in range(2, limite):
        if n % i == 0:
             return False
    return True

def esprimov1(n: int) -> bool:
    limite = math.isqrt(n) + 1
    # Check 6k - 1 and 6k + 1 up to sqrt(n)
    for i in range(5, limite, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def prog():
    t1 = time.perf_counter()
    _primo = esprimo
    resultados = []
    for i in range(11, 1000000, 30):
        a = i
        b = i + 2
        c = i + 6
        d = i + 8
        if _primo(a) and _primo(b) and _primo(c) and _primo(d):
            resultados.append((a, b, c, d))
    t2 = time.perf_counter() - t1
    print(2, 3, 5, 7)
    for r in resultados:
        print(*r)
    print(t2)
    return t2

def prog1():
    t1 = time.perf_counter()
    _primo = esprimov1

    resultados = [
        (i, i + 2, i + 6, i + 8)
        for i in range(11, 1000000, 30)
        if _primo(i) and _primo(i + 2) and _primo(i + 6) and _primo(i + 8)
    ]

    print(2, 3, 5, 7)
    for r in resultados:
        print(*r)
    t2 = time.perf_counter() - t1
    print(t2)

if __name__ == "__main__":
    # p = prog()
    prog1()
    # print(p, p1)
