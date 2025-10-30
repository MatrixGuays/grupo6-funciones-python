from funciones.restar import restar # type: ignore
def test_restar():
 assert restar(10, 4) == 6
 assert restar(5, 10) == -5