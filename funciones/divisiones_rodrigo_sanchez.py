def dividir(a, b):
 """Devuelve la división de dos números. Si b es 0, devuelve None."""
 if b == 0:
  return None
 return a / b
#tests/test_dividir.py
from funciones.dividir import dividir # type: ignore
def test_dividir():
 assert dividir(10, 2) == 5
 assert dividir(5, 0) is None