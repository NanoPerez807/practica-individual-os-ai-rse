FROM python:3.9

MAINTAINER fernando.perezalo@alumnos.upm.es

WORKDIR /practica-individual-os-ai-rse

# Copiamos los archivos de scripts y papers al contenedor
COPY scripts/ ./scripts/
COPY papers/ ./papers/

# Instalamos las dependencias necesarias
RUN pip install matplotlib wordcloud

# Definimos el comando por defecto al ejecutar el contenedor
CMD ["python", "scripts/figures.py"]
