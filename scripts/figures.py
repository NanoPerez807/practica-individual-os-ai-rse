nombre_archivo = input("Escribe el nombre del archivo XML: ")

with open(nombre_archivo, "r", encoding="utf-8") as archivo:
    contenido = archivo.read()

num_figuras = contenido.count("<figure")

print("Número de figuras en el artículo:", num_figuras)
