from jinja2 import Template
from bingo import generar_carton

template = Template(open("src/plantilla.j2").read())

file = open("bingo.html", "w")
file.write(template.render(carton=generar_carton()))
file.close()
