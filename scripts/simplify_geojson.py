import sys
try:
    import geopandas as gpd
except ImportError:
    print("Error: Geopandas no esta instalado. Instalar con: pip install geopandas")
    sys.exit(1)

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

files_to_process = [
    ('Disponibilidad_Cuencas_2020.json', 'Disponibilidad_Cuencas_2020_lite.json'),
    ('Estado.json', 'Estado_lite.json')
]

for in_name, out_name in files_to_process:
    input_path = os.path.join(BASE_DIR, 'datos', in_name)
    output_path = os.path.join(BASE_DIR, 'datos', out_name)

    print(f"Cargando {in_name}...")
    gdf = gpd.read_file(input_path)

    # Simplificar los polígonos conservando la integridad topológica
    # tolerance=0.015 grados approx 1.5 km
    print(f"Procesando reduccion poligonal para {in_name}...")
    gdf.geometry = gdf.geometry.simplify(tolerance=0.015, preserve_topology=True)

    print(f"Exportando {out_name}...")
    gdf.to_file(output_path, driver='GeoJSON')
    file_size = os.path.getsize(output_path) / (1024 * 1024)
    print(f"¡Completado! Nuevo GeoJSON guardado en {output_path}")
    print(f"Nuevo tamaño: {file_size:.2f} MB\n")
