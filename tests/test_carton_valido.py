from src import bingo

# Genera el carton
mi_carton = bingo.carton()

# Guarda la cantidad de celdas ocupadas
cant_celdas_ocupadas = bingo.contar_celdas_ocupadas(mi_carton)

# Verifica que la cantidad de celdas ocupadas no sea menor a 15
def test_no_menos_de_15():
    assert cant_celdas_ocupadas >= 15

# Verifica que la cantidad de celdas ocupadas no sea mayor a 15
def test_no_mas_de_15():
    assert cant_celdas_ocupadas <= 15

# Verifica que no haya columnas vacias
def test_sin_colums_vacias():
    assert bingo.sin_colums_vacias(mi_carton)

# Verifica que no haya filas vacias
def test_sin_filas_vacias():
    assert bingo.sin_filas_vacias(mi_carton)
