import os
from jinja2 import Environment, FileSystemLoader


env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('index.html')


practicas = []
for archivo in os.listdir("material/practicas"):
    practicas += [archivo]

teoricas = []
for archivo in os.listdir("material/teoricas"):
    teoricas += [archivo]

teoricas.sort()
practicas.sort()

output = template.render({"teoricas": teoricas, "practicas": practicas})

os.system("mkdir -p _build")
with open("_build/index.html", "w") as f:
    f.write(output)

with open("_build/.nojekyll", "w") as _:
    pass
