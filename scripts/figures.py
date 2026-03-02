import os
import matplotlib.pyplot as plt

papers = "../papers"

xmls = [f for f in os.listdir(papers) if f.endswith(".xml")]

nombres = []
num_figuras_lista = []

for nombre_archivo in xmls:
    with open(f"{papers}/{nombre_archivo}", "r", encoding="utf-8") as archivo:
        contenido = archivo.read()

    num_figuras = contenido.count("<figure")
    nombres.append(nombre_archivo)
    num_figuras_lista.append(num_figuras)


plt.figure(figsize=(10, 6))
plt.bar(nombres, num_figuras_lista, color='skyblue')
plt.xticks(rotation=45, ha='right')
plt.ylabel("Número de figuras")
plt.xlabel("Papers")
plt.title("Número de figuras por artículo")
plt.tight_layout()
