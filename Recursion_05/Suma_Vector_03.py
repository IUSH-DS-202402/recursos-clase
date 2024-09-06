def sumaDatos(V,n):
    suma = 0
    for i in range(n):
        suma += V[i]
    return suma

sumaDatos([1,2,3],3)

def sumaDatos(V, i, n):
    suma = 0
    if i < n:
        suma = V[i] + sumaDatos(V, i+1, n)
    return suma


sumaDatos([1,2,3],0,3)

