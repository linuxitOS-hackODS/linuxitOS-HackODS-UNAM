import requests
import json
import pandas as pd
import os
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Configuración de la API oculta de SIODS
URL_API = "https://agenda2030.mx/ods/api/Valores/PorClave"
HEADERS = {"Content-Type": "application/json"}

# Indicadores a extraer (actualizado con el descubrimiento del "Punto Ciego Estatal")
# 6.1.1.c = PCveInd: 618, PCveSer: 2073 (Proporción estatal de agua potable segura)
# 6.2.1.c = PCveInd: 620, PCveSer: 2079 (Proporción estatal de saneamiento seguro - asumido como ejemplo cercano, o nos quedamos con el nacional 192 si no tenemos la serie exacta, pero priorizaremos el 618)
INDICADORES_SIODS = [
    {"nombre": "ODS_6.1.1.a_Nacional_Agua_Segura", "PCveInd": 54, "PCveSer": 2015},
    {"nombre": "ODS_6.1.1.c_Estatal_Agua_Segura", "PCveInd": 618, "PCveSer": 2073},
]


def extraer_siods(ind_config):
    payload = {
        "PCveInd": ind_config["PCveInd"],
        "PCveSer": ind_config["PCveSer"],
        "POrden": "DESC",
        "PCveAgrupaCla": "99",
        "PIdioma": "ES",
    }

    try:
        response = requests.post(URL_API, json=payload, headers=HEADERS, verify=False)
        if response.status_code == 200:
            data = response.json()

            series = data.get("Series", [])
            if not series:
                return None

            serie = series[0]
            coberturas = serie.get("Coberturas", [])

            resultados = []
            for cob in coberturas:
                clave_geo = cob.get("ClaveCobGeo_cg", "00")
                desc_geo = cob.get("Descrip_cg", "Nacional")

                for obs in cob.get("ValorDato", []):
                    resultados.append(
                        {
                            "Indicador": ind_config["nombre"],
                            "Clave_Entidad": clave_geo,
                            "Entidad": desc_geo,
                            "Año": obs.get("AADato_ser"),
                            "Valor": obs.get("Dato_ser"),
                        }
                    )

            return pd.DataFrame(resultados)
        else:
            print(f"Error {response.status_code} al consultar {ind_config['nombre']}")
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None


def ejecutar_pipeline():
    print("Iniciando extracción desde la API de SIODS (Agenda 2030)...")

    df_list = []
    for config in INDICADORES_SIODS:
        print(f"Extrayendo: {config['nombre']}")
        df = extraer_siods(config)
        if df is not None and not df.empty:
            df_list.append(df)

    if df_list:
        df_final = pd.concat(df_list, ignore_index=True)

        ruta_salida = "../datos/siods_agua_saneamiento_nacional.csv"
        os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)
        df_final.to_csv(ruta_salida, index=False)

        print(f"\nExtracción exitosa. Guardado en {ruta_salida}")
        print("\n--- Análisis de Granularidad (El Punto Ciego) ---")
        entidades_unicas = df_final["Entidad"].unique()
        print(f"Total de entidades geográficas extraídas: {len(entidades_unicas)}")
        print(
            "La base contiene datos Nacionales y Estatales, confirmando la necesidad de pivotar a datos Municipales (CONEVAL) para evaluar zonas rurales."
        )


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    ejecutar_pipeline()
