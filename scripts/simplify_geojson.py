import sys
try:
    import geopandas as gpd
except ImportError:
    print("Error: Geopandas no esta instalado. Instalar con: pip install geopandas")
    sys.exit(1)

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
input_path = os.path.join(BASE_DIR, 'datos', 'Disponibilidad_Cuencas_2020.json')
output_path = os.path.join(BASE_DIR, 'datos', 'Disponibilidad_Cuencas_2020_lite.json')

print("Cargando GeoJSON masivo (18.5 MB)...")
gdf = gpd.read_file(input_path)

# Simplificar los polígonos conservando la integridad topológica
# tolerance=0.015 grados approx 1.5 km
print("Procesando reduccion poligonal...")
gdf.geometry = gdf.geometry.simplify(tolerance=0.015, preserve_topology=True)

print("Exportando a archivo hiper-ligero...")
gdf.to_file(output_path, driver='GeoJSON')
file_size = os.path.getsize(output_path) / (1024 * 1024)
print(f"¡Completado! Nuevo GeoJSON guardado en {output_path}")
print(f"Nuevo tamaño: {file_size:.2f} MB")
