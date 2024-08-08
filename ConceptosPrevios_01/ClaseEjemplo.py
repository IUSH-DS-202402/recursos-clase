class Perro: # Clase
    def __init__(self, capacidad): # Constructor
        self.pepitas_estomago = 0 # Atributo
        self.max_pepitas_estomago = capacidad #Atributo
        
    def hacer_sonido(self): #Método
        print("Guau Guau")

    def alimentar(self, num_pepitas): #Método
        nuevo_total = self.pepitas_estomago + num_pepitas #Referencia a si mismo
        if nuevo_total <= self.max_pepitas_estomago:
            self.pepitas_estomago = nuevo_total
            print(f"Que rico, ahora me he comido: {self.pepitas_estomago} pepitas")
        else:
            print("No puedo comer más, me voy a reventar")

p1 = Perro(10) # Instancia
p1.hacer_sonido()
p1.alimentar(5)
p1.alimentar(4)
p1.alimentar(5)