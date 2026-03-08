import os
import re

papers = "../papers"
xml_files = [f for f in os.listdir(papers) if f.endswith(".xml")]

with open("../resultados/enlaces.txt", "w", encoding="utf-8") as out:

    for nombre_archivo in xml_files:

        with open(f"{papers}/{nombre_archivo}", "r", encoding="utf-8") as archivo:
            text = archivo.read()

        out.write(f"{nombre_archivo}:\n")

        enlaces = set(re.findall(r'https?://[^\s<>"\]]+', text))

        for link in enlaces:
            if link != "https://github.com/kermitt2/grobid":
                out.write(link + "\n")

        out.write("\n")

print("Enlaces guardados en '../resultados/enlaces.txt'")
