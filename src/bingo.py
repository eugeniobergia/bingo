import random
import math

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
    x = 0
    y = 9
    for columna in range(9):
        for fila in range(3):
            if mi_carton[fila][columna] != 0:
                if not(x <= mi_carton[fila][columna] <= y):
                    return False
        x += 10
        y += 10
        if y == 89:
            y = 90
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
    aux = mi_carton[0] + mi_carton[1] + mi_carton[2]

    if len(set(aux)) != 16:
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

def cant_colums_con_1_celda_ocupada(mi_carton):
    contador = 0
    for columna in range(9):
        contador2 = 0
        for fila in range(3):
            if mi_carton[fila][columna] != 0:
                contador2 += 1
        if contador2 == 1:
            contador += 1

    return contador

def matriz_de_3x9(mi_carton):
    if len(mi_carton) != 3:
        return False
    for fila in mi_carton:
        if len(fila) != 9:
            return False
    return True

def intento_carton():
    contador = 0

    carton = [
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]
    ]
    numerosCarton = 0

    while numerosCarton < 15:
        contador += 1
        if contador == 50 :
            return intento_carton()
        numero = random.randint(1, 90)

        columna = math.floor(numero / 10)
        if columna == 9:
            columna = 8
        huecos = 0
        for i in range(3):
            if carton[i][columna] == 0:
                huecos += 1
            if carton[i][columna] == numero:
                huecos = 0
                break
        if(huecos < 2):
            continue

        fila = 0
        for j in range(3):
            huecos = 0
            for i in range(9):
                if carton[fila][i] == 0:
                    huecos += 1
            if huecos < 5 or carton[fila][columna] != 0:
                fila += 1
            else:
                break
        if fila == 3:
            continue

        carton[fila][columna] = numero
        numerosCarton += 1
        contador = 0

    for x in range(9):
        huecos = 0
        for y in range(3):
            if carton[y][x] == 0:
                huecos += 1
        if huecos == 3:
            return intento_carton()

    return carton

def generar_carton():
    while True:
        carton = intento_carton()
        if(contar_celdas_ocupadas(carton) == 15
        and contar_celdas_ocupadas_en_fila(carton[0]) == 5
        and contar_celdas_ocupadas_en_fila(carton[1]) == 5
        and contar_celdas_ocupadas_en_fila(carton[2]) == 5
        and sin_colums_vacias(carton)
        and sin_filas_vacias(carton)
        and celdas_ocupadas_1_a_90(carton)
        and mayores_a_la_derecha(carton)
        and mayores_abajo(carton)
        and sin_numeros_repeditos(carton)
        and sin_colums_llenas(carton)
        and sin_3_celdas_ocupadas_consecutivas(carton)
        and sin_3_celdas_vacias_consecutivas(carton)
        and cant_colums_con_1_celda_ocupada(carton) == 3
        and matriz_de_3x9(carton)):
            break
    return carton

def main():
    carton = generar_carton()
    for fila in carton:
        print(fila)

if __name__ == "__main__":
    main()
