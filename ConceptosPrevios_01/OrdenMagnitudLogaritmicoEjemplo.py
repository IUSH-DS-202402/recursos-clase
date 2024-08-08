n = int(input())                                                # 1 
iterador = n                                                    # 1
resultado = 0                                                   # 1
while (iterador > 1):                                           # log2(n) + 1
    iterador = iterador/2                                       # log2(n)
    resultado += 1                                              # log2(n)

print(f"El logaritmo de {n} base 2 es {resultado}")             # 1