## Documentación del Proyecto

### Actividad 1: Recolección de información y generación del archivo XLS

Pasos:
1. Elección de url donde sacaremos la información para trabajar, en esta caso será con el uso de la plataforma Mercado Libre con la búsqueda de relojes inteligentes "Smartwatch".
2. Organización de campos que usaremos, como lo son "Nombre o Producto", "Precios" y "Calificaciones".
3. Estructurar el código para que tome del HTML necesario de la página los campos requeridos, usando las librerías pandas, requests y BeautifulSoup.
4. Codificar para poder tomar la información de HTML y crear un archivo csv donde almacenaremos la información.

---

## Continuación del Proyecto: Automatización, Almacenamiento, Monitoreo y Alertas

Después de la Actividad 1, el proyecto evolucionó para incluir:

### 1. **Automatización del Scraping y Almacenamiento**
- El scraping se automatizó para ejecutarse desde un script principal.
- Los datos extraídos se almacenan primero en un archivo CSV y luego en una base de datos SQLite para facilitar su consulta y análisis.

### 2. **Ingesta de Datos**
- Se creó un módulo que toma el CSV generado por el scraper y lo ingresa a la base de datos, asegurando que la información esté centralizada y lista para análisis posteriores.

### 3. **Monitoreo y Métricas**
- Se implementó un sistema de monitoreo que:
  - Cuenta los registros en la base de datos.
  - Calcula métricas como precio promedio, mínimo y máximo, y detecta productos con precios nulos o datos faltantes.
  - Guarda un historial de estas métricas en un archivo de logs JSON, permitiendo revisar la evolución de los datos.

### 4. **Alertas Automáticas**
- El sistema puede enviar alertas por correo electrónico con el TOP 4 de productos más baratos, mostrando los precios en pesos colombianos con tres decimales.
- Las alertas se configuran mediante variables de entorno para mayor seguridad.

### 5. **Ejecución Automática (CI/CD)**
- Se añadió un workflow de GitHub Actions para ejecutar automáticamente el scraping, la ingesta y el monitoreo cada vez que hay cambios en el repositorio.

---

## ¿Cómo usar el proyecto?

1. **Extraer datos de Mercado Libre y guardarlos en CSV:**
   ```sh
   python -m edu_pad.main_extractora
   ```

2. **Cargar los datos del CSV a la base de datos:**
   ```sh
   python -m edu_pad.main_ingesta
   ```

3. **Monitorear la base de datos y enviar alertas:**
   ```sh
   python -m edu_pad.monitor
   ```

---

## Resumen de la estructura actual

```
Activida1Scraping/
│
├── src/
│   └── edu_pad/
│       ├── dataweb.py           # Scraper de Mercado Libre
│       ├── database.py          # Gestión de base de datos SQLite
│       ├── main_extractora.py   # Ejecuta el scraping y guarda CSV
│       ├── main_ingesta.py      # Ingresa datos del CSV a la base de datos
│       ├── monitor.py           # Monitorea la base de datos y envía alertas
│       └── static/
│           ├── csv/
│           │   └── data_extractora.csv
│           ├── db/
│           │   └── productos_analisis.db
│           └── logs/
│               └── monitor_log.json
│
├── .github/workflows/main.yml   # Pipeline de CI/CD
└── README.md
```

---

- **Automatización con GitHub Actions:**  
  Solo la parte de ingestación de datos (`main_ingesta.py`) está configurada para ejecutarse automáticamente mediante las acciones de GitHub (CI/CD). Esto significa que, cuando hay un push a la rama principal, el pipeline ejecuta la ingesta de datos de forma automática.

- **Ejecución manual requerida:**  
  La generación de la base de datos, la lectura, el monitoreo, los cálculos y el envío de alertas **deben ser iniciados manualmente por el usuario** ejecutando el archivo `monitor.py`.  
  Para hacerlo, usa el siguiente comando desde la carpeta `src`:
  ```sh
  python -m edu_pad.monitor
  ```

---

**Importante:**  
El monitoreo y las alertas NO se ejecutan automáticamente desde GitHub Actions. El usuario debe lanzar el monitoreo manualmente ejecutando desde la carpeta del proyecto al siguiente código: python -m src.edu_pad.monitor

**Este proyecto es una continuación y mejora de la actividad anterior, integrando scraping, almacenamiento, monitoreo y alertas automáticas para el análisis de precios de smartwatches en Colombia.**