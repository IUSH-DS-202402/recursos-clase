# Los fixtures en pytest son una manera de proporcionar datos de prueba y configuraciones repetitivas 
# de una manera estructurada y reutilizable. 

# Importa la biblioteca pytest
import pytest

# Importamos las funciones del archivo calculadora
from calculadora import suma, resta, multiplica, divide

# Definimos un fixture que proporciona datos de prueba para las funciones de la calculadora.
@pytest.fixture
def datos():
    """Fixture que proporciona datos de prueba."""
    return {
        "a": 10,
        "b": 5,
        "c": 0
    }

# Definimos otro fixture que proporciona un diccionario con los resultados esperados
@pytest.fixture
def resultados():
    """Fixture que proporciona resultados esperados."""
    return {
        "suma": 15,
        "resta": 5,
        "multiplica": 50,
        "divide": 2
    }

# Escribimos nuestras pruebas. Cada prueba es una función que comienza con la palabra "test_".

def test_suma(datos, resultados):
    """Prueba la función suma usando un fixture."""
    assert suma(datos["a"], datos["b"]) == resultados["suma"]

def test_resta(datos, resultados):
    """Prueba la función resta usando un fixture."""
    assert resta(datos["a"], datos["b"]) == resultados["resta"]

def test_multiplica(datos, resultados):
    """Prueba la función multiplica usando un fixture."""
    assert multiplica(datos["a"], datos["b"]) == resultados["multiplica"]

def test_divide(datos, resultados):
    """Prueba la función divide usando un fixture."""
    assert divide(datos["a"], datos["b"]) == resultados["divide"]

    # Prueba la excepción de división por cero
    with pytest.raises(ValueError, match="No se puede dividir por cero!"):
        divide(datos["a"], datos["c"])

# Para ejecutar estas pruebas, abre una terminal y navega al directorio que contiene `test_calculadora.py`.
# Luego ejecuta el siguiente comando:
# pytest test_calculadora.py

# pytest buscará automáticamente cualquier función que comience con "test_" y ejecutará cada una de ellas.
# Los resultados se mostrarán en la terminal.