def stair(n):

    if n <= 2:
        return n
    
    prev1 = 1
    prev2 = 1
    curr = 2

    for i in range(2, n):
        memo = curr + prev1 + prev2
        prev1 = prev2
        prev2 = curr
        curr = memo

    return curr

if __name__ == "__main__":
    print(stair(5))