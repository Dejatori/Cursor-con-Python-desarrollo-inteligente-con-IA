# Análisis de Ventas

Este proyecto realiza un análisis exploratorio de datos de ventas a partir de un archivo CSV, generando estadísticas clave y gráficos visuales para facilitar la interpretación de los resultados.

## Descripción General

El script principal carga los datos de ventas, calcula las ventas totales por mes, identifica el producto más vendido y el de mayor ingreso, y genera gráficos de barras para visualizar la información. Es ideal para pequeñas empresas o proyectos educativos que requieran un análisis rápido y visual de sus ventas.

## Requisitos del Sistema

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Sistema operativo compatible con Python (Windows, macOS, Linux)

## Instalación

1. Clona este repositorio o descarga los archivos del proyecto.
2. Instala las dependencias necesarias ejecutando:

```bash
pip install -r requirements.txt
```

## Ejecución

Asegúrate de que el archivo `ventas.csv` se encuentra en la carpeta `analisis_ventas/`.

Para ejecutar el análisis y generar los gráficos, ejecuta el siguiente comando en la terminal:

```bash
python analisis.py
```

Se generarán dos archivos de imagen en la carpeta `analisis_ventas/`:

- `grafico_ventas_por_mes.png`: Gráfico de ventas totales por mes.
- `grafico_top_5_productos.png`: Gráfico de los 5 productos con mayores ingresos.

## Ejemplo de Uso

```
Ventas totales por mes:
mes
2025-01    50.0
2025-02    40.0
...
Producto más vendido: A con 40 unidades
Producto con mayor ingresos: B con 440.0 ingresos
```

## Estructura del Proyecto

- `analisis.py`: Script principal de análisis y visualización.
- `analisis_ventas/ventas.csv`: Archivo de datos de ventas (ejemplo).
- `analisis_ventas/grafico_ventas_por_mes.png`: Gráfico generado por el script.
- `analisis_ventas/grafico_top_5_productos.png`: Gráfico generado por el script.
- `requirements.txt`: Dependencias necesarias.

## Licencia

Este proyecto se distribuye bajo la licencia MIT. Puedes usarlo, modificarlo y distribuirlo libremente.
