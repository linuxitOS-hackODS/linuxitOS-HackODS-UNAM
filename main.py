import subprocess
import sys
import os

def run_script(script_path):
    print(f"\n{'-'*50}")
    print(f"[INFO] Ejecutando módulo: {script_path}")
    print(f"{'-'*50}")
    try:
        # Usar subprocess para llamar al script de python
        result = subprocess.run([sys.executable, script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"\n[ERROR] Falla en la ejecución de {script_path}. Abortando pipeline.")
        sys.exit(1)
    except Exception as e:
        print(f"\n[FATAL] Error inesperado en el módulo {script_path}: {e}")
        sys.exit(1)

def main():
    print("Iniciando Pipeline Automatizado de Datos (ETL): HackODS UNAM 2026 - linuxitOS\n")
    
    # Ajuste dinámico del directorio de trabajo (soporte para Terminal vs Jupyter Notebooks)
    # Si Jupyter lanza la libreta desde la carpeta 'notebooks/', bajamos un nivel para poder ver 'scripts/'.
    if not os.path.exists('scripts') and os.path.exists(os.path.join('..', 'scripts')):
        os.chdir('..')
        print("[INFO] Entorno Jupyter Notebook detectado. El directorio de trabajo se ajustó a la raíz del proyecto.\n")
    elif not os.path.exists('scripts'):
         print("[ERROR] El entorno no pudo localizar la carpeta 'scripts/'.")
         print("        Asegúrate de ejecutar desde la raíz del repositorio o dentro de la carpeta 'notebooks/'.")
         sys.exit(1)

    # Orden secuencial de ejecución para la integración del dataset maestro
    pipeline = [
        "scripts/siods_extractor.py",
        "scripts/analyze_iter.py",
        "scripts/clean_coneval.py",
        "scripts/merge_inegi_coneval.py",
        "scripts/merge_shcp.py",
        "scripts/merge_conagua.py",
        "scripts/simplify_geojson.py"
    ]

    for script in pipeline:
        run_script(script)

    print("\n[ÉXITO] Pipeline ETL concluido satisfactoriamente.")
    print("[INFO] El dataset analítico 'final_merged_data.csv' ha sido generado exitosamente.")
    print("[INFO] Para compilar el dashboard Quarto, ejecute el siguiente comando:")
    print("       quarto render dashboard/index.qmd")

if __name__ == "__main__":
    main()
