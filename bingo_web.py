from jinja2 import Template
from src.bingo import generar_carton

template = Template(open("web/plantilla.j2").read())

file = open("bingo.html", "w")
file.write(template.render(carton = generar_carton()))
file.close()
print("Generado \"bingo.html\".")
