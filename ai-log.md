# AI Log - Equipo linuxitOS

## Herramientas utilizadas
- OpenCode (Gemini, Claude)
- GitHub Copilot (VS Code)

## Filosofía de uso
Decidimos usar IA exclusivamente para tareas mecánicas y de estructuración inicial. Las decisiones analíticas, la selección de variables y la narrativa son producto del trabajo intelectual del equipo. Nuestro criterio: si la tarea requiere conocimiento del contexto social, económico e hídrico de México, la hacemos nosotros.

## Registro de uso

### 2026-04-02 | OpenCode / Claude / Gemini | Definición del Contexto Estricto y Restricciones del Agente AI
- **Tarea**: Establecer las restricciones técnicas, éticas y de evaluación del hackathon como contexto de sistema para el agente IA desde el inicio del proyecto.
- **Prompt**: "Actúa como mi asistente de programación y análisis de datos experto. Estoy participando en el HackODS UNAM 2026, un hackatón enfocado en crear un tablero de datos (dashboard) sobre los Objetivos de Desarrollo Sostenible (ODS 1 y ODS 6). Para ayudarme correctamente, debes acatar estrictamente la siguiente lista de tecnologías permitidas, reglas de evaluación y restricciones de uso de IA del evento. Si te pido algo que viole estas reglas, debes advertírmelo.

  1. TECNOLOGÍAS PERMITIDAS Y REQUERIDAS: Lenguaje base: Python. Manejo y transformación de datos: Pandas. Visualización de datos: Plotly (específicamente gráficos interactivos y mapas como px.choropleth). Construcción del Tablero (Obligatorio): archivos de Quarto (.qmd) o Jupyter Notebooks (.ipynb). Diseño Web y UI/UX: HTML, CSS y frameworks como Bootstrap o UIkit. Despliegue: GitHub / GitHub Pages.

  2. REGLAS DE USO DE IA: SÍ PUEDES generar código base (boilerplate) para gráficas en Plotly, crear scripts de limpieza de datos en Pandas, sugerir estructuras de layout para Quarto y depurar errores de código. SÍ PUEDES actuar como editor o revisor crítico de textos. NO PUEDES (PROHIBIDO): Escribir la narrativa del tablero. Los textos que contextualizan los datos, conectan las variables y formulan el argumento central deben ser redactados por el nosotros. No generes conclusiones automáticas sobre los datos sociales. CALIDAD DEL CÓDIGO: Todo el código debe estar documentado con comentarios claros y mantener un estilo uniforme.

  3. REGLAS ESTRICTAS DE ESTRUCTURA (RIESGO DE DESCALIFICACIÓN): Debe contener exactamente estas tres carpetas base: datos/, scripts/ y dashboard/. El tablero (.qmd o .ipynb) debe ir obligatoriamente dentro de dashboard/. Debe existir un archivo ai-log.md en la raíz. Debe existir un README.md con metadatos de datasets y pregunta central. Debe incluir un archivo LICENSE declarando CC BY-SA.

  4. DATOS PERMITIDOS: Solo podemos utilizar fuentes de datos públicas, oficiales y verificables (SIODS, INEGI, CONEVAL, Banco Mundial, UNAM, etc.). No puedes inventar, simular o 'alucinar' datos estadísticos.

  Entendido este contexto, ¿estás listo para comenzar?"
- **Resultado**: Asimilación completa del entorno técnico y delimitación ética del modelo. El agente confirmó los límites operativos y quedó configurado para el contexto del hackathon.
- **Decisión**: El equipo estructuró exhaustivamente este mandato inicial para que cualquier interacción posterior estuviera alineada con la rúbrica desde el primer momento. Este contexto fue revisado y aprobado por el equipo antes de usarse.

---

### 2026-04-04 | OpenCode / Claude / Gemini| Refactorización Arquitectónica y Visualización (Actos 1 y 2)
- **Tarea**: Modularizar los scripts de ETL y agregar visualizaciones de Plotly para los Actos 1 y 2 del dashboard.
- **Prompt**: "Necesito que trabajemos en la modularidad y escalabilidad de los .py, sé profesional y haz uso de buenas prácticas. Respecto al acto 1 de la "Ilusión Nacional", ocupo que coloque un gráfico que compare ... utiliza una gráfica de barras con Plotly. Respecto al acto 2, ayúdame con el código de una tabla que filtre ..., apégate al uso de las tecnologías permitidas así como las restricciones dadas; no modifiques (borres o agregues) ningún dato oficial dado."
- **Resultado**: Generó el código base estructurado de scripts separados e inyectó sintaxis de Plotly interactivo para el Acto 1 y la codificación para la tabla filtrada del Acto 2.
- **Decisión**: El equipo instruyó exactamente qué métricas comparar e impuso la restricción de no modificar ningún dato oficial. La selección de variables a visualizar (carencia de agua vs. pobreza extrema) y el argumento narrativo detrás de cada gráfica fueron íntegramente definidos por el equipo.

---

### 2026-04-05 | OpenCode / Claude / Gemini| Mejora UI/UX Acto 2 (Interactividad ITables) y Enriquecimiento de Datos
- **Tarea**: Enriquecer la tabla de anomalías fiscales con el nombre del Estado y reemplazarla con una tabla interactiva usando ITables.
- **Prompt**: "Para mejorar el acto 2, necesito enriquecer la tabla de anomalías para que sea mucho más profesional e interactiva. Modifica el script merge_inegi_coneval.py para extraer y conservar el nombre del Estado (NOM_ENT) desde el diccionario oficial... Segundo, en el dashboard utiliza itables para cambiar la tabla... Por último, borra el script audit_datasets.py para mantener el repositorio limpio."
- **Resultado**: Modificó el script de extracción para incluir la clave geopolítica estatal, actualizó dependencias en requirements.txt e implementó ITables en el entorno de visualización de Quarto.
- **Decisión**: El equipo identificó la necesidad de dar contexto geográfico inmediato a las anomalías de recaudación (razón analítica, no técnica). La decisión de usar ITables como librería de interactividad nativa fue del equipo, basándose en las tecnologías permitidas por la rúbrica.

