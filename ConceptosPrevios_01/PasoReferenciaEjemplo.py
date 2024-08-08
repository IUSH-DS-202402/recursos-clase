def cuadrado(base):
    base = base*base
    return base

i1 = 10
cuadrado(i1)
#Que pasará si imprimo i1?
print(i1)

def adicionar(lista, elemento):
    l2 = lista
    l2.append(elemento)
    return l2

v1 = [1,2,3]

adicionar(v1,4)
#¿Que pasará si imprimo v1?
print(v1)