import os
from edu_pad.dataweb import DataWeb

def main_1():
    dw = DataWeb()
    df = dw.obtener_datos()
    
    # Crear la carpeta 'csv' dentro de 'static' del proyecto
    output_dir = os.path.join(os.path.dirname(__file__), "static", "csv")
    os.makedirs(output_dir, exist_ok=True)
    
    if not df.empty:
        df.to_csv(os.path.join(output_dir, "data_extractora.csv"), index=False)
    else:
        print("No se encontraron datos para guardar.")

if __name__ == "__main__":
    main_1()
