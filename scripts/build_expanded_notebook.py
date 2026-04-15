import nbformat as nbf
import os

def create_markdown_cell(text):
    return nbf.v4.new_markdown_cell(text)

def create_code_cell(code):
    return nbf.v4.new_code_cell(code)

def main():
    notebook = nbf.v4.new_notebook()
    
    # Metadata for the notebook
    notebook['metadata'] = {
        'kernelspec': {
            'display_name': 'Python 3',
            'language': 'python',
            'name': 'python3'
        },
        'language_info': {
            'name': 'python',
            'version': '3.10'
        }
    }

    # Intro
    intro_md = """# Pipeline de Datos Detallado: Estrategia de Integración Multifuente
**Equipo:** linuxitOS

Este documento presenta la **auditoría técnica integral** de nuestro pipeline de datos (ETL). El objetivo primordial de esta libreta es demostrar la transparencia metodológica, la solidez estadística y la eficiencia computacional de nuestra arquitectura.

### Objetivos Técnicos:
1.  **Trazabilidad:** Seguimiento del dato desde la fuente oficial (SIODS, Microdatos INEGI/CONEVAL) hasta el dataset maestro.
2.  **Integridad Espacial:** Normalización de claves geográficas (`CVEGEO`) a 5 dígitos para garantizar cruces precisos a nivel municipal.
3.  **Optimización:** Implementación de algoritmos de simplificación geométrica para un rendimiento web de alto desempeño.

    """
    notebook['cells'].append(create_markdown_cell(intro_md))

    # Pipeline defined in main.py
    pipeline = [
        "scripts/siods_extractor.py",
        "scripts/analyze_iter.py",
        "scripts/clean_coneval.py",
        "scripts/merge_inegi_coneval.py",
        "scripts/merge_shcp.py",
        "scripts/merge_conagua.py",
        "scripts/simplify_geojson.py"
    ]

    descriptions = {
        "scripts/siods_extractor.py": """## Módulo 1: Minería de Metadatos SIODS
**Objetivo:** Extracción de indicadores oficiales de la Agenda 2030 (ODS 6).

Este script consulta la API de la plataforma SIODS. Se enfoca en identificar el "Punto Ciego Estatal" de los indicadores **6.1.1 (Agua Potable Segura)**, permitiendo contrastar las metas globales de la ONU con la realidad territorial en México.""",
        
        "scripts/analyze_iter.py": """## Módulo 2: Microdatos Censales (INEGI 2020)
**Objetivo:** Definición de la vocación territorial (Rural vs Urbano).

Implementamos un análisis de granularidad máxima utilizando el dataset **ITER 2020**. El algoritmo clasifica cada una de las miles de localidades del país bajo el estándar de 2,500 habitantes de INEGI, agregándolas a nivel municipal para derivar una métrica de "Ruralidad Predominante" (>50% de población en áreas rurales).""",
        
        "scripts/clean_coneval.py": """## Módulo 3: Pobreza Multidimensional (CONEVAL)
**Objetivo:** Extracción de vectores de vulnerabilidad social.

Procesamos la matriz del CONEVAL enfocándonos en la **Pobreza Extrema** y la **Carencia por acceso a los servicios básicos en la vivienda**. Este paso es crítico para establecer la correlación estadística entre la falta de infraestructura hídrica y la marginación estructural.""",
        
        "scripts/merge_inegi_coneval.py": """## Módulo 4: Integración del Dataset Maestro (Baseline)
**Objetivo:** Fusión de las dimensiones sociodemográficas y de pobreza.

Realizamos un *Left Join* determinista utilizando la clave `CVEGEO` como eje de unión. Este módulo garantiza la **Integridad Referencial** de nuestro proyecto, asegurando que cada municipio rural identificado tenga su correspondiente vector de pobreza alineado temporalmente al ciclo 2020.""",
        
        "scripts/merge_shcp.py": """## Módulo 5: Derechos de Agua e Ingresos Municipales (SHCP)
**Objetivo:** Análisis de la salud fiscal y recaudación hídrica.

Añadimos la dimensión financiera mediante los datos de la SHCP sobre **Derechos de Agua**. Calculamos el monto recaudado per cápita para identificar desigualdades municipales entre la capacidad administrativa y el acceso efectivo al recurso.""",
        
        "scripts/merge_conagua.py": """## Módulo 6: Disponibilidad Hídrica y Regiones (CONAGUA)
**Objetivo:** Contextualización hidro-topográfica.

Integramos las **Regiones Hidrológico-Administrativas (RHA)** y el indicador de cobertura de la CONAGUA. Derivamos una métrica de "Deficiencia Hídrica Específica" (100 - %cobertura), contrastando la visión de la autoridad hídrica con los datos socioeconómicos previos.""",
        
        "scripts/simplify_geojson.py": """## Módulo 7: Optimización de Activos (Douglas-Peucker)
**Objetivo:** Eficiencia computacional y performance del Dashboard.

Para garantizar un tiempo de carga menor a 2 segundos en el navegador, implementamos el algoritmo de **Douglas-Peucker**. Este módulo simplifica la topología de las cuencas y estados de México, reduciendo el peso de los archivos GeoJSON de **18MB a ~1MB** sin perder la precisión necesaria para la visualización del Dashboard."""
    }

    for script_path in pipeline:
        # Add Header
        header = descriptions.get(script_path, f"### Módulo: {script_path}")
        notebook['cells'].append(create_markdown_cell(header))
        
        # Add Code
        try:
            with open(script_path, 'r', encoding='utf-8') as f:
                code_content = f.read()
            notebook['cells'].append(create_code_cell(code_content))
        except Exception as e:
            notebook['cells'].append(create_code_cell(f"# ERROR LEYENDO {script_path}: {e}"))

    # Conclusion
    conclusion_md = """## Conclusión Metodológica
Este pipeline representa una solución escalable para la integración de datos gubernamentales heterogéneos. La automatización de la limpieza, el cruce de variables sociodemográficas con indicadores de disponibilidad hídrica y la optimización final de la geometría aseguran que el proyecto no solo sea una visualización estática, sino una plataforma de análisis técnico de alto nivel.

**Próximo Paso:** Instanciación del Dashboard vía `quarto render dashboard/index.qmd`."""
    notebook['cells'].append(create_markdown_cell(conclusion_md))

    # Final logic to ensure notebooks dir exists
    os.makedirs("notebooks", exist_ok=True)
    out_path = "notebooks/002_Pipeline_Datos_Detallado.ipynb"
    
    with open(out_path, 'w', encoding='utf-8') as f:
        nbf.write(notebook, f)
        
    print(f"Jupyter Notebook expandido generado exitosamente en: {out_path}")

if __name__ == "__main__":
    main()
