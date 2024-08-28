class NS:
    def __init__(self, dato) -> None:
        self.dato = dato
        self.liga = None

    def asignaLiga(self, nodoALigar) -> None:
        self.liga = nodoALigar

    def asignaDato(self, dato) -> None:
        self.dato = dato

    def retornaLiga(self):
        return self.liga
    
    def retornaDato(self):
        return self.dato


class Cola:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def esVacia(self):
        return self.primero is None
    
    def esLlena(): # Puede ser implementada de manera diferente
        return False
    
    def encolar(self, dato):
        nodo = NS(dato)
        if self.primero is not None:
            self.ultimo.asignaLiga(nodo)
        else:
            self.primero = nodo
        self.ultimo = nodo
    
    def desencolar(self):
        if self.esVacia():
            raise Exception("La cola está vacía")
        nodo = self.primero
        if self.primero == self.ultimo:
            self.ultimo = None
        self.primero = self.primero.retornaLiga()
        return nodo.retornaDato()
    
    def pistear(self):
        return self.primero.retornaDato()