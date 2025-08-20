def add(a, b):
    """Adderar två tal"""
    return a + b

def subtract(a, b):
    """Subtraherar b från a"""
    return a - b

def multiply(a, b):
    """Multiplicerar två tal"""
    return a * b

def divide(a, b):
    """Dividerar a med b"""
    if b == 0:
        raise ValueError("Kan inte dividera med noll!")
    return a / b