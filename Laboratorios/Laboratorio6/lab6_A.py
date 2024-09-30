# Lab 6 A
# Nombre:
# Grupo: 
# Cod Estudiante:

######################################
#                                    #
#             Punto #1               #
#                                    #
######################################

# Partiendo de la representación de Arboles como HashMap vista en clase, cree una clase llamada SistemaArchivos. Por defecto al crear una instancia del árbol, se creará el nodo raiz que tendrá el valor "C:". La clase SistemaArchivos almacenará rutas del sistema y deberá tener los siguientes métodos:
# - crear_directorio(ruta): Recibe un parámetro llamado ruta que contiene la ruta nueva que se va a crear dentro del sistema de archivos. Las rutas siempre deben comenzar desde la raiz. Ej: crear_directorio("C:\Usuarios\Felipe\Documentos"). La forma de almacenar las rutas es la siguiente:
#     Cada elemento de la ruta está separado por '\' siendo el primer elemento siempre C: y cada elemento subsecuente representa un subdirectorio en una estructura jerárquica., para el ejemplo anterior la relación de jerarquía es la siguiente: C: -> Usuarios -> Felipe -> Documentos. Al llamar varias veces el método se debe construir un árbol con dichas jerarquías. Si ya existía la jerarquía se debe retornar Falso, de lo contrario verdadero. En caso de recibir una entrada inválida se lanza un error.
# - consultar_directorio(ruta): Recibe un parámetro llamado ruta que contiene la ruta que se va a consultar en el sistema de archivos, si existe retorna Verdadero, si no retorna Falso.
#  ATENCIÓN: De no usar la representación mencionada al inicio el punto será inválido. Incluya todo el código de la clase SistemaArchivos.

# INICIO_SOLUCION
# FIN_SOLUCION

######################################
#                                    #
#             Punto #2               #
#                                    #
######################################

# Teniendo en cuenta que para realizar el punto anterior partió de la representación de árboles como HashMap vista en clase, la eficiencia a la hora de insertar y consultar elementos puede ser mejorada drásticamente de log(n) a constante. Analice y realice los cambios necesarios a la representación para que el orden de magnitud sea constante para estas operaciones. Incluya todo el código de la clase SistemaArchivos.


# INICIO_SOLUCION
# FIN_SOLUCION

######################################
#                                    #
#             Punto #3               #
#                                    #
######################################

# Busque el pensum de alguna universidad que le parezca llamativa de EEUU y represente como un árbol el pensum de algun estudio de pregrado o posgrado de su preferencia usando la notación de árbol como listas.


# INICIO_SOLUCION
# FIN_SOLUCION

######################################
#                                    #
#             Punto #4               #
#                                    #
######################################

# Partiendo de la representación de árboles como HashMap, cree el método hallar_altura(...) que dado el valor de un nodo, lo busque en la estructura y retorne la altura.

# INICIO_SOLUCION
# FIN_SOLUCION

######################################
#                                    #
#             Punto #5               #
#                                    #
######################################

# Partiendo de la representación de árboles como listas, cree el método 'ancestros(...)' que reciba el valor de un nodo, lo busque en la estructura e imprima los ancestros. Recuerde que los ancestros incluyen al nodo en cuestión.

# INICIO_SOLUCION
# FIN_SOLUCION