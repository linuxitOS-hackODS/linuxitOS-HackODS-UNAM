# 📄 Reporte de Auditoría Técnica: Cumplimiento de Rúbrica (md-only)

## 📌 Contexto
La rúbrica del HackODS estipula estrictamente (valor de 8 puntos):
> **md-only** — la prosa de `index.qmd` está en markdown/Quarto puro - No se utiliza HTML ni Java en el tablero.

Actualmente, el proyecto **no cumple** con este requerimiento. A continuación, se detalla el análisis de dónde estamos utilizando tecnologías prohibidas por la rúbrica y por qué fallamos en este punto.

---

## 🚨 Hallazgos Críticos (Violaciones de la Rúbrica)

### 1. Uso de JavaScript (Inyección de Scripts)
La rúbrica especifica "ni Java" (comúnmente refiriéndose a JavaScript en el contexto web front-end). 
* **Dónde fallamos:** Tenemos un script personalizado de JavaScript para animar los números y detectar el scroll.
* **Archivos implicados:**
  - `dashboard/animations.html`: Contiene 53 líneas de código puro en JavaScript (`<script>`) usando `IntersectionObserver` y `requestAnimationFrame`.
  - `dashboard/index.qmd` (Líneas 5-6): Se está inyectando este script directamente en el tablero a través del comando de YAML `include-after-body: animations.html`.

### 2. Uso de Bloques HTML Puros (````{=html}`)
La rúbrica exige que la prosa y estructura estén en "markdown/Quarto puro". 
* **Dónde fallamos:** Para lograr el diseño estético de las tarjetas premium, usamos bloques que escapan el Markdown y procesan HTML directo en `index.qmd`.
* **Ubicaciones exactas en `index.qmd`:**
  - **Líneas 39-68:** Bloque HTML para el "Subtítulo Ejecutivo" y las tres tarjetas KPI principales (Ej. `<div class="stat-card-v2...">`).
  - **Líneas 246-258:** Bloque HTML para las "Tarjetas de Contexto" laterales (Ej. `<div class="context-card card-blue">`).
  - **Líneas 435-455:** Bloque HTML para las tarjetas KPI de la segunda pestaña (Ej. `<div class="stat-cards-container...">`).

---

## 🛠️ Conclusiones y Plan de Remediación

Si los jueces evalúan el código fuente hoy, **perderemos automáticamente los 8 puntos**.

Para recuperar estos puntos sin sacrificar demasiado el diseño premium que hemos logrado, necesitaremos hacer una refactorización que traduzca el HTML y JS a componentes nativos de Quarto:

1. **Eliminar JS:** 
   - Quitar `animations.html` de `index.qmd` y eliminar el archivo. Perderemos la animación de "contador" de los números, pero aseguraremos los puntos.
2. **Refactorizar Tarjetas KPI:**
   - Reemplazar los `<div>` HTML por el componente nativo de Quarto llamado **Value Boxes** (`::: {.valuebox}`). Podemos adaptar `styles.css` para que las Value Boxes nativas se vean idénticas a nuestras tarjetas actuales.
3. **Refactorizar Tarjetas de Contexto y Subtítulos:**
   - Reemplazar los `<div>` por **Callouts** nativos de Quarto (`::: {.callout-note}`) o simplemente bloques Div nativos de Pandoc (`::: {.context-card}`). Esto permite usar la sintaxis de markdown puro y seguir aplicando el CSS personalizado.

**Estado actual:** Auditoría completada. Ningún archivo ha sido modificado aún. A la espera de tu luz verde para proceder con la refactorización a Markdown puro.
