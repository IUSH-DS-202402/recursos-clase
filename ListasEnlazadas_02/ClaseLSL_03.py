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


class LSL:
    def __init__(self) -> None:
        self.primero = None
        self.ultimo = None
    def esVacia(self) -> bool:
        return self.primero == None
    def primerNodo(self):
        return self.primero
    def ultimoNodo(self):
        return self.ultimo
    
    def anterior(self, posterior: NS) -> NS:
        iterador = self.primerNodo()
        nodoAnt = None
        while iterador != posterior and iterador is not None:
            nodoAnt = iterador
            iterador = iterador.retornaLiga()
        if iterador is None:
            raise Exception(f"No se encontró {posterior} en la lista")
        return nodoAnt
    
    def buscaDondeInsertar(self, candidato) -> NS:
        iterador:NS = self.primerNodo()
        nodoAnt = None
        while iterador != None and iterador.retornaDato() < candidato:
            nodoAnt = iterador
            iterador = iterador.retornaLiga()
        return nodoAnt
    
    def conectar(self, nodoAConectar:NS, nodoAnterior:NS) -> None:
        if nodoAnterior == None:
            nodoAConectar.asignaLiga(self.primero)
            if self.primero == None:
                self.ultimo = nodoAConectar
            self.primero = nodoAConectar
        else:
            nodoAConectar.asignaLiga(nodoAnterior.retornaLiga())
            nodoAnterior.asignaLiga(nodoAConectar)
            if nodoAnterior == self.ultimo:
                self.ultimo = nodoAConectar

    def insertar(self, dato):
        nodoAnterior = self.buscaDondeInsertar(dato)
        nuevoNodo = NS(dato)
        self.conectar(nuevoNodo,nodoAnterior)

    def recorre(self):
        iterador = self.primerNodo()
        while iterador != None:
            print(iterador.retornaDato())
            iterador = iterador.retornaLiga()
    
    def buscarDato(self, dato) -> NS:
        iterador = self.primerNodo()
        nodoAnt = None
        while iterador != None and iterador.retornaDato() != dato:
            nodoAnt = iterador
            iterador = iterador.retornaLiga()
        return iterador
    
    def desconectar(self, nodoADesconectar:NS) -> None:
        nodoAnterior = self.anterior(nodoADesconectar)
        if nodoADesconectar == self.primero:
            self.primero = self.primero.retornaLiga()
            if self.primero == None:
                self.ultimo = None
        else:
            nodoAnterior.asignaLiga(nodoADesconectar.retornaLiga())
            if nodoADesconectar == self.ultimo:
                self.ultimo = nodoAnterior

    def borrar(self,datoABorrar) -> None:
        nodoABorrar = self.buscarDato(datoABorrar)
        if nodoABorrar == None:
            raise("Dato inexistente en la lista")
        self.desconectar(nodoABorrar)
