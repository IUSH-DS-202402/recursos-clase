from HashMap_04.NM import NM
class HashMap:
    def __init__(self):
        self.conteo_buckets = 10
        self.conteo = 0
        buckets = [None] * self.conteo_buckets

    def obtener(self,llave):
        hash_reducido = self.__obtener_hash_reducido(llave)
        iterador = self.buckets[hash_reducido]
        while iterador is not None and llave != iterador.retornaLlave():
            iterador = iterador.retornaLiga()
        if iterador is None:
            raise("No se encontró la llave {llave}")
        return iterador
    
    def contiene(self, llave):
        try:
            self.obtener(llave)
        except:
            return False
        return True
    
    def poner(self, llave, valor):
        nodo_nuevo = NM(llave,valor)
        hash_reducido = self.__obtener_hash_reducido(llave)

        if self.buckets[hash_reducido] is None:
            self.buckets[hash_reducido] = nodo_nuevo
            self.conteo += 1
            return
        
        iterador = self.buckets[hash_reducido]
        anterior = None

        while iterador is not None and llave != iterador.retornaLlave():
            anterior = iterador
            iterador = iterador.retornaLiga()
        
        if iterador is None:
            anterior.asignaLiga(nodo_nuevo)
            self.conteo += 1
        else:
            iterador.asignaValor(valor)


    def __obtener_hash_reducido(self, llave):
        valor_hash = hash(llave)
        hash_reducido = valor_hash % self.conteo_buckets
        return hash_reducido