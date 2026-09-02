import time
# import math

def erato(n: int) -> list[bool]:
    if n < 2:
        return []

    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for p in range(2, int(n**0.5) + 1):
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False

    return is_prime

def esprimo(n: int) -> bool:
    if not hasattr(esprimo, "_sieve"):
        esprimo._sieve = erato(1000008)

    if n >= len(esprimo._sieve):
        esprimo._sieve = erato(n * 2)

    return esprimo._sieve[n]


def prog():
    t1 = time.time()

    resultados = [
        (i, i + 2, i + 6, i + 8)
        for i in range(11, 983449, 30)
        if esprimo(i) and esprimo(i + 2) and esprimo(i + 6) and esprimo(i + 8)
    ]

    print(2, 3, 5, 7)
    for r in resultados:
        print(*r)

    t2 = time.time() - t1
    print(t2)


if __name__ == "__main__":
    prog()
