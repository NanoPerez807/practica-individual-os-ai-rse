# Práctica Individual de Open Science and AI in Research Software Engineering

Este proyecto realiza un análisis sobre 10 artículos científicos de acceso abierto que fueron obtenidos de arXiv y posteriormente se procesaron con Grobid para generar los archivos XML, que se usan como entrada para los scripts.

---

# Estructura del repositorio

```
.
├── papers/           # Archivos XML 
├── scripts/          # Scripts de análisis
│   ├── figures.py
│   ├── keywords.py
│   └── links.py
├── resultados/       # Resultados generados por los scripts
├── pyproject.toml    # Configuración del entorno con Poetry
├── poetry.lock
├── LICENSE
└── README.md
```

---

# Descripción de los scripts

## 1. Contador de figuras

Script: `scripts/figures.py`

Este script recorre los archivos XML y cuenta el número de apariciones de la etiqueta `<figure>` en cada artículo.

El resultado se visualiza mediante un gráfico de barras que muestra el número de figuras por artículo.

Resultado generado:

```
resultados/figuras.png
```

---

## 2. Nube de palabras clave

Script: `scripts/keywords.py`

Para cada archivo XML se extrae el contenido de la etiqueta `<abstract>` y se cuentan las frecuencias de cada palabra para generar una nube de palabras que muestra las palabras más relevantes del abstract.

Resultados generados:

```
resultados/nube_<nombre_del_articulo>.png
```
---

## 3. Listado de enlaces

Script: `scripts/links.py`

Este script busca enlaces dentro de los archivos XML y los lista.

Resultado generado:

```
resultados/enlaces.txt
```

---

# Instalación del entorno

El proyecto utiliza Poetry para la gestión de dependencias y del entorno virtual.

## Instalar Poetry

https://python-poetry.org/docs/#installation

## Instalar dependencias

Desde la raíz del proyecto:

```
poetry install
```

## Activar el entorno

```
poetry env activate
(devolverá el comando con la ruta a ejecutar, se debe por tanto ejecutar literalmente lo que devuelva el comando)
```

---

# Ejecución de los scripts

Una vez activado el entorno, los scripts pueden ejecutarse desde la raíz del proyecto.

Generar gráfico de figuras:

```
python scripts/figures.py
```

Generar nubes de palabras:

```
python scripts/keywords.py
```

Extraer enlaces:

```
python scripts/links.py
```

Los resultados se guardarán automáticamente en la carpeta `resultados/`.

---

# Validación de resultados

Se realizaron comprobaciones manuales para verificar que los resultados generados por los scripts son correctos.

## Palabras clave

Las nubes de palabras se compararon manualmente con el contenido del `<abstract>` de cada archivo XML para comprobar que los términos más frecuentes coinciden con los del resumen.

## Figuras

El número de figuras se verificó buscando manualmente la etiqueta `<figure>` dentro de los archivos XML.

## Enlaces

Los enlaces extraídos se compararon con los enlaces presentes en el texto y en los atributos del XML. Y, debido a que se habían ciertos enlaces que no eran del propio PDF, sino que se generaban automaticamente con la creación del XML en Grobid, se estableció una condición para no tenerlos en cuenta. Concretamente se han descartado: "https://github.com/kermitt2/grobid", "https://raw.githubusercontent.com/kermitt2/grobid/master/grobid-home/schemas/xsd/Grobid.xsd", "http://www.tei-c.org/ns/1.0", "http://www.w3.org/2001/XMLSchema-instance", "http://www.w3.org/1999/xlink".21q

---

# Limitaciones

Las dificultades que he encontrado a la hora de programar por no tener conocimiento total del lenguaje de programación implica varias limitaciones:

* El conteo de figuras se basa en la aparición de la cadena `<figure>` y puede incluir elementos que no correspondan exactamente a figuras visibles.
* La extracción del abstract depende de que el XML contenga correctamente la etiqueta `<abstract>`.
* La lista de palabras comunes que se utiliza en la creación de la nube de palabras clave es limitada.
* La extracción de enlaces se basa en expresiones regulares, por lo que algunos formatos poco comunes podrían no detectarse.


---

# Licencia

Este proyecto se distribuye bajo la licencia MIT.
