nombre_archivo = input("Escribe el nombre del archivo XML: ")

with open(nombre_archivo, "r", encoding="utf-8") as archivo:
    contenido = archivo.read()

palabras = contenido.split()

enlaces = []

for palabra in palabras:
    if palabra.startswith("http://") or palabra.startswith("https://"):
        # Limpiar posibles caracteres finales
        enlace = palabra.strip(".,;:()[]\"'") # quitar signos de puntuación
        enlaces.append(enlace)

print("Enlaces encontrados en el artículo:")
for enlace in enlaces:
    print(enlace)
