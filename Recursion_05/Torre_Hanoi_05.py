from collections import deque

class Torre:
    def __init__(self, nombre, aros=[]):
        if aros != sorted(aros, reverse=True):
            raise Exception("Aros iniciales no están ordenados")
        self.aros = deque(aros)
        self.nombre = nombre


    def apilar(self, aro):
        if len(self.aros) > 1 and aro >= self.aros[-1]:
            raise Exception("Se intenta ingresar un aro más grande")
        self.aros.append(aro)

    def desapilar(self):
        if len(self.aros) < 1:
            raise Exception("No hay aros para desapilar")
        return self.aros.pop()
    
    def pistear(self):
        if len(self.aros) < 1:
            return None
        return self.aros[-1]

def print_aros(n, origen, auxiliar, destino):
    length = n*3*2 + n-1
    lineas = []
    rotulo = ["="]*length
    rotulo[n-1:n] = ["o"]*2
    rotulo[n*3:n*3+1] = ["a"]*2
    rotulo[n*5+1:n*5+2] = ["d"]*2
    lineas.append(rotulo)
    for i in range(n):
        l = [' ']*length
        if i < len(origen.aros):
            tamano_aro = origen.aros[i]
            l[n-tamano_aro:n+tamano_aro] = ['#']*(2*tamano_aro)

        if i < len(auxiliar.aros):
            tamano_aro = auxiliar.aros[i]
            l[n*3+1-tamano_aro:n*3+1+tamano_aro] = ['#']*(2*tamano_aro)

        if i < len(destino.aros):
            tamano_aro = destino.aros[i]
            l[n*5+2-tamano_aro:n*5+2+tamano_aro] = ['#']*(2*tamano_aro)
        lineas.append(l)

    lineas.append([])
    lineas.reverse()
    for l in lineas:
        print("".join(l))


origen = Torre("o",[4,3,2,1])
auxiliar = Torre("a")
destino = Torre("d")

print_aros(4,origen, auxiliar,destino)


def mover_torre(n,o,a,d):
    """ Mueve la torre de n aros desde o (origen) hasta d (destino) usando a (auxiliar)."""
    if n > 0: # Si hay al menos un aro en la torre
        mover_torre(n-1,o,d,a) # Mueve la torre de n-1 aros de origen a auxiliar usando destino
        n_aro = o.desapilar() #Toma el aro que queda en el origen
        d.apilar(n_aro) # Mueve el aro que estaba en el origen al destino
        print(f"{o.nombre} -> {d.nombre}")
        print_aros(4,origen, auxiliar,destino)
        input() 
        mover_torre(n-1,a,o,d) # Mueve la torre de n-1 aros de auxiliar a destino usando origen

mover_torre(4, origen,auxiliar,destino)


