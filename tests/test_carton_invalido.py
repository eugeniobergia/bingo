from src import bingo

# Genera el carton
mi_carton = [
    [0,3,0,5,5,5,0,4,91],
    [1,2,0,0,0,0,0,0,0],
    [0,1,0,0,0,0,0,0,0]
]

# Guarda la cantidad de celdas ocupadas
cant_celdas_ocupadas = bingo.contar_celdas_ocupadas(mi_carton)

# Verifica que la cantidad de celdas ocupadas no sea igual a 15
def test_15_celdas_ocupadas():
    assert cant_celdas_ocupadas != 15

# Verifica que la cantidad de celdas ocupadas por fila no sea 5
def test_5_ocupadas_por_fila():
    assert (bingo.contar_celdas_ocupadas_en_fila(mi_carton[0]) != 5
    and bingo.contar_celdas_ocupadas_en_fila(mi_carton[1]) != 5
    and bingo.contar_celdas_ocupadas_en_fila(mi_carton[2]) != 5)

# Verifica que haya columnas
def test_sin_colums_vacias():
    assert not(bingo.sin_colums_vacias(mi_carton))

# Verifica que haya columnas llenas o filas vacias
def test_sin_colums_llenas_o_filas_vacias():
    assert not(bingo.sin_colums_llenas(mi_carton) and bingo.sin_filas_vacias(mi_carton))

# Verifica que haya filas con 3 celdas ocupadas consecutivas
def test_sin_3_celdas_ocupadas_consecutivas():
    assert not(bingo.sin_3_celdas_ocupadas_consecutivas(mi_carton))

# Verifica que haya filas con 3 celdas vacias consecutivas
def test_sin_3_celdas_vacias_consecutivas():
    assert not(bingo.sin_3_celdas_vacias_consecutivas(mi_carton))

# Verifica que no haya exactamente 3 columnas son solo una columna ocupada
def test_3_colums_con_1_celda_ocupada():
    assert bingo.cant_colums_con_1_celda_ocupada(mi_carton) != 3

# Verifica que las celdas ocupadas no esten en el rango de 1 a 90
def test_celdas_ocupadas_1_a_90():
    assert not(bingo.celdas_ocupadas_1_a_90(mi_carton))

# Verifica que las celdas por columnas no esten en rangos crecientes de 10 en 10
def test_mayores_a_la_derecha():
    assert not(bingo.mayores_a_la_derecha(mi_carton))

# Verifica que las celdas de las columnas no vayan creciendo de valor para abajo
def test_mayores_abajo():
    assert not(bingo.mayores_abajo(mi_carton))

# Verifica que haya numeros repetidos en el carton
def test_sin_numeros_repeditos():
    assert not(bingo.sin_numeros_repeditos(mi_carton))
