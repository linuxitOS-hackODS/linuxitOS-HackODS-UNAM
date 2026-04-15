import pandas as pd
import numpy as np
import os

# Ajuste de directorio de trabajo para soportar ejecución en Terminal y Notebooks
if not os.path.exists('scripts') and os.path.exists(os.path.join('..', 'scripts')):
    os.chdir('..')

file_path = "datos/conjunto_de_datos_iter_00CSV20.csv.gz"

print("[INFO] Cargando microdatos censales (ITER 2020)...")
df = pd.read_csv(file_path, usecols=['ENTIDAD', 'MUN', 'LOC', 'NOM_LOC', 'POBTOT'], dtype=str)

# Limpieza básica
# Filtramos para quitar el total nacional y estatales (MUN == '000')
df = df[df['MUN'] != '000']
# Filtramos para quitar los totales municipales (LOC == '0000') y quedarnos solo con localidades
df_loc = df[df['LOC'] != '0000'].copy()

# Convertir población a numérico ('*' se vuelve NaN, luego 0)
df_loc['POBTOT'] = pd.to_numeric(df_loc['POBTOT'], errors='coerce').fillna(0)

# Criterio INEGI: Localidad rural = menos de 2500 habitantes
df_loc['es_rural'] = df_loc['POBTOT'] < 2500
df_loc['pob_rural'] = np.where(df_loc['es_rural'], df_loc['POBTOT'], 0)

# Agrupación a nivel municipal
df_loc['CVEGEO'] = df_loc['ENTIDAD'] + df_loc['MUN']
agrupado = df_loc.groupby('CVEGEO').agg(
    poblacion_total=('POBTOT', 'sum'),
    poblacion_rural=('pob_rural', 'sum'),
    total_localidades=('LOC', 'count'),
    localidades_rurales=('es_rural', 'sum')
).reset_index()

# Calcular porcentaje rural del municipio
agrupado['pct_rural'] = (agrupado['poblacion_rural'] / agrupado['poblacion_total']) * 100
agrupado['pct_rural'] = agrupado['pct_rural'].fillna(0)

# Clasificar municipio (Rural si > 50% de su población vive en localidades rurales)
agrupado['clasificacion'] = np.where(agrupado['pct_rural'] > 50, 'Rural', 'Urbano')

print("\n[INFO] --- Resumen Poblacional (Censo 2020) ---")
print(f"[INFO] Municipios totales evaluados: {len(agrupado)}")
print(f"[INFO] Entidades de vocación rural predominante: {len(agrupado[agrupado['clasificacion'] == 'Rural'])}")
print(f"[INFO] Entidades de vocación urbana predominante: {len(agrupado[agrupado['clasificacion'] == 'Urbano'])}")
print(f"[INFO] Universo poblacional censado: {agrupado['poblacion_total'].sum():,.0f}")
print(f"[INFO] Población clasificada como rural: {agrupado['poblacion_rural'].sum():,.0f}")
print(f"[INFO] Tasa global de ruralidad: {(agrupado['poblacion_rural'].sum() / agrupado['poblacion_total'].sum()) * 100:.2f}%")

