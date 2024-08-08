def intercambio(V,a,b):
    temp = V[a] 
    V[a] = V[b] 
    V[b] = temp 


def seleccion(V:list):
    numElementos = len(V)
    iterExterno = 0
    while iterExterno < (numElementos - 1) :
        indiceMenor = iterExterno
        iterInterno = iterExterno + 1
        while iterInterno < numElementos:
            if V[iterInterno] < V[iterExterno]:
                indiceMenor = iterInterno
            iterInterno += 1
        intercambio(V,indiceMenor,iterExterno)
        iterExterno += 1
    return V