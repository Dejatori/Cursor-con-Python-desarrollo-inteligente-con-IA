"""
Análisis de ventas
------------------
Este script carga datos de ventas desde un archivo CSV, calcula estadísticas clave y genera gráficos:
- Ventas totales por mes
- Producto más vendido y producto con mayores ingresos
- Gráficos de ventas por mes y top 5 productos por ingresos

Autor: Dejatori
"""

import pandas as pd
import matplotlib.pyplot as plt

def cargar_datos(ruta_csv):
    """
    Carga los datos de ventas desde un archivo CSV.

    Args:
        ruta_csv (str): Ruta al archivo CSV.

    Returns:
        pd.DataFrame: DataFrame con los datos cargados.
    """
    return pd.read_csv(ruta_csv, parse_dates=['fecha'])

def calcular_ventas_por_mes(df):
    """
    Calcula las ventas totales por mes.

    Args:
        df (pd.DataFrame): DataFrame con los datos de ventas.

    Returns:
        pd.Series: Ventas totales por mes.
    """
    df['fecha'] = pd.to_datetime(df['fecha'])
    df['mes'] = df['fecha'].dt.to_period('M')
    return df.groupby('mes').apply(lambda x: (x['cantidad'] * x['precio']).sum())

def calcular_ventas_por_producto(df):
    """
    Calcula la cantidad total vendida y los ingresos por producto.

    Args:
        df (pd.DataFrame): DataFrame con los datos de ventas.

    Returns:
        pd.DataFrame: DataFrame con columnas 'producto', 'cantidad' e 'ingresos'.
    """
    df['ingresos'] = df['cantidad'] * df['precio']
    return df.groupby('producto').agg({'cantidad': 'sum', 'ingresos': 'sum'}).reset_index()

def mostrar_estadisticas(ventas_por_producto):
    """
    Imprime el producto más vendido y el de mayor ingreso.

    Args:
        ventas_por_producto (pd.DataFrame): DataFrame con ventas por producto.
    """
    mas_vendido = ventas_por_producto.loc[ventas_por_producto['cantidad'].idxmax()]
    mayor_ingreso = ventas_por_producto.loc[ventas_por_producto['ingresos'].idxmax()]
    print(f"Producto más vendido: {mas_vendido['producto']} con {mas_vendido['cantidad']} unidades")
    print(f"Producto con mayor ingresos: {mayor_ingreso['producto']} con {mayor_ingreso['ingresos']} ingresos")

def graficar_ventas_por_mes(ventas_por_mes, ruta_guardado):
    """
    Genera y guarda un gráfico de barras de ventas por mes.

    Args:
        ventas_por_mes (pd.Series): Ventas totales por mes.
        ruta_guardado (str): Ruta para guardar la imagen.
    """
    # Convertir el índice a string para que matplotlib lo entienda
    ventas_por_mes.index = ventas_por_mes.index.astype(str)
    plt.figure(figsize=(10, 6))
    ventas_por_mes.plot(kind='bar', color='skyblue')
    plt.title('Ventas por Mes')
    plt.xlabel('Mes')
    plt.ylabel('Ingresos ($)')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(ruta_guardado)
    plt.show()

def graficar_top_productos(ventas_por_producto, ruta_guardado, top_n=5):
    """
    Genera y guarda un gráfico de barras de los productos con mayores ingresos.

    Args:
        ventas_por_producto (pd.DataFrame): DataFrame con ventas por producto.
        ruta_guardado (str): Ruta para guardar la imagen.
        top_n (int): Número de productos a mostrar.
    """
    top_productos = ventas_por_producto.nlargest(top_n, 'ingresos')
    plt.figure(figsize=(10, 6))
    top_productos.plot(kind='bar', x='producto', y='ingresos', color='salmon')
    plt.title(f'Top {top_n} Productos por Ingresos')
    plt.xlabel('Producto')
    plt.ylabel('Ingresos ($)')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(ruta_guardado)
    plt.show()

def main():
    """
    Función principal que ejecuta el análisis de ventas.
    """
    # Cargar datos
    df = cargar_datos('analisis_ventas/ventas.csv')

    # Calcular ventas por mes
    ventas_por_mes = calcular_ventas_por_mes(df)
    print("Ventas totales por mes:")
    print(ventas_por_mes)

    # Calcular ventas por producto y mostrar estadísticas
    ventas_por_producto = calcular_ventas_por_producto(df)
    mostrar_estadisticas(ventas_por_producto)

    # Graficar ventas por mes
    graficar_ventas_por_mes(ventas_por_mes, 'analisis_ventas/grafico_ventas_por_mes.png')

    # Graficar top 5 productos por ingresos
    graficar_top_productos(ventas_por_producto, 'analisis_ventas/grafico_top_5_productos.png', top_n=5)

if __name__ == "__main__":
    main()
