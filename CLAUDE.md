# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

HackODS UNAM 2026 — interactive data dashboard analyzing the structural link between water infrastructure deficits (ODS 6) and extreme poverty (ODS 1) across Mexico's 2,469 municipalities. Built with Python + Quarto.

## Commands

```bash
# Install dependencies (uv manages the .venv automatically)
uv sync

# Run the full ETL pipeline → produces datos/final_merged_data.csv
uv run main.py

# Dev server (hot-reload preview)
quarto preview dashboard/index.qmd

# Production build → outputs to docs/ (GitHub Pages)
quarto render dashboard/index.qmd

# Run a single ETL script directly
uv run scripts/merge_conagua.py
```

## Architecture

### Data Flow

```
Raw sources (datos/)
    │
    ▼
main.py (orchestrator)
    ├── scripts/siods_extractor.py     → siods_agua_saneamiento_nacional.csv
    ├── scripts/analyze_iter.py        → ruralidad classification from INEGI census
    ├── scripts/clean_coneval.py       → coneval_clean_2020.csv
    ├── scripts/merge_inegi_coneval.py → merges census + poverty data
    ├── scripts/merge_shcp.py          → adds municipal water revenue (SHCP)
    ├── scripts/merge_conagua.py       → adds CONAGUA water coverage
    └── scripts/simplify_geojson.py   → produces *_lite.json GeoJSON files
    │
    ▼
datos/final_merged_data.csv  (master dataset, all visualizations read from here)
    │
    ▼
dashboard/index.qmd  →  quarto render  →  docs/index.html (GitHub Pages)
```

### Key Files

- `dashboard/index.qmd` — single-file Quarto dashboard; all charts are Python code blocks with Plotly
- `dashboard/_quarto.yml` — project type `website`, output-dir `../docs`, theme `lux + styles.css`
- `dashboard/styles.css` — custom CSS layered on top of the `lux` Bootswatch theme
- `datos/final_merged_data.csv` — master merged dataset consumed by the dashboard
- `datos/Estado_lite.json` — simplified GeoJSON for state-level choropleth (`featureidkey: properties.clvedo`)
- `datos/Estado.csv` — state catalog with `clvedo` (state code) and `estado` columns
- `datos_ongs.yml` + `ongs.ejs` — ONG directory rendered as a Quarto listing in the "Acción Positiva" tab

### Dashboard Structure (tabs in index.qmd)

1. **La Ilusión Nacional** — histogram + scatter plot exposing the rural/urban gap
2. **La Realidad Demográfica** — horizontal bar chart of top 15 municipalities by water deficit
3. **El mapa de la invisibilidad** — state choropleth + interactive itables table
4. **Acción Positiva** — ONG presence choropleth + YAML-driven directory
5. **Explorador de Datos** — full interactive table of all 2,469 municipalities

### Ruralidad Classification

Defined in `scripts/analyze_iter.py` from the INEGI ITER 2020 census: a municipality is **Rural** if more than 50% of its localities have fewer than 2,500 inhabitants. The derived column `clasificacion_rural` (values: `'Rural'` / `'Urbano'`) flows through all subsequent merges into `final_merged_data.csv`.

## Critical Constraints

**Do not set `pio.renderers` in the dashboard.** Forcing a renderer breaks Quarto's internal ResizeObserver and causes overlapping legends. Let Quarto manage widget rendering natively.

**Suppress intermediate Plotly calls** with `_ = fig.update_layout(...)` to prevent auto-display of intermediate objects in Quarto cells.

**Relative paths in dashboard:** `index.qmd` references data as `../datos/` (one level up from `dashboard/`). Quarto renders from inside `dashboard/`, so this path resolves correctly during both `preview` and `render`.

**GeoJSON key for choropleth:** state-level maps use `featureidkey='properties.clvedo'` matched against the `clvedo` column of `Estado.csv`.

**Python env:** managed by `uv` with `pyproject.toml`. Always use `uv run` or activate `.venv` before running scripts directly.

**md-only:** prose in `index.qmd` is pure Markdown/Quarto. No raw HTML (`<script>` tags, inline event handlers). OJS (`{ojs}` cells) is allowed — it's Quarto-native, used for reactive interactivity (e.g., search inputs). Python data is passed to OJS via `ojs_define()`.
