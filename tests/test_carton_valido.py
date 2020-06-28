from src import bingo

# Genera el carton
mi_carton = bingo.generar_carton()

# Guarda la cantidad de celdas ocupadas
cant_celdas_ocupadas = bingo.contar_celdas_ocupadas(mi_carton)

# Verifica que la cantidad de celdas ocupadas no sea menor a 15
def test_no_menos_de_15():
    assert cant_celdas_ocupadas >= 15

# Verifica que la cantidad de celdas ocupadas no sea mayor a 15
def test_no_mas_de_15():
    assert cant_celdas_ocupadas <= 15

# Verifica que la cantidad de celdas ocupadas por fila sea exactamente 5
def test_5_ocupadas_por_fila():
    assert (bingo.contar_celdas_ocupadas_en_fila(mi_carton[0]) == 5
    and bingo.contar_celdas_ocupadas_en_fila(mi_carton[1]) == 5
    and bingo.contar_celdas_ocupadas_en_fila(mi_carton[2]) == 5)

# Verifica que no haya columnas vacias
def test_sin_colums_vacias():
    assert bingo.sin_colums_vacias(mi_carton)

# Verifica que no haya filas vacias
def test_sin_filas_vacias():
    assert bingo.sin_filas_vacias(mi_carton)

# Verifica que no haya columnas llenas
def test_sin_colums_llenas():
    assert bingo.sin_colums_llenas(mi_carton)

# Verifica que no haya filas con 3 celdas ocupadas consecutivas
def test_sin_3_celdas_ocupadas_consecutivas():
    assert bingo.sin_3_celdas_ocupadas_consecutivas(mi_carton)

# Verifica que no haya filas con 3 celdas vacias consecutivas
def test_sin_3_celdas_vacias_consecutivas():
    assert bingo.sin_3_celdas_vacias_consecutivas(mi_carton)

# Verifica que solo haya 3 columnas son solo una columna ocupada
def test_3_colums_con_1_celda_ocupada():
    assert bingo.cant_colums_con_1_celda_ocupada(mi_carton) == 3

# Verifica que las celdas ocupadas esten en el rango de 1 a 90
def test_celdas_ocupadas_1_a_90():
    assert bingo.celdas_ocupadas_1_a_90(mi_carton)

# Verifica que las celdas por columnas esten en rangos crecientes de 10 en 10
def test_mayores_a_la_derecha():
    assert bingo.mayores_a_la_derecha(mi_carton)

# Verifica que las celdas de las columnas vayan creciendo de valor para abajo
def test_mayores_abajo():
    assert bingo.mayores_abajo(mi_carton)

# Verifica que no haya numeros repetidos en el carton
def test_sin_numeros_repeditos():
    assert bingo.sin_numeros_repeditos(mi_carton)

# Verifica que la matriz sea de 3x9
def test_matriz_de_3x9():
    assert bingo.matriz_de_3x9(mi_carton)
