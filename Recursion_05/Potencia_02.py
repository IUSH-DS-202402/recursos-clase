def pow(n,r):
    if r == 0:
        return 1
    if r > 0:
        return n * pow(n, r-1)
    if r < 0:
        return 1/n * pow(n, r+1)

pow(10,2)

