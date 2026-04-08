# linuxitOS - HackODS UNAM

[![HackODS UNAM](https://img.shields.io/badge/HackODS-UNAM-gold.svg)](https://www.hackods.unam.mx/)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Quarto](https://img.shields.io/badge/Quarto-Dashboard-9cf.svg)](https://quarto.org/)

## 1. Datos del Equipo
- **Equipo:** linuxitOS
- **Integrantes:** 
  - Jesús Sebastián Vázquez Zarco
  - Alejandra Naomi Muciño Hernández
  - Victor Federico Caldera Arellano
- **ODS Elegidos:** ODS 6 (Agua limpia y saneamiento) interconectado de manera transveral con el ODS 1 (Fin de la pobreza).

---

## 2. Descripción y Planteamiento del Problema
**Pregunta Central:**  
*¿Cómo el déficit de infraestructura hídrica profundiza sistemáticamente la pobreza en el México rural frente a los grandes centros urbanos?*

Este proyecto demuestra estadísticamente que el "promedio" estatal o nacional de acceso al agua es un "espejismo". A través del análisis exploratorio y cruce espacial de microdatos censales, evidenciamos cómo la dispersión sociodemográfica rural castiga a miles de municipios desconectados de las grandes redes de infraestructura pública, convirtiendo la carencia de agua en el ancla principal de la pobreza en México.

---

## 3. Fuentes de Datos Oficiales

> **[Consultar Metadatos y Diccionarios de Datos aquí](datos/README.md)**
> *Nota: Toda la información técnica de los datasets (diccionario de variables, fechas de extracción, enlaces primarios y licencias de uso) se encuentra documentada a detalle en el README de la carpeta de datos.*

---

## 4. Guía de Reproducibilidad Técnica

**Entorno de Ejecución:**
- **Python:** `>= 3.10`
- **Quarto CLI:** Instalado a nivel sistema operativo.

### Comandos de Instalación y Pipeline ETL
Ejecutar los siguientes comandos en terminal:

```bash
# 1. Clonar el repositorio
git clone https://github.com/linuxitOS-hackODS/linuxitOS-HackODS-UNAM.git
cd linuxitOS-HackODS-UNAM

# 2. Crear y activar entorno virtual de Python
python3 -m venv venv
source venv/bin/activate  # En sistemas Linux/Mac
# venv\Scripts\activate   # En sistemas Windows

# 3. Descargar e instalar dependencias del core
pip install -r requirements.txt

# 4. Compilar Pipeline de Datos (Extracción, Limpieza y Cruce)
python scripts/siods_extractor.py
python scripts/analyze_iter.py
python scripts/clean_coneval.py
python scripts/merge_inegi_coneval.py
python scripts/merge_shcp.py
python scripts/merge_conagua.py
python scripts/simplify_geojson.py

# 5. Procesar y visualizar el Dashboard Analítico (En vivo)
quarto preview dashboard/index.qmd
```

---

## 5. Arquitectura del Proyecto
- `datos/`: Repositorio inmutable para los datasets en crudo (*raw*) y salida del dataset unificado (`final_merged_data.csv`).
- `scripts/`: Módulos de Python responsables del flujo ETL (Extract, Transform, Load) bajo estándares de código limpio.
- `dashboard/`: Código fuente del tablero analítico (`index.qmd`), configuraciones topológicas (`_quarto.yml`) y UI/CSS personalizado (`styles.css`).
- `ai-log.md`: Declaratoria de trazabilidad, documentando las interacciones tecnológicas y éticas de apoyo de IA durante el Hackathon.
- `LICENSE`: Este trabajo intelectual opera bajo la Licencia Creative Commons (CC BY-SA 4.0).
