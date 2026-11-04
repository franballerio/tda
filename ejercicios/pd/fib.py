def fib(n):
    anterior = 1
    actual = 1

    for i in range(1, n):
        memo = actual + anterior
        anterior = actual
        actual = memo

    return actual

if __name__ == "__main__":
    print(fib(11))