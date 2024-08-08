
from ListasEnlazadas_02.ClaseLSL_03 import LSL # Si se ejecuta Python desde el directorio raiz de git
#from ClaseLSL_03 import LSL # Si se ejecuta Python desde el directorio ListasEnlazadas_02

print('Escriba el n hasta el cual se va a calcular Fibonacci(n):')
num_a_generar = int(input())

secuencia = LSL()

fn_menos2 = 0 #f0
fn_menos1 = 1 #f1

secuencia.insertar(fn_menos2) #f0
secuencia.insertar(fn_menos1) #f1

for n_actual in range(2,num_a_generar):
    fn = fn_menos2 + fn_menos1
    secuencia.insertar(fn)
    fn_menos2 = fn_menos1
    fn_menos1 = fn

secuencia.recorre()