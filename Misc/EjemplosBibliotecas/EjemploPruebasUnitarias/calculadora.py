
def suma(a, b):
    """Esta función retorna la suma de dos números."""
    return a + b

def resta(a, b):
    """Esta función retorna la resta de dos números."""
    return a - b

def multiplica(a, b):
    """Esta función retorna la multiplicación de dos números."""
    return a * b

def divide(a, b):
    """Esta función retorna la división de dos números.
    Lanza una excepción si el divisor es cero."""
    if b == 0:
        raise ValueError("No se puede dividir por cero!")
    return a / b