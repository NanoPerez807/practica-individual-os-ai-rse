from wordcloud import WordCloud
import re

nombre_archivo = input("Escribe el nombre del archivo XML: ")

with open(nombre_archivo, "r", encoding="utf-8") as archivo:
    contenido = archivo.read()

inicio = contenido.find("<abstract>")
fin = contenido.find("</abstract>")

if inicio != -1 and fin != -1:
    resumen = contenido[inicio + len("<abstract>"):fin]
else:
    resumen = ""

resumen = re.sub(r"<[^>]+>", " ", resumen)

palabras = resumen.lower().split()

# Palabras comunes a ignorar
palabras_comunes = ["and","the","of","in","to","with","for","on","by","an","is","are","as","at","from","that","this","it","be","or","was","were","which","by"]


frecuencia = {}
for palabra in palabras:
    palabra = palabra.strip(".,;:()[]\"'")  # quitar signos de puntuación
    if palabra and palabra not in palabras_comunes:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1


# Generar nube de palabras
if frecuencia:
    nube = WordCloud(width=800, height=400, background_color="white")
    nube.generate_from_frequencies(frecuencia)
    archivo_salida = f"nube_palabras_{nombre_archivo.replace('.xml','')}.png"
    nube.to_file(archivo_salida)
    print(f"Nube de palabras guardada en '{archivo_salida}'")
else:
    print("No se pudo generar la nube de palabras (abstract vacío o solo palabras comunes).")
