from src.bingo import carton

# Cuenta la cantidad de celdas ocupadas, funcion axuiliar para los tests
def contar_celdas_ocupadas():
    mi_carton = carton()
    contador = 0
    for fila in mi_carton:
        for celda in fila:
            contador += celda
    return contador

# Guarda la cantidad de celdas ocupadas
cant_celdas_ocupadas = contar_celdas_ocupadas()

# Verifica que la cantidad de celdas ocupadas no sea menor a 15
def test_no_menos_de_15():
    assert cant_celdas_ocupadas >= 15

# Verifica que la cantidad de celdas ocupadas no sea mayor a 15
def test_no_mas_de_15():
    assert cant_celdas_ocupadas <= 15

# Verifica que no haya columnas vacias
def test_sin_colums_vacias():
    mi_carton = carton()
    for i in range(9):
        if not(mi_carton[0][i] or mi_carton[1][i] or mi_carton[2][i]):
            assert False
    assert True
