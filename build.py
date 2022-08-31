import os
from jinja2 import Environment, FileSystemLoader


env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('index.html')

archivos = []
for archivo in os.listdir("material"):
    archivos += [archivo]

archivos.sort()

output = template.render({"archivos": archivos})

os.system("mkdir -p _build")
with open("_build/index.html", "w") as f:
    f.write(output)

with open("_build/.nojekyll", "w") as _:
    pass
