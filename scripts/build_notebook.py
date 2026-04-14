import os
import json

def create_markdown_cell(source_text):
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": [line + '\n' for line in source_text.split('\n')]
    }

def create_code_cell(source_text):
    lines = source_text.split('\n')
    source = [line + '\n' for line in lines[:-1]] + [lines[-1]] if lines else []
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": source
    }

def build_notebook():
    notebook = {
        "cells": [],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "name": "python",
                "version": "3.10"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }

    # Intro Cell
    intro_md = """# HackODS UNAM 2026: Pipeline de Datos y Análisis Exploratorio (Equipo linuxitOS)

Este notebook contiene el pipeline ETL (Extract, Transform, Load) centralizado que alimenta el [Dashboard ODS 1 x ODS 6](https://github.com/linuxitOS-hackODS/linuxitOS-HackODS-UNAM/tree/main/dashboard).
    
El objetivo principal es demostrar la transparencia y reproducibilidad técnica de nuestro análisis de datos geoespaciales, sociodemográficos y financieros. Para facilitar la evaluación de nuestro repositorio sin perder la comprensión de nuestra arquitectura técnica, hemos consolidado la ejecución en un orquestador principal (`main.py`).

## Arquitectura del Pipeline ETL (7 Módulos)
Nuestro procesamiento de datos está dividido en 7 fases especializadas que se ejecutan de manera secuencial. A continuación se describe el propósito de cada script de la carpeta `scripts/`:

1. **`siods_extractor.py`**: Recolección de métricas de infraestructura municipal desde SIODS.
2. **`analyze_iter.py`**: Depuración demográfica y cálculo de ruralidad desde el ITER (INEGI).
3. **`clean_coneval.py`**: Normalización de Índices de Rezago Social y Pobreza (CONEVAL).
4. **`merge_inegi_coneval.py`**: Integración o *merge* de la base demográfica.
5. **`merge_shcp.py`**: Cruce financiero con el presupuesto federal (FAISMUN/FORTAMUN).
6. **`merge_conagua.py`**: Cruce hídrico de disponibilidad por regiones hidrológicas (CONAGUA).
7. **`simplify_geojson.py`**: Optimización algorítmica geoespacial (Douglas-Peucker) para reducir los polígonos de cuencas de 18MB a 1MB y garantizar alto rendimiento web.

## Ejecución del Orquestador
La celda de código a continuación corresponde a nuestro `main.py`, el cual invoca secuencialmente cada uno de estos módulos, construye el dataset analítico y lo exporta para consumo nativo en el framework Quarto."""
    
    notebook["cells"].append(create_markdown_cell(intro_md))

    # Add main.py code cell
    try:
        with open('main.py', 'r', encoding='utf-8') as f:
            code_text = f.read()
            
        # We append a simple execution line at the end so judges can just shift+enter
        code_text += '\n# Para ejecutar el pipeline completo desde esta libreta, \n# descomente la siguiente línea si el entorno es adecuado:\n# main()\n'
        notebook["cells"].append(create_code_cell(code_text))
    except Exception as e:
        err_msg = f"# ERROR LEYENDO main.py: {str(e)}"
        notebook["cells"].append(create_code_cell(err_msg))

    conclusion_md = """## Conclusión del Pipeline

Al ejecutar el orquestador `main.py`, se generan los datasets limpios y el archivo geoespacial optimizado en la carpeta `datos/`. Estos archivos son la columna vertebral y fuente de la verdad para nuestro tablero de Quarto.

El archivo analítico final consolidado es: `datos/final_merged_data.csv`."""
    notebook["cells"].append(create_markdown_cell(conclusion_md))

    out_path = "notebooks/001_Pipeline_ETL_ODS.ipynb"
    
    # Ensure dir exists
    os.makedirs("notebooks", exist_ok=True)
    
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, ensure_ascii=False, indent=2)
    
    print(f"Jupyter Notebook generado exitosamente en: {out_path}")

if __name__ == "__main__":
    if not os.path.exists("main.py"):
        print("Ejecuta este script desde la raíz del repositorio.")
    else:
        build_notebook()
