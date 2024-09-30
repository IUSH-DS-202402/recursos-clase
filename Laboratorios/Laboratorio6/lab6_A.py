# Lab 6 A
# Nombre:
# Grupo: 
# Cod Estudiante:

######################################
#                                    #
#             Punto #1               #
#                                    #
######################################

# Crear una clase llamada `SistemaArchivos` utilizando la representación de Árboles como HashMap vista en clase. 
# Al instanciar `SistemaArchivos`, debe crear un nodo raíz con el valor "C:".
# La clase `SistemaArchivos` debe permitir la gestión de rutas y contener los siguientes métodos:
# 
# - `crear_directorio(ruta)`: Recibe un parámetro `ruta` que contiene la nueva ruta a crear dentro del sistema de archivos. Las rutas deben comenzar desde la raíz.
#   La ruta se almacena de la siguiente manera: Cada elemento de la ruta está separado por '\' y el primer elemento siempre es "C:". Cada elemento subsecuente representa un subdirectorio en una estructura jerárquica.
#   - Si la jerarquía ya existe, retorna `False`.
#   - Si se crea exitosamente, retorna `True`.
#   - En caso de recibir una entrada inválida, lanza un error.
# - `consultar_directorio(ruta)`: Recibe un parámetro `ruta` que contiene la ruta a consultar en el sistema de archivos. 
#   - Si la ruta existe, retorna `True`.
#   - Si la ruta no existe, retorna `False`.
# 
# Nota: Debe usar la representación de Árboles como HashMap para que el punto sea válido.
# 
# INICIO_SOLUCION
# FIN_SOLUCION

######################################
#                                    #
#             Punto #2               #
#                                    #
######################################

# Mejore la eficiencia de las operaciones de inserción y consulta en la clase `SistemaArchivos` del Punto #1.
# Optimice la representación del árbol para mejorar la eficiencia de log(n) a tiempo constante. Incluya todo el código de la clase SistemaArchivos.

# INICIO_SOLUCION
# FIN_SOLUCION

######################################
#                                    #
#             Punto #3               #
#                                    #
######################################

# Partiendo de la clase `SistemaArchivos` del Punto #1. Cree el método `hallar_altura(ruta)` en la clase `SistemaArchivos`.
# Este método debe buscar el nodo con el valor dado y retornar la altura del nodo en la estructura. Si no existe lanza un error. Incluya todo el código de la clase SistemaArchivos.

# INICIO_SOLUCION
# FIN_SOLUCION


######################################
#                                    #
#             Punto #4               #
#                                    #
######################################

# Cree una función llamada `calcular_posfijo` que reciba una expresión matemática en notación posfija (postfija) y calcule el resultado.
# Las operaciones a considerar son:  multiplicación (*), división (/), suma (+) y resta (-).

# INICIO_SOLUCION
# FIN_SOLUCION

######################################
#                                    #
#             Punto #5               #
#                                    #
######################################

# Cree una clase llamada `ArbolExpresion` que permita construir un árbol de expresiones a partir de una expresión matemática en notación inorden.
# Las operaciones a considerar son: multiplicación (*), división (/), suma (+) y resta (-), 
# y deben manejarse también los paréntesis para definir la precedencia de las operaciones.
# 
# La clase `ArbolExpresion` debe incluir los siguientes métodos:
# - `leer_inorden(expresion)`: Recibe una cadena `expresion` que contiene la expresión matemática en notación inorden y construye el árbol de expresiones.
# - `imprimir()`: Imprime la expresión en notación inorden.
# 
# Incluya todo el código de la clase 'ArbolExpresion'.

# INICIO_SOLUCION
# FIN_SOLUCION

######################################
#                                    #
#             Punto #6               #
#                                    #
######################################

# Extienda la clase `ArbolExpresion` para permitir la construcción de un árbol de expresiones a partir de una expresión matemática en notación posorden.
# La clase `ArbolExpresion` debe incluir el siguiente método adicional:
# - `leer_posorden(expresion_posorden)`: Recibe una cadena `expresion_posorden` que contiene la expresión matemática en notación posorden y construye el árbol de expresiones.
# - `imprimir_posorden()`: Imprime la expresión en notación posorden.
# 
# Incluya todo el código de la clase 'ArbolExpresion'.

# INICIO_SOLUCION
# FIN_SOLUCION

######################################
#                                    #
#             Punto #7               #
#                                    #
######################################

# Extienda la clase `ArbolExpresion` para evaluar la expresión representada por el árbol.
# La clase `ArbolExpresion` debe incluir el siguiente método adicional:
# - `evaluar()`: Evalúa la expresión representada por el árbol y retorna el resultado. Incluya todo el código de la clase 'ArbolExpresion'.

# INICIO_SOLUCION
# FIN_SOLUCION