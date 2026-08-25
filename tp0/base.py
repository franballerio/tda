import time

def esprimo(n):
    i = 2
    cd=0
    while i<=n-1:
        if n%i == 0:
            cd = cd+1
        i = i+1
    if cd == 0:
        return True
    else:
        return False

def prog():
    t1=time.time()
    for i in range (11,10000):
        if esprimo(i) and esprimo(i+2) and esprimo(i+6) and esprimo(i+8):
            print (i, i+2, i+6,i+8)
    t2=time.time()
    print(t2-t1)

prog()
