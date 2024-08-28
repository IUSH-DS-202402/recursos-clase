class NP:
    def __init__(self, dato, prioridad) -> None:
        self.dato = dato
        self.prioridad = prioridad
        self.liga = None

    def asignaLiga(self, nodoALigar) -> None:
        self.liga = nodoALigar

    def asignaDato(self, dato) -> None:
        self.dato = dato

    def asignaPrioridad(self, prioridad) -> None:
        self.prioridad = prioridad

    def retornaPrioridad(self):
        return self.prioridad

    def retornaLiga(self):
        return self.liga
    
    def retornaDato(self):
        return self.dato


class ColaPrioridad:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def esVacia(self):
        return self.primero is None
    
    def esLlena(): # Puede ser implementada de manera diferente
        return False
    
    def encolar(self, dato, prioridad):
        nodo = NP(dato, prioridad)
        aux = self.primero
        ant = None

        while aux is not None and nodo.prioridad < aux.prioridad:
            ant = aux
            aux = aux.retornaLiga()
        
        if ant is not None:
            ant.asignaLiga(nodo)
        else:
            self.primero = nodo

        if aux is None:
            self.ultimo = nodo
        
        nodo.asignaLiga(aux)
    
    def desencolar(self):
        if self.esVacia():
            raise Exception("La cola está vacía")
        nodo = self.ultimo
        if self.primero == self.ultimo:
            self.ultimo = None
        self.primero = self.primero.retornaLiga()
        return nodo.retornaDato()
    
    def pistear(self):
        return self.ultimo.retornaDato()