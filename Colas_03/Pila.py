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


class Pila:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def esVacia(self):
        return self.primero is None
    
    def esLlena(): # Puede ser implementada de manera diferente
        return False
    
    def apilar(self, dato):
        nodo = NS(dato)
        nodo.asignaLiga(self.primero)
        if self.primero is None:
            self.ultimo = nodo
        self.primero = nodo
    
    def desapilar(self):
        if self.esVacia:
            raise Exception("No hay elementos en la pila")
        nodo = self.primero
        if self.primero == self.ultimo:
            self.ultimo = None
        self.primero = self.primero.retornaLiga()
        return nodo.retornaDato()
    
    def tope(self):
        return self.primero.retornaDato()