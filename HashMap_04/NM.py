class NM:
    def __init__(self, llave, valor) -> None:
        self.llave = llave
        self.valor = valor
        self.liga = None

    def asignaLiga(self, nodoALigar) -> None:
        self.liga = nodoALigar

    def asignaValor(self, valor) -> None:
        self.valor = valor

    def asignaLlave(self,llave):
        self.llave = llave

    def retornaLiga(self):
        return self.liga
    
    def retornaValor(self):
        return self.valor
    
    def retornaLlave(self):
        return self.llave

