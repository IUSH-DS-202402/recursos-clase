
from ListasEnlazadas_02.ClaseLSL_03 import LSL # Si se ejecuta Python desde el directorio raiz de git
#from ClaseLSL_03 import LSL # Si se ejecuta Python desde el directorio ListasEnlazadas_02
import random

print('Escriba la cantidad de números aleatorios a generar:')
num_a_generar = int(input())

secuencia = LSL()

for n_actual in range(0,num_a_generar):
    secuencia.insertar(random.randint(0, 100))

secuencia.recorre()