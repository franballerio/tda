import time
import math

def erato(n: int) -> list[bool]:
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
    # return [num for num, prime in enumerate(is_prime) if prime]
    return is_prime

def esprimoV4(n: int, primes: list[bool]):
    return primes[n]

def prog():
    t1 = time.perf_counter()
    primes = erato(1000000)
    # print(11,13,17,19)
    # print(101, 103, 107,109)
    for i in range(11, 1000000, 30):
        if esprimoV4(i, primes) and esprimoV4(i+2, primes) and esprimoV4(i+6, primes) and esprimoV4(i+8, primes):
            print (i, i+2, i+6,i+8)
    t2 = time.perf_counter() - t1
    print(t2)

p = prog()
