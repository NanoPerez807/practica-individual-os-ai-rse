# Práctica Individual de Open Science and AI in Research Software Engineering

Este proyecto realiza un análisis sobre 10 artículos científicos de acceso abierto que fueron obtenidos de arXiv y posteriormente se procesaron con Grobid para generar los archivos XML, que se usan como entrada para los scripts.

---

# Estructura del repositorio

```
.
├── papers/           # Aquí se encuentran los archivos XML, para comprobar con otros archivos XML, simplemente se han de insertar en este directorio 
├── scripts/          # Scripts de análisis
│   ├── figures.py
│   ├── keywords.py
│   └── links.py
├── resultados/       # Resultados generados por los scripts
├── pyproject.toml    # Configuración del entorno con Poetry
├── poetry.lock
├── LICENSE
├── run.sh            # Script para ejecutar todo de manera automática
└── README.md
```

---

# Descripción de los scripts

## 1. Contador de figuras

Script: `figures.py`

Este script recorre los archivos XML y cuenta el número de apariciones de la etiqueta `<figure>` en cada artículo.

El resultado se visualiza mediante un gráfico de barras que muestra el número de figuras por artículo.

Resultado generado:

```
resultados/figuras.png
```

---

## 2. Nube de palabras clave

Script: `keywords.py`

Para cada archivo XML se extrae el contenido de la etiqueta `<abstract>` y se cuentan las frecuencias de cada palabra para generar una nube de palabras que muestra las palabras más relevantes del abstract.

Resultados generados:

```
resultados/nube_<nombre_del_articulo>.png
```
---

## 3. Listado de enlaces

Script: `links.py`

Este script busca enlaces dentro de los archivos XML y los lista.

Resultado generado:

```
resultados/enlaces.txt
```

---

# Instalación y ejecución

El proyecto puede ejecutarse de dos maneras: usando Poetry (entorno local) o usando Docker (contenedor). Se explican ambas a continuación.
## Opción 1: Usando Poetry (entorno local)

Esta opción permite ejecutar los scripts directamente en tu máquina usando un entorno virtual gestionado con Poetry.

### 1. Instalar Poetry

Sigue las instrucciones oficiales en:

https://python-poetry.org/docs/#installation

### 2. Instalar dependencias

Desde la raíz del proyecto, ejecuta:

```
poetry install
```

## Opción 2: Usando Docker

Esta opción permite ejecutar los scripts dentro de un contenedor Docker, sin necesidad de instalar dependencias en tu máquina local.

### 1. Instalar Docker

Sigue las instrucciones oficiales según tu sistema operativo:

https://docs.docker.com/get-docker/

### 2. Construir la imagen

Desde la raíz del proyecto, ejecuta:

```
docker build -t practica-os-ai-rse .
```

## Ejecutar scripts

Se ha preparado un script para automatizar la ejecución de los scripts.

Para ejecutarlo:

previamente hay que darle permiso de ejecución:

```
chmod +x run.sh
```

y después ejecutarlo con:

```
./run.sh poetry
```
o bien 

```
./run.sh docker
```
# Validación de resultados

Se realizaron comprobaciones manuales para verificar que los resultados generados por los scripts son correctos.

## Palabras clave

Las nubes de palabras se compararon manualmente con el contenido del `<abstract>` de cada archivo XML para comprobar que los términos más frecuentes coinciden con los del resumen.

## Figuras

El número de figuras se verificó buscando manualmente la etiqueta `<figure>` dentro de los archivos XML.

## Enlaces

Los enlaces extraídos se compararon con los enlaces presentes en el texto y en los atributos del XML. Y, debido a que habían ciertos enlaces que no eran del propio PDF, sino que se generaban con la creación del XML en Grobid, se estableció una condición para no tenerlos en cuenta. Concretamente se han descartado: "https://github.com/kermitt2/grobid", "https://raw.githubusercontent.com/kermitt2/grobid/master/grobid-home/schemas/xsd/Grobid.xsd", "http://www.tei-c.org/ns/1.0", "http://www.w3.org/2001/XMLSchema-instance", "http://www.w3.org/1999/xlink".

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
