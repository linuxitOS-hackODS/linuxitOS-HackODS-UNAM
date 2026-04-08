# Metadatos del Proyecto linuxitOS

En esta carpeta (`datos/`) guardamos todos los datasets utilizados en crudo y procesados. Cada archivo tiene su propia metadata descrita a continuación, cumpliendo con los lineamientos de la rúbrica del Módulo A.

---

### 1. Contexto Nacional y Estatal (Agenda 2030)
- **Nombre de archivo:** `siods_agua_saneamiento_nacional.csv`
- **Descripción de las variables (Data Dictionary):** 
  - `Indicador`: Nombre de la meta oficial (6.1.1.a Nacional o 6.1.1.c Estatal).
  - `Clave_Entidad`: Clave geoestadística de la zona (00 para Nacional, 01-32 para Estatal).
  - `Entidad`: Nombre geográfico.
  - `Año`: Año del registro (2020).
  - `Valor`: Porcentaje de cobertura del servicio.
- **Fuente:** Sistema de Información de los Objetivos de Desarrollo Sostenible (SIODS). API Oficial [Indicador 54 (Nacional)](https://agenda2030.mx/ODSind.html?ind=ODS006000050010&cveind=54&cveCob=99&lang=es#/Indicator) y [Indicador 618 (Estatal)](https://agenda2030.mx/ODSind.html?ind=ODS006000050030&cveind=618&cveCob=99&lang=es#/Indicator).
- **Fecha de descarga:** 02 de abril de 2026.
- **Licencia:** [Licencia de Código Abierto del Gobierno de México](https://www.agenda2030.mx/docs/doctos/system/Licencia_codigo_abierto_ES.pdf).

### 2. Geografía de la Desigualdad (Demografía INEGI)
- **Nombre de archivo:** Archivos dentro de la carpeta `iter_00_cpv2020_csv/`
- **Descripción de las variables (Data Dictionary):** 
  - `ENTIDAD`: Clave del Estado.
  - `MUN`: Clave del Municipio.
  - `LOC`: Clave de la Localidad.
  - `POBTOT`: Población total residente en esa localidad. *(Variable clave usada para determinar ruralidad: localidades < 2500 habitantes)*.
- **Fuente:** INEGI. Censo de Población y Vivienda 2020. Principales resultados por localidad (ITER). [Enlace de descarga oficial](https://www.inegi.org.mx/app/descarga/ficha.html?tit=326108&ag=0&f=csv)
- **Fecha de descarga:** 02 de abril de 2026.
- **Licencia:** [Términos de Libre Uso de la Información del INEGI](https://www.inegi.org.mx/contenidos/inegi/doc/terminos_sitio.pdf).

### 3. Dimensión de la Pobreza y Carencia de Infraestructura (CONEVAL)
- **Nombre de archivo:** `Concentrado_indicadores_de_pobreza_2020.xlsx` (y su versión limpia `coneval_clean_2020.csv`)
- **Descripción de las variables (Data Dictionary):** 
  - `CVEGEO`: Clave geográfica municipal (5 dígitos).
  - `Municipio`: Nombre del municipio.
  - `Pobreza_pct`: Porcentaje de la población en pobreza multidimensional.
  - `Pobreza_extrema_pct`: Porcentaje de la población en pobreza extrema.
  - `Carencia_servicios_pct`: Porcentaje de la población con carencia por acceso a los servicios básicos en la vivienda (Indicador oficial que penaliza la falta de agua y drenaje).
- **Fuente:** CONEVAL. Medición de la Pobreza a Nivel Municipal 2020. Anexo Estadístico. [Descarga ZIP original](https://www.coneval.org.mx/Medicion/Documents/Pobreza_municipal/2020/Concentrado_indicadores_de_pobreza_2020.zip)
- **Fecha de descarga:** 02 de abril de 2026 (Archivo original data de Dic 2021).
- **Licencia:** Libre Uso (Datos Abiertos del Gobierno de México / CONEVAL).

### 4. Finanzas Públicas Municipales (SHCP)
- **Nombre de archivo:** `derecho_agua_municipal.csv`
- **Descripción de las variables (Data Dictionary):**
  - `monto_agua`: Recaudación anual (2020) por derechos de suministro de agua potable.
  - `tomas_pagadas`: Número de tomas de agua registradas con pago.
  - `monto_recaudado_percapita`: Cálculo derivado de la recaudación por habitante municipal.
- **Fuente:** Secretaría de Hacienda y Crédito Público (SHCP) - Estadísticas de Finanzas Públicas Municipales. [Enlace de descarga oficial](https://www.datos.gob.mx/dataset/derechos_agua_municipal).
- **Fecha de descarga:** 02 de abril de 2026.
- **Licencia:** Creative Commons Attribution 4.0.

### 5. Cobertura Específica de Agua y Cuencas (CONAGUA)
- **Nombre de archivo:** `Población con acceso al agua en el año 2020.xlsx`
- **Descripción de las variables (Data Dictionary):** 
  - `CVEGEO`: Clave geográfica municipal construida a partir de Entidad y Municipio.
  - `RHA`: Región Hidrológico-Administrativa (Agrupación por cuencas naturales).
  - `Población Cobertura(%)`: Porcentaje de cobertura específica de agua entubada en el municipio.
  - *Nota técnica:* Se generó la variable derivada `carencia_agua_conagua_pct` (`100 - Cobertura`) para medir el déficit directo (ODS 6). No se utilizaron las métricas demográficas de este archivo para evitar conflictos con el Censo INEGI 2020.
- **Fuente:** Comisión Nacional del Agua (CONAGUA) - Sistema Nacional de Información del Agua (SINA). [Consulta interactiva de coberturas](https://sinav30.conagua.gob.mx:8080/Estadistico/#/coberturas).
- **Fecha de descarga:** 03 de abril de 2026.
- **Licencia:** [Datos Abiertos de México (Libre Uso)](https://app.conagua.gob.mx/datosabiertoscna/index.html#:~:text=Los%20datos%20abiertos%20son%20datos%20que%20pueden,de%20la%20misma%20manera%20en%20que%20aparecen).

### 6. Geometría y Disponibilidad Hídrica de Cuencas (SINA - CONAGUA)
- **Nombre de archivo:** `Disponibilidad_Cuencas_2020.json` (Crudo de 18MB), `Disponibilidad_Cuencas_2020_lite.json` (Optimizado) y `Disponibilidad_Cuencas_2020.csv` (Diccionario tabular)
- **Descripción de las variables (Data Dictionary):** 
  - `clvcuenca`: Clave alfanumérica única de identificación de la Cuenca Hidrológica (Ej. "0101").
  - `cuenca`: Nombre geográfico y oficial de la cuenca (Ej. "Tijuana").
  - `clvrha`: Clave romana de la Región Hidrológico-Administrativa a la que pertenece (Ej. "I").
  - `clvrh`: Clave interna hidro-geográfica complementaria.
  - `clasificacion`: Estado dictaminado oficialmente para la cuenca ("Con disponibilidad" o "Sin disponibilidad").
  - `d`: Disponibilidad volumétrica.
  - `geometry`: Fronteras espaciales topológicas (GeoJSON Polygons / Multipolygons).
- **Fuente:** Sistema Nacional de Información del Agua (SINA) - CONAGUA. Módulo Temático de Cuencas Hidrológicas. [Consulta e Interfaz del Mapa](https://sinav30.conagua.gob.mx:8080/SINA/?opcion=cuencas).
- **Fecha de descarga:** 05 de abril de 2026.
- **Licencia:** [Datos Abiertos de México (Libre Uso)](https://app.conagua.gob.mx/datosabiertoscna/index.html#:~:text=Los%20datos%20abiertos%20son%20datos%20que%20pueden,de%20la%20misma%20manera%20en%20que%20aparecen).

---

### 7. Dataset Maestro (Elaboración Propia - Reproducibilidad)
- **Nombre de archivo:** `final_merged_data.csv`
- **Descripción de las variables (Data Dictionary):** Unificación consolidada de los microdatos de INEGI, CONEVAL, SHCP y CONAGUA. Las variables principales incluyen:
  - `CVEGEO`, `Municipio`, `poblacion_total`, `pct_rural`, `clasificacion_rural` (INEGI / Cálculo propio de ruralidad).
  - `Pobreza_pct`, `Pobreza_extrema_pct`, `Carencia_servicios_pct` (CONEVAL).
  - `monto_agua`, `tomas_pagadas`, `monto_recaudado_percapita` (SHCP).
  - `RHA`, `cobertura_agua_conagua_pct`, `carencia_agua_conagua_pct` (CONAGUA).
- **Fuente:** Elaboración propia (Equipo linuxitOS).
- **Reproducibilidad:** Este archivo asegura el rigor metodológico del Módulo A. Se genera de manera automatizada y secuencial ejecutando los scripts de limpieza y cruce ubicados en la carpeta `scripts/` (tales como `scripts/merge_shcp.py` y `scripts/merge_conagua.py`). Además, la optimización topológica del JSON se garantiza mediante `scripts/simplify_geojson.py`. Esto garantiza la trazabilidad total desde las fuentes primarias oficiales hasta el cruce final sin manipulación manual.
- **Fecha de última actualización:** 05 de abril de 2026.
- **Licencia:** CC BY-SA 4.0 (Licencia general de este repositorio).
