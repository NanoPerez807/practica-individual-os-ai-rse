xml_file = input("Escribe el nombre del archivo XML: ")
with open(xml_file, "r", encoding="utf-8") as f:
    text = f.read()

i = 0
while True:
    i = text.find('target="', i)
    if i == -1:
        break
    i += len('target="')
    j = text.find('"', i)
    link = text[i:j]
    if link.startswith("http") and link != "https://github.com/kermitt2/grobid":
        print(link)
    i = j
