import pandas as pd

def process_coneval():
    file_path = "datos/Concentrado_indicadores_de_pobreza_2020.xlsx"
    print(f"Leyendo archivo CONEVAL: {file_path}")
    
    df = pd.read_excel(file_path, sheet_name="Concentrado municipal", header=None, skiprows=8)
    
    # 3: CVEGEO
    # 4: Municipio
    # 10: Pobreza 2020 (%)
    # 19: Pobreza extrema 2020 (%) -> NUEVA COLUMNA AGREGADA PARA MAYOR IMPACTO
    # 94: Carencia servicios basicos 2020 (%)
    df_clean = df[[3, 4, 10, 19, 94]].copy()
    df_clean.columns = ["CVEGEO", "Municipio", "Pobreza_pct", "Pobreza_extrema_pct", "Carencia_servicios_pct"]
    
    df_clean.dropna(subset=["CVEGEO"], inplace=True)
    df_clean["CVEGEO"] = df_clean["CVEGEO"].astype(str).str.replace(".0", "", regex=False).str.zfill(5)
    df_clean = df_clean[df_clean["CVEGEO"].str.len() == 5]
    
    df_clean["Pobreza_pct"] = pd.to_numeric(df_clean["Pobreza_pct"], errors='coerce')
    df_clean["Pobreza_extrema_pct"] = pd.to_numeric(df_clean["Pobreza_extrema_pct"], errors='coerce')
    df_clean["Carencia_servicios_pct"] = pd.to_numeric(df_clean["Carencia_servicios_pct"], errors='coerce')
    
    out_path = "datos/coneval_clean_2020.csv"
    df_clean.to_csv(out_path, index=False)
    print(f"Datos de CONEVAL procesados y guardados en {out_path}")
    
    # Estadísticas rápidas para el análisis
    print("\n--- Resumen Estadístico CONEVAL ---")
    print(df_clean.describe())

if __name__ == "__main__":
    process_coneval()
