def multiplicar(a, b):
 """Devuelve el producto de dos números."""
 return a * b
#tests/test_multiplicar.py
from funciones.multiplicar import multiplicar # type: ignore
def test_multiplicar():
 assert multiplicar(3, 4) == 12
 assert multiplicar(-2, 5) == -10