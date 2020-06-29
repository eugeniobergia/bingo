[![Build Status](https://travis-ci.com/eugeniobergia/bingo.svg?branch=master)](https://travis-ci.com/eugeniobergia/bingo)
[![Coverage Status](https://coveralls.io/repos/github/eugeniobergia/bingo/badge.svg?branch=master)](https://coveralls.io/github/eugeniobergia/bingo?branch=master)
# Bingo

Código en Python 3 que genera un cartón de bingo.
Escrito para Adaptación Del Ambiente De Trabajo, Instituto Politécnico Superior "Gral. San Martín", 2020.

## Reglas
Se considara un cartón válido al que cumple con las siguientes condiciones:
* Cada carton es una matrix de 3 x 9.
* Los números del carton se encuentran en el rango 1 a 90.
* Cada columna de un carton (contando de izquierda a derecha) contiene numeros que van del 1 al 9, 10 al 19, 20 al 29 ..., 70 al 79 y 80 al 90.
* No hay números repetidos en el carton.
* Cada fila de un carton tiene exactamente 5 celdas ocupadas.
* Cada carton tiene 15 celdas ocupadas.
* Para una misma columna, sus números están ordenados de menor a mayor de arriba hacia abajo.
* No pueden existir columnas vacias.
* No pueden existir columnas con sus tres celdas ocupadas.
* Cada carton debe tener 3 y solo 3 columas con solo una celda ocupada.
* En una fila no existen más de dos celdas vacías consecutivas.
* En una fila no existen más de dos celdas ocupadas consecutivas.

## Uso
Para clonar el repositorio:
```
git clone https://github.com/eugeniobergia/bingo.git
```

Para generar un cartón por consola:
```
python bingo_cli.py
```
Para generar un html con un cartón visual:
```
python bingo_web.py
```
Nota: para distribuciones basadas en Debian utilizar `python3`

Para más información sobre cómo instalar o actualizar Python visite https://www.python.org/

## Ejemplo de salida
### Consola
```
$ python3 bingo_cli.py
[0, 0, 20, 0, 47, 57, 0, 71, 89]
[0, 11, 26, 0, 49, 0, 0, 72, 90]
[9, 17, 0, 32, 0, 59, 63, 0, 0]
```
### Web
```
$ python3 bingo_web.py
Generado "bingo.html".
```
![Ejemplo Bingo Web](https://github.com/eugeniobergia/bingo/blob/master/imagenes/ejemplo_web.png?raw=true)
