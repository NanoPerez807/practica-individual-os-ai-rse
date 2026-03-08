import os

papers = "../papers"
xmls = [f for f in os.listdir(papers) if f.endswith(".xml")]

with open("../resultados/enlaces.txt", "w", encoding="utf-8") as out:

    for nombre_archivo in xmls:

        with open(f"{papers}/{nombre_archivo}", "r", encoding="utf-8") as archivo:
            text = archivo.read()

        out.write(f"{nombre_archivo}:\n")

        i = 0
        while True:
            i = text.find('target="', i)
            if i == -1:
                break
            i += len('target="')
            j = text.find('"', i)
            link = text[i:j]

            if link.startswith("http") and link != "https://github.com/kermitt2/grobid":
                out.write(link + "\n")

            i = j

        out.write("\n")

print("Enlaces guardados en 'enlaces.txt'")
