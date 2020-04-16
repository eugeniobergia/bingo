from src.bingo import carton

def contar_celdas_ocupadas():
    mi_carton = carton()
    contador = 0
    for fila in mi_carton:
        for celda in fila:
            contador += celda
    return contador

cant_celdas_ocupadas = contar_celdas_ocupadas()

def test_no_menos_de_15():
    assert cant_celdas_ocupadas >= 15

def test_no_mas_de_15():
    assert cant_celdas_ocupadas <= 15

def test_sin_colums_vacias():
    mi_carton = carton()
    for i in range(9):
        if not(mi_carton[0][i] or mi_carton[1][i] or mi_carton[2][i]):
            assert False
    assert True

# Verifica que no haya filas vacias
def test_sin_filas_vacias():
    mi_carton = carton()
    for fila in mi_carton:
        sum = 0
        for celda in fila:
            sum += celda
        if sum == 0:
            assert False
    assert True
