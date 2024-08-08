class Gato:
    def __init__(self, nombre, edad):
        self.edad = edad
        self.nombre = nombre

    def autopresentacion(self):
        print(f"Hola, soy {self.nombre} el gato y tengo {self.edad} años gatunos, miau :3")

mi_primer_gato = Gato("Silvestre", 5)
mi_segundo_gato = Gato("Doraemon", 30)
mi_primer_gato.autopresentacion()
mi_segundo_gato.autopresentacion()

mi_primer_gato.nombre = 'Bola de Nieve II'
mi_primer_gato.autopresentacion()