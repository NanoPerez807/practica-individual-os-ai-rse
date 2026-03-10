FROM python:3.9

MAINTAINER fernando.perezalo@alumnos.upm.es

WORKDIR /practica-individual-os-ai-rse

COPY scripts/ ./scripts/
COPY papers/ ./papers/
RUN mkdir -p resultados

# Instalamos dependencias
RUN pip install matplotlib wordcloud

# Lanzar un shell para luego poder elegir el script
CMD ["/bin/bash"]
