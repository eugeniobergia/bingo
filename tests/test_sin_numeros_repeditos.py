from src import bingo

mi_carton = bingo.carton()

def test_sin_numeros_repeditos():
    assert bingo.sin_numeros_repeditos(mi_carton)
