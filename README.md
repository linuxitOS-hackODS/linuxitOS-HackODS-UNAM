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
- **ODS Elegidos:** 
  - ODS 6 de "Agua limpia y saneamiento" interconectado de manera transveral con el ODS 1 de "Fin de la pobreza".

--- 

## 2. Descripción y Planteamiento del Problema
**Pregunta Central:**  
*¿Cómo el déficit de infraestructura hídrica profundiza sistemáticamente la pobreza en el México rural frente a los grandes centros urbanos?*

En México, el acceso al agua suele evaluarse con promedios nacionales que ocultan profundas desigualdades territoriales. Al analizar los datos a nivel municipal, se revela que muchas comunidades rurales permanecen rezagadas, fuera del alcance de la infraestructura hídrica.

Esta brecha no es solo técnica, sino estructural: la dispersión geográfica influye en cómo se asignan los recursos, dejando a ciertos territorios sistemáticamente excluidos. En consecuencia, la falta de agua no solo refleja la pobreza, sino que contribuye a perpetuarla.

Este proyecto explora estas desigualdades mediante el cruce de microdatos, con el objetivo de visibilizar patrones que permanecen ocultos en las estadísticas agregadas.

---

## 3. Fuentes de Datos Oficiales

> **[Consultar Metadatos y Diccionarios de Datos aquí](datos/README.md)**

> *Nota: Toda la información técnica de los datasets (diccionario de variables, fechas de extracción, enlaces primarios y licencias de uso) se encuentra documentada a detalle en el README de la carpeta de datos.*

---

## 4. Guía de Reproducibilidad Técnica

**Entorno de Ejecución:**
- **Python:** `>= 3.10`
- **Gestor de Dependencias:** [uv](https://docs.astral.sh/uv/getting-started/installation/) (Astral)
- **Quarto CLI:** `>= 1.4`
- **Control de Versiones:** `Git`

### Evidencia Técnica y Narrativa
Este repositorio implementa una estrategia de **"Documentación Multinivel"** para garantizar la transparencia metodológica:

*   **Narrativa Estratégica ([`001_Pipeline_ETL_ODS.ipynb`](notebooks/001_Pipeline_ETL_ODS.ipynb)):** Es el documento principal de revisión. Presenta el flujo lógico, la interconexión entre ODS y los resultados analíticos finales de forma orquestada.
*   **Auditoría Técnica Detallada ([`002_Pipeline_Datos_Detallado.ipynb`](notebooks/002_Pipeline_Datos_Detallado.ipynb)):** Expone el código fuente íntegro de los 7 módulos del pipeline, permitiendo una inspección profunda de los algoritmos de limpieza, normalización y optimización geoespacial.

---

## 5. Guía de Reproducción y Auditoría

Para replicar el entorno de desarrollo y verificar la integridad del pipeline, se utiliza el estándar **`uv`**. Este gestor garantiza que las dependencias instaladas en su sistema coincidan exactamente con las utilizadas durante la investigación.

### Instalación de `uv` (si es necesario)
- **Windows (PowerShell):** `powershell -c "irm https://astral.sh/uv/install.ps1 | iex"`
- **Linux/macOS (Terminal):** `curl -LsSf https://astral.sh/uv/install.sh | sh`

### Protocolo de Ejecución (CLI)
Ejecutar los siguientes comandos desde la raíz del proyecto para reconstruir la evidencia técnica:

```bash
# 1. Clonar el repositorio
git clone https://github.com/linuxitOS-hackODS/linuxitOS-HackODS-UNAM.git
cd linuxitOS-HackODS-UNAM

# 2. Sincronización determinista del entorno virtual
# uv lee el archivo pyproject.toml y levanta el entorno de manera aislada.
uv sync

# 3. Compilar Pipeline de Datos Automatizado (Orquestador ETL)
uv run main.py

# 4. Procesar e instanciar el Dashboard Analítico (Preview)
uv run quarto preview dashboard/index.qmd
```

---

## 6. Arquitectura del Proyecto
- `datos/`: Repositorio inmutable para los datasets en crudo (*raw*) y salida del dataset unificado (`final_merged_data.csv`).
- `scripts/`: Módulos de Python responsables del flujo ETL (Extract, Transform, Load) bajo estándares de código limpio.
- `dashboard/`: Código fuente del tablero analítico (`index.qmd`), configuraciones topológicas (`_quarto.yml`) y UI/CSS personalizado (`styles.css`).
- `ai-log.md`: Declaratoria de trazabilidad, documentando las interacciones tecnológicas y éticas de apoyo de IA durante el Hackathon.
- `LICENSE`: Este trabajo intelectual opera bajo la Licencia Creative Commons (CC BY-SA 4.0).
