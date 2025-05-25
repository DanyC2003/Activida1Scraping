from edu_pad.database import Database

def main():
    print("Ejecutando scraping de productos de Mercado Libre...")
    db = Database()
    db.obtener_datos()
    print("Proceso finalizado.")

if __name__ == "__main__":
    main()