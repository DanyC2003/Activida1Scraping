from edu_pad.dataweb import DataWeb

def main():
    print("Ejecutando scraping de productos de Mercado Libre...")
    dw = DataWeb()
    dw.obtener_datos()
    print("Proceso finalizado.")

if __name__ == "__main__":
    main()