import os
from edu_pad.dataweb import DataWeb

def main():
    print("Ejecutando scraping de productos de Mercado Libre...")
    dw = DataWeb()
    dw.obtener_datos()
    if not dw.empty:
        output_dir = "static/cvs"
        os.makedirs(output_dir, exist_ok=True)
        
        cvs_path = os.path.join(output_dir, "data_web.csv")
        dw.df.to_csv(cvs_path, index=False)

        print(f"Datos exportados a '{cvs_path}' correctamente.")
    else:
        print("No se encontraron datos para exportar.")
        

if __name__ == "__main__":
    main()