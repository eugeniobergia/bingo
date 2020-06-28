import os
import sys
sys.path.append(os.getcwd())
from src.bingo import generar_carton
from jinja2 import Template

template = Template(open("web/plantilla.j2").read())

file = open("bingo.html", "w")
file.write(template.render(carton = generar_carton()))
file.close()
