import time
import math

def erato(n: int) -> list[int]:
    """Returns a list of all prime numbers up to n."""
    if n < 2:
        return []

    # Initialize a boolean list tracking the prime status of numbers 0 to n
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime

    # Only iterate up to the square root of n
    for p in range(2, int(n**0.5) + 1):
        if is_prime[p]:
            # Mark all multiples of p starting from p*p as false
            for i in range(p * p, n + 1, p):
                is_prime[i] = False

    # Filter out and return the indices that remain True
    return [num for num, prime in enumerate(is_prime) if prime]

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

# def esprimoV3(n: int, primes: list[int]):
#     for i in primes:
#         if (i > int(math.sqrt(n))):
#             break
#         if n%i == 0:
#              return False
#     return True

def esprimoV4(n: int, primes: list[int]):
    limite = int(math.sqrt(n))
    for i in primes:
        if (i > limite):
            break
        if n%i == 0:
             return False
    return True

# def prog():
#     t1 = time.time()
#     primes = erato(int(math.sqrt(1000000)))
#     # print(11,13,17,19)
#     # print(101, 103, 107,109)
#     for i in range(11, 1000000, 30):
#         if esprimoV3(i, primes) and esprimoV3(i+2, primes) and esprimoV3(i+6, primes) and esprimoV3(i+8, primes):
#             print (i, i+2, i+6,i+8)
#     t2 = time.time()
#     times = t2 - t1
#     print(times)
#     return times

def prog():
    t1 = time.time()
    primes = erato(int(math.sqrt(1000000)))
    # print(11,13,17,19)
    # print(101, 103, 107,109)
    for i in range(11, 1000000, 30):
        if esprimoV4(i, primes) and esprimoV4(i+2, primes) and esprimoV4(i+6, primes) and esprimoV4(i+8, primes):
            print (i, i+2, i+6,i+8)
    t2 = time.time()
    times = t2 - t1
    print(times)
    return times

p = prog()
# print('-------------------------')
# p1 = prog1()

# print(p, p1)
