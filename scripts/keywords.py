nombre_archivo = input("Escribe el nombre del archivo XML: ")

with open(nombre_archivo, "r", encoding="utf-8") as archivo:
    contenido = archivo.read()

inicio = contenido.find("<abstract>")
fin = contenido.find("</abstract>")

if inicio != -1 and fin != -1:
    resumen = contenido[inicio + len("<abstract>"):fin]
else:
    resumen = ""

# Pasar a minúsculas y separar en palabras
palabras = resumen.lower().split()

# Palabras comunes a ignorar
palabras_comunes = ["el", "la", "los", "las", "y", "de", "del", "un", "una", "con", "para", "en", "por", "a", "al", "se"]

# Contar frecuencia de palabras
frecuencia = {}
for palabra in palabras:
    palabra = palabra.strip(".,;:()[]\"'")  # quitar signos de puntuación
    if palabra and palabra not in palabras_comunes:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1

# Lista de las 10 palabras más frecuentes
keywords = sorted(frecuencia, key=frecuencia.get, reverse=True)[:10]

print("\nKeywords:", keywords)
