def carton():
    #carton = (
    #    (1,0,0,1,1,0,1,0,1),
    #    (0,1,1,1,0,1,1,1,1),
    #    (0,1,0,0,1,0,0,1,0)
    #)

    carton = (
        (0,11,0,32,44,0,62,73,0),
        (8,0,25,38,0,56,0,0,80),
        (0,17,29,0,47,0,67,0,88)
    )
    return carton

# Cuenta la cantidad de celdas ocupadas
def contar_celdas_ocupadas(mi_carton):
    contador = 0
    for fila in mi_carton:
        for celda in fila:
            if celda > 0:
                contador += 1
    return contador

# Retorna True si no hay columnas vacias, False en caso contrario
def sin_colums_vacias(mi_carton):
    for i in range(9):
        if not(mi_carton[0][i] or mi_carton[1][i] or mi_carton[2][i]):
            return False
    return True

# Retorna True si no hay filas vacias, False en caso contrario
def sin_filas_vacias(mi_carton):
    for fila in mi_carton:
        sum = 0
        for celda in fila:
            sum += celda
        if sum == 0:
            return False
    return True

# Retorna True si las celdas ocupadas se encuentran entre 1 y 90, False en caso contrario
def celdas_ocupadas_1_a_90(mi_carton):
    for fila in mi_carton:
        for celda in fila:
            if not(celda >= 0 and celda <= 90):
                return False
    return True
