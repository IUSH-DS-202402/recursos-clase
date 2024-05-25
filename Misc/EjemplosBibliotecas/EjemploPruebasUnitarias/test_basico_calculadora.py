# Primero, asegúrate de tener pytest instalado. Puedes instalarlo usando pip:
# pip install pytest

# Este archivo contiene ejemplos básicos de cómo escribir y ejecutar pruebas usando pytest.

# Importa la biblioteca pytest
import pytest

# Importamos las funciones del archivo calculadora
from calculadora import suma, resta, multiplica, divide

# Escribimos nuestras pruebas. Cada prueba es una función que comienza con la palabra "test_".

def test_suma():
    """Prueba la función suma."""
    assert suma(1, 2) == 3
    assert suma(-1, 1) == 0
    assert suma(-1, -1) == -2

def test_resta():
    """Prueba la función resta."""
    assert resta(2, 1) == 1
    assert resta(-1, 1) == -2
    assert resta(-1, -1) == 0

def test_multiplica():
    """Prueba la función multiplica."""
    assert multiplica(2, 3) == 6
    assert multiplica(-1, 1) == -1
    assert multiplica(-1, -1) == 1

def test_divide():
    """Prueba la función divide."""
    assert divide(6, 3) == 2
    assert divide(-1, 1) == -1
    assert divide(-1, -1) == 1

    # Prueba la excepción de división por cero
    with pytest.raises(ValueError, match="No se puede dividir por cero!"):
        divide(1, 0)

# Para ejecutar estas pruebas, abre una terminal y navega al directorio que contiene `test_calculadora.py`.
# Luego ejecuta el siguiente comando:
# pytest test_basico_calculadora.py

# pytest buscará automáticamente cualquier función que comience con "test_" y ejecutará cada una de ellas.
# Los resultados se mostrarán en la terminal.