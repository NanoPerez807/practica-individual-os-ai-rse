import os
import re

papers = "practica-individual-os-ai-rse/papers"
xmls = [f for f in os.listdir(papers) if f.endswith(".xml")]

with open("practica-individual-os-ai-rse/resultados/enlaces.txt", "w", encoding="utf-8") as out:

    for nombre_archivo in xmls:

        with open(f"{papers}/{nombre_archivo}", "r", encoding="utf-8") as archivo:
            text = archivo.read()

        out.write(f"{nombre_archivo}:\n")

        enlaces = set(re.findall(r'https?://[^\s<>"\]]+', text))

        for link in enlaces:
            if link != "https://github.com/kermitt2/grobid" and link != "https://raw.githubusercontent.com/kermitt2/grobid/master/grobid-home/schemas/xsd/Grobid.xsd" and link != "http://www.tei-c.org/ns/1.0" and link != "http://www.w3.org/2001/XMLSchema-instance" and link != "http://www.w3.org/1999/xlink":
                out.write(link + "\n")
        out.write("\n")

print("Enlaces guardados en 'enlaces.txt'")
