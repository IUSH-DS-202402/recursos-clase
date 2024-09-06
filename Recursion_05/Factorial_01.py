def fact(n):
    if n < 0:
        raise Exception("No está definido el factorial en los negativos")
    if n == 0:
        return 1
    return n * fact(n-1)