import pandas as pd

def main():
    print("Cargando final_merged_data.csv...")
    df_main = pd.read_csv("datos/final_merged_data.csv")
    
    # Asegurar que CVEGEO sea string de 5 caracteres
    df_main['CVEGEO'] = df_main['CVEGEO'].astype(str).str.zfill(5)
    
    print("Cargando datos de CONAGUA...")
    df_conagua = pd.read_excel("datos/Población con acceso al agua en el año 2020.xlsx")
    
    # Crear CVEGEO en CONAGUA
    df_conagua['CVEGEO'] = df_conagua['Clave Entidad'].astype(str).str.zfill(2) + df_conagua['Clave Municipio'].astype(str).str.zfill(3)
    
    # Calcular carencia de agua
    df_conagua['carencia_agua_conagua_pct'] = 100.0 - df_conagua['Población Cobertura(%)']
    df_conagua['cobertura_agua_conagua_pct'] = df_conagua['Población Cobertura(%)']
    
    # Seleccionar solo las columnas necesarias (regla de oro: nada de demografía de CONAGUA)
    cols_to_keep = ['CVEGEO', 'Clave RHA', 'RHA', 'cobertura_agua_conagua_pct', 'carencia_agua_conagua_pct']
    df_conagua_subset = df_conagua[cols_to_keep]
    
    print("Realizando cruce (Left Join)...")
    df_merged = pd.merge(df_main, df_conagua_subset, on='CVEGEO', how='left')
    
    print(f"Total de filas antes del cruce: {len(df_main)}")
    print(f"Total de filas después del cruce: {len(df_merged)}")
    print("Muestra de nuevas columnas:")
    print(df_merged[['CVEGEO', 'Municipio', 'RHA', 'cobertura_agua_conagua_pct', 'carencia_agua_conagua_pct']].head(3))
    
    print("Guardando datos/final_merged_data.csv...")
    df_merged.to_csv("datos/final_merged_data.csv", index=False)
    print("¡Proceso completado exitosamente!")

if __name__ == "__main__":
    main()
