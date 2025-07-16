"""
Contador de Palabras
--------------------
Script para contar el número total de palabras y mostrar las palabras más frecuentes en un archivo de texto.
"""

import re
from collections import Counter

def contar_palabras(texto):
    """
    Cuenta el número total de palabras y la frecuencia de cada palabra en un texto dado.

    Args:
        texto (str): Texto a analizar.

    Returns:
        tuple: Una tupla (total_palabras, contador_palabras) donde:
            - total_palabras (int): Número total de palabras encontradas.
            - contador_palabras (collections.Counter): Frecuencia de cada palabra.
    """
    # Extrae todas las palabras (alfanuméricas) ignorando mayúsculas/minúsculas
    palabras = re.findall(r'\b\w+\b', texto.lower())
    total_palabras = len(palabras)
    contador_palabras = Counter(palabras)
    return total_palabras, contador_palabras


def main():
    """
    Función principal del script. Solicita la ruta de un archivo de texto,
    cuenta las palabras y muestra las 10 más frecuentes.
    """
    archivo = input("Ingrese la ruta del archivo de texto: ")

    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            contenido = f.read()
    except FileNotFoundError:
        print(f"El archivo {archivo} no existe.")
        return
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return

    total_palabras, contador = contar_palabras(contenido)
    print(f"Total de palabras: {total_palabras}")

    mas_comunes = contador.most_common(10)
    print("\nLas 10 palabras más frecuentes:")
    for palabra, conteo in mas_comunes:
        print(f"{palabra}: {conteo}")


if __name__ == "__main__":
    main()
