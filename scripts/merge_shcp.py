import pandas as pd
import os


def main():
    # Definir rutas absolutas basadas en la estructura del proyecto
    if "__file__" in globals():
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    else:
        base_dir = os.getcwd()
        if not os.path.exists(os.path.join(base_dir, 'scripts')):
            base_dir = os.path.dirname(base_dir)

    merged_path = os.path.join(base_dir, "datos", "final_merged_data.csv")
    shcp_path = os.path.join(base_dir, "datos", "derecho_agua_municipal.csv")

    print("[INFO] Instanciando dataframes (Dataset Maestro y SHCP)...")
    # Leer dataset principal (manteniendo CVEGEO como string para no perder ceros a la izquierda)
    df_main = pd.read_csv(merged_path, dtype={"CVEGEO": str})
    # Leer dataset de SHCP
    df_shcp = pd.read_csv(shcp_path)

    print("[INFO] Limpiando base de derechos de agua SHCP (Corte: 2020)...")
    # Filtrar solo el ciclo 2020 para alinear temporalmente con INEGI y CONEVAL
    df_shcp_2020 = df_shcp[df_shcp["ciclo"] == 2020].copy()

    # Construir la clave CVEGEO: 2 dígitos entidad + 3 dígitos municipio
    df_shcp_2020["CVEGEO"] = df_shcp_2020["id_entidad_federativa"].astype(
        str
    ).str.zfill(2) + df_shcp_2020["id_municipio"].astype(str).str.zfill(3)

    # Seleccionar columnas de interés para no saturar el dataset maestro
    cols_to_keep = [
        "CVEGEO",
        "monto_agua",
        "monto_recaudado_percapita",
        "tomas_pagadas",
    ]
    df_shcp_2020 = df_shcp_2020[cols_to_keep]

    # Limpiar las columnas financieras/tomas: Convertir a numérico y rellenar nulos con 0
    for col in ["monto_agua", "monto_recaudado_percapita", "tomas_pagadas"]:
        df_shcp_2020[col] = pd.to_numeric(df_shcp_2020[col], errors="coerce").fillna(0)

    print("[INFO] Ejecutando operación Left Join con estructura base...")
    # Realizar un left join para mantener todos los municipios que ya teníamos,
    # y simplemente añadir la información de recaudación.
    df_final = pd.merge(df_main, df_shcp_2020, on="CVEGEO", how="left")

    # Rellenar con 0 si algún municipio del main no existía en el padrón de SHCP
    for col in ["monto_agua", "monto_recaudado_percapita", "tomas_pagadas"]:
        df_final[col] = df_final[col].fillna(0)

    # Sobrescribir el dataset final
    print(f"[INFO] Escribiendo matriz transaccional en {merged_path}...")
    df_final.to_csv(merged_path, index=False)

    print(f"[ÉXITO] Dimensiones financieras integradas al espacio matricial.")
    print(f"[INFO] Verificando cabeceras financieras (n=5):")
    print(df_final[["CVEGEO", "Municipio", "monto_agua", "tomas_pagadas"]].head())


if __name__ == "__main__":
    main()
