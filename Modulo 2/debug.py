def fatorial(n, n1= 1):
    if n == 0:
        return n1
    return fatorial(n-1, n*n1)

fatorial(5)