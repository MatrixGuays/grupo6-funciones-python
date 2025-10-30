#funciones/promedio.py
def promedio(numeros):
 """Devuelve el promedio de una lista de números."""
 if not numeros:
    return None
    return sum(numeros) / len(numeros)

