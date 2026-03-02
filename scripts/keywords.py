import os
import re

papers = "../papers"

xmls = [f for f in os.listdir(papers) if f.endswith(".xml")]

palabras_comunes = ["and","the","of","in","to","with","for","on","by","an","is","are","as","at","from","that","this","it","be","or","was","were","which"]

for nombre_archivo in xmls:
    with open(f"{papers}/{nombre_archivo}", "r", encoding="utf-8") as archivo:
        contenido = archivo.read()

    inicio = contenido.find("<abstract>")
    fin = contenido.find("</abstract>")

    if inicio == -1 or fin == -1:
        continue

    resumen = contenido[inicio + len("<abstract>"):fin]
    resumen = re.sub(r"<[^>]+>", " ", resumen)

    palabras = resumen.lower().split()

    frecuencia = {}
    for palabra in palabras:
        palabra = palabra.strip(".,;:()[]\"'")
        if palabra and palabra not in palabras_comunes:
            if palabra in frecuencia:
                frecuencia[palabra] += 1
            else:
                frecuencia[palabra] = 1

    nube = WordCloud(width=800, height=400, background_color="white")
    nube.generate_from_frequencies(frecuencia)

    nube.to_file(f"../resultados/nube_{nombre_archivo.replace('.xml', '.png')}")

    print(f"Nube generada: nube_{nombre_archivo.replace('.xml', '.png')}")
