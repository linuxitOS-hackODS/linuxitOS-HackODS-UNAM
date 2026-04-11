import pandas as pd
import numpy as np
import os

def procesar_inegi():
    print("1. Procesando Censo INEGI 2020 (ITER) para calcular ruralidad municipal...")
    file_path = "../datos/conjunto_de_datos_iter_00CSV20.csv.gz"
    
    # Leemos solo las columnas necesarias para ahorrar memoria
    df = pd.read_csv(file_path, usecols=['ENTIDAD', 'NOM_ENT', 'MUN', 'LOC', 'POBTOT'], dtype=str)
    
    # Filtros: quitar totales estatales (MUN='000') y totales municipales (LOC='0000')
    df = df[df['MUN'] != '000']
    df_loc = df[df['LOC'] != '0000'].copy()
    
    # Convertir población a numérico (reemplazando '*' por NaN y luego 0)
    df_loc['POBTOT'] = pd.to_numeric(df_loc['POBTOT'], errors='coerce').fillna(0)
    
    # Regla de ruralidad INEGI: Localidad con menos de 2500 habitantes
    df_loc['es_rural'] = df_loc['POBTOT'] < 2500
    df_loc['pob_rural'] = np.where(df_loc['es_rural'], df_loc['POBTOT'], 0)
    
    # Agrupar por clave municipal (CVEGEO = ENTIDAD + MUN)
    df_loc['CVEGEO'] = df_loc['ENTIDAD'] + df_loc['MUN']
    
    agrupado = df_loc.groupby('CVEGEO').agg(
        Estado=('NOM_ENT', 'first'),
        poblacion_total=('POBTOT', 'sum'),
        poblacion_rural=('pob_rural', 'sum')
    ).reset_index()
    
    # Calcular porcentaje rural del municipio
    agrupado['pct_rural'] = (agrupado['poblacion_rural'] / agrupado['poblacion_total']) * 100
    agrupado['pct_rural'] = agrupado['pct_rural'].fillna(0)
    
    # Clasificación principal para el storytelling
    agrupado['clasificacion_rural'] = np.where(agrupado['pct_rural'] > 50, 'Rural', 'Urbano')
    
    return agrupado[['CVEGEO', 'Estado', 'poblacion_total', 'pct_rural', 'clasificacion_rural']]

def merge_datos():
    inegi_df = procesar_inegi()
    
    coneval_path = "../datos/coneval_clean_2020.csv"
    print(f"2. Cargando datos de pobreza municipal CONEVAL: {coneval_path}")
    coneval_df = pd.read_csv(coneval_path, dtype={'CVEGEO': str})
    
    # Asegurar formato de clave a 5 dígitos
    inegi_df['CVEGEO'] = inegi_df['CVEGEO'].str.zfill(5)
    coneval_df['CVEGEO'] = coneval_df['CVEGEO'].str.zfill(5)
    
    print("3. Ejecutando el Cruce de Datos (Merge)...")
    # Inner merge para conservar solo los municipios que existen en ambas fuentes
    merged_df = pd.merge(coneval_df, inegi_df, on='CVEGEO', how='inner')
    
    out_path = "../datos/final_merged_data.csv"
    merged_df.to_csv(out_path, index=False)
    
    print(f"\n¡CRUCE EXITOSO! Dataset maestro generado en: {out_path}")
    print(f"Total de municipios cruzados: {len(merged_df)}")
    
    print("\n--- Vista previa de los datos listos para el Dashboard ---")
    print(merged_df.head().to_string())
    
    print("\n--- Comprobación de Hipótesis (Promedios por Clasificación) ---")
    resumen = merged_df.groupby('clasificacion_rural').agg(
        Carencia_Agua_Promedio=('Carencia_servicios_pct', 'mean'),
        Pobreza_Extrema_Promedio=('Pobreza_extrema_pct', 'mean'),
        Municipios=('CVEGEO', 'count')
    ).round(2)
    print(resumen.to_string())

if __name__ == "__main__":
    # Asegurar rutas relativas correctas
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    merge_datos()
