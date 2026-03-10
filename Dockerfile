FROM python:3.9

MAINTAINER fernando.perezalo@alumnos.upm.es

WORKDIR /practica-individual-os-ai-rse

COPY scripts/ ./scripts/
COPY papers/ ./papers/
RUN mkdir -p resultados

# Instalar dependencias
RUN pip install matplotlib wordcloud

CMD ["python", "scripts/figures.py"]
