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

# Cuenta la cantidad de celdas ocupadas en una fila
def contar_celdas_ocupadas_en_fila(mi_fila):
    contador = 0
    for celda in mi_fila:
        if celda > 0:
            contador += 1
    return contador

# Retorna True si no hay columnas vacias, False en caso contrario
def sin_colums_vacias(mi_carton):
    for columna in range(9):
        if not(mi_carton[0][columna] or mi_carton[1][columna] or mi_carton[2][columna]):
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

# Retorna True si todos los numeros van de menor a mayor horizontalmente, False en caso contrario
def mayores_a_la_derecha(mi_carton):
    for columna in range(8):
        ma = max(mi_carton[0][columna], mi_carton[1][columna], mi_carton[2][columna])

        l = []
        for fila in range(3):
            if mi_carton[fila][columna + 1] != 0:
                l.append(mi_carton[fila][columna + 1])
        mi = min(l)

        if ma > mi:
            return False
    return True

# Retorna True si todos los numeros van de menor a mayor verticalmente en una columna, False en caso contrario
def mayores_abajo(mi_carton):
    for columna in range(9):
        if mi_carton[0][columna] != 0:
            if mi_carton[1][columna] != 0:
                if mi_carton[0][columna] > mi_carton[1][columna]:
                    return False
            if mi_carton[2][columna] != 0:
                if mi_carton[0][columna] > mi_carton[2][columna]:
                    return False

        if mi_carton[1][columna] != 0:
            if mi_carton[2][columna] != 0:
                if mi_carton[1][columna] > mi_carton[2][columna]:
                    return False
    return True

# Retorna True si no hay numeros repetido, False en caso contrario
def sin_numeros_repeditos(mi_carton):
    aux = []
    for fila in mi_carton:
        for celda in fila:
            if celda != 0:
                aux.append(celda)

    if len(aux) != len(set(aux)):
        return False

    return True

def sin_colums_llenas(mi_carton):
    for columna in range(9):
        if mi_carton[0][columna] and mi_carton[1][columna] and mi_carton[2][columna]:
            return False
    return True

def sin_3_celdas_ocupadas_consecutivas(mi_carton):
    for fila in mi_carton:
        contador = 0
        for celda in fila:
            if celda == 0:
                contador = 0
            else:
                contador += 1
            if contador == 3:
                return False
    return True

def sin_3_celdas_vacias_consecutivas(mi_carton):
    for fila in mi_carton:
        contador = 0
        for celda in fila:
            if celda != 0:
                contador = 0
            else:
                contador += 1
            if contador == 3:
                return False
    return True