---

### 2026-04-05 | OpenCode / Claude / Gemini | Rediseño Geoespacial del Acto 3 y Optimización Topológica
- **Tarea**: Integrar un mapa choropleth interactivo de las 757 cuencas hidrológicas CONAGUA y comprimir el GeoJSON oficial de 18MB a ~1MB para web.
- **Prompt**: "Sé un profesional en UI/UX y rediseña la experiencia visual del acto 3. Utilizando choropleth ayúdame a integrar un mapa que integre la comparativa de disponibilidad de agua de las 757 cuencas (de datos oficiales de CONAGUA), para ello te integré un GeoJSON, así como un diccionario de datos en un .csv (que no deben ser modificados). El GeoJSON tiene un peso de 18MB por lo que necesito que me apoyes a comprimirlo con un script que utilice GeoPandas para su compresión. Utiliza solamente las tecnologías permitidas y respeta restricciones de rúbricas."
- **Resultado**: Construyó el código del choropleth en Quarto y desarrolló el script `simplify_geojson.py` en Python usando GeoPandas para reducir el peso topológico del archivo sin pérdida de fidelidad visual.
- **Decisión**: El equipo tomó la decisión editorial de hacer el Acto 3 centralizado en el mapa como elemento narrativo principal (acceso vs. escasez hídrica por cuenca). La validación de que la simplificación topológica no distorsionara las fronteras de las cuencas fue una verificación manual del equipo.

---

### 2026-04-06 | OpenCode / Claude / Gemini | Reestructuración Narrativa y UI Final (Acto 4: Acción Positiva)
- **Tarea**: Integrar nuevo Acto 4 ("Contrastes de Recaudación") como "Acción Positiva", integrando un nuevo mapa estatal de ONGs y los logos institucionales de forma orgánica.
- **Prompt**: "Necesito que reestructures completamente el acto 4 que se llama 'contrastes de recaudación', vamos a basarnos en la estética y filosofía de diseño de los actos previos; analízalos. Necesito que con base en las tecnologías que podemos ocupar mejoremos el diseño y reescribamos desde cero este apartado. Encontrarás unas imágenes contenidas en la ruta /dashboard/img, estas imágenes corresponden a los logos de ciertas instituciones, necesito que analicemos la forma más óptima de incluir estas imágenes de la forma más orgánica posible. Toma de referencia el acto 3 'el mapa de la invisibilidad', necesito que la información se despliegue del lado izquierdo y del lado derecho generaremos un mapa interactivo utilizando choropleth de la república mexicana. Para ello te incluyo Estados.csv y Estados.json. El objetivo es hacer que por cada estado se ilumine de color azul dependiendo de la cantidad de organizaciones que tengan impacto en él (0 blanco, 1 a 2 azul claro y 3 a 4 azul oscuro). No programes nada aún, vamos a planificar para ejecutarlo de la forma más profesional posible y siguiendo la rúbrica dada por el equipo de organizadores."
- **Resultado**: Desarrolló la arquitectura del layout en Quarto, procesó el join entre `Estado.csv` y `proyectos_agua.csv`, y generó la lógica del mapa choropleth categórico por intensidad de presencia de ONGs.
- **Decisión**: El equipo tomó la decisión estratégica de eliminar la sección de anomalías de la SHCP para cerrar el dashboard con un acto enfocado en la solución, no en el problema. La narrativa literaria completa ("Pero la estadística no es destino. Hay quienes están cambiando el mapa...") y la selección de las 4 organizaciones documentadas fue íntegramente redactada y curada por el equipo.

---

### 2026-04-13 | OpenCode / Claude / Gemini | Integración del Pipeline ETL a Jupyter Notebook
- **Tarea**: Migrar secuencialmente los 7 scripts Python aislados hacia un único `.ipynb` consolidado que facilite la evaluación de los jurados del HackODS, asegurando coherencia narrativa.
- **Prompt**: "Necesito que me ayudes a escribir un script en python que cree la base de un .ipnyb (libreta de Jupiter). Necesito que facilitemos la colaboración y reproducibilidad del proyecto creando un Notebook ordenado, profesional y robusto. Vamos a planear la integración paso a paso para hacer una correcta integración de lo solicitado."
- **Resultado**: Se desarrolló el script automático `scripts/build_notebook.py` que lee los `.py` originales y los ensambla estructuralmente dentro de un formato `.ipynb` nativo, preservando la organización oficial dentro del directorio `notebooks/`.
- **Decisión**: El equipo tomó la decisión estratégica de alinear la arquitectura del proyecto con los repositorios de ejemplo de los organizadores (`NombreEquipo_ejemplo`), facilitando la experiencia del jurado al aglutinar todas las reglas de negocio y limpieza de datos en un solo cuaderno reproducible.

---

### NO usamos IA para hacer lo siguiente:
- Formular la pregunta central y definir el rumbo de nuestro storytelling.
- Definir la narrativa del tablero y las conclusiones cruzando el ODS 1 y el ODS 6.
- Definir la estrategia analítica frente a la pobreza multidimensional.
- Definir la estrategia de visualización y diseño del dashboard.
- Seleccionar las variables clave de cada fuente oficial (INEGI, CONEVAL, CONAGUA, SHCP).
- Redactar los textos descriptivos de las ONGs.