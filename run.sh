#!/bin/bash

# Script para ejecutar los scripts con Poetry o Docker
# Uso:
#   ./run_all.sh poetry   -> ejecuta con Poetry
#   ./run_all.sh docker   -> ejecuta dentro del contenedor de Docker

modo=$1

if [ "$modo" == "poetry" ]; then
    echo "Ejecutando con Poetry..."

    # Activar el entorno de Poetry
    source $(poetry env info --path)/bin/activate

    # Entrar en scripts/ para ejecutar desde allí
    cd scripts

    echo "Ejecutando figures.py..."
    python figures.py

    echo "Ejecutando keywords.py..."
    python keywords.py

    echo "Ejecutando links.py..."
    python links.py

    cd ..
    echo "Scripts ejecutados correctamente."

elif [ "$modo" == "docker" ]; then
    echo "Ejecutando con Docker..."

    # Build de la imagen (si no está construida, se puede forzar con --build)
    docker build -t practica-os-ai-rse .

    # Ejecutar scripts dentro del contenedor
    docker run --rm -it \
        -v $(pwd)/resultados:/practica-individual-os-ai-rse/resultados \
        practica-os-ai-rse \
        bash -c "cd scripts && python scripts/figures.py && python scripts/keywords.py && python scripts/links.py"

    echo "Scripts ejecutados con correctamente."

else
    echo "Modo no reconocido. Usa:"
    echo "  ./run_all.sh poetry"
    echo "  ./run_all.sh docker"
fi
