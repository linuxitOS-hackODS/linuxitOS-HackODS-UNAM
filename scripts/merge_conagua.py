import pandas as pd

def main():
    import os
    if not os.path.exists('scripts') and os.path.exists(os.path.join('..', 'scripts')):
        os.chdir('..')

    print("[INFO] Leyendo base: final_merged_data.csv")
    df_main = pd.read_csv("datos/final_merged_data.csv")
    
    # Asegurar que CVEGEO sea string de 5 caracteres
    df_main['CVEGEO'] = df_main['CVEGEO'].astype(str).str.zfill(5)
    
    print("[INFO] Leyendo base: CONAGUA (Población con acceso al agua 2020)")
    df_conagua = pd.read_excel("datos/Población con acceso al agua en el año 2020.xlsx")
    
    # Crear CVEGEO en CONAGUA
    df_conagua['CVEGEO'] = df_conagua['Clave Entidad'].astype(str).str.zfill(2) + df_conagua['Clave Municipio'].astype(str).str.zfill(3)
    
    # Calcular carencia de agua
    df_conagua['carencia_agua_conagua_pct'] = 100.0 - df_conagua['Población Cobertura(%)']
    df_conagua['cobertura_agua_conagua_pct'] = df_conagua['Población Cobertura(%)']
    
    # Seleccionar solo las columnas necesarias (regla de oro: nada de demografía de CONAGUA)
    cols_to_keep = ['CVEGEO', 'Clave RHA', 'RHA', 'cobertura_agua_conagua_pct', 'carencia_agua_conagua_pct']
    df_conagua_subset = df_conagua[cols_to_keep]
    
    print("[INFO] Concatenando observaciones (Left Join por CVEGEO)...")
    df_merged = pd.merge(df_main, df_conagua_subset, on='CVEGEO', how='left')
    
    print(f"[INFO] Observaciones iniciales: {len(df_main)}")
    print(f"[INFO] Observaciones resultantes: {len(df_merged)}")
    print("[INFO] Verificación taxonómica (head):")
    print(df_merged[['CVEGEO', 'Municipio', 'RHA', 'cobertura_agua_conagua_pct', 'carencia_agua_conagua_pct']].head(3))
    
    print("[INFO] Volcando estructura consolidada en disco (CSV)...")
    df_merged.to_csv("datos/final_merged_data.csv", index=False)
    print("[ÉXITO] Base CONAGUA unificada con dataset maestro.")

if __name__ == "__main__":
    main()
