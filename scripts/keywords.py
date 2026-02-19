archivo = input("Escribe el nombre del archivo XML")

with open(archivo, "r", encoding="utf-8") as f:
    contenido = f.read()

inicio = contenido.find("<abstract>")
fin = contenido.find("</abstract>")

if inicio != -1 and fin != -1:
    abstract = contenido[inicio + len("<abstract>"):fin]
else:
    abstract = None
