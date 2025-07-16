# Contador de Palabras

## Descripción

Este proyecto es un sencillo script en Python que permite contar el número total de palabras en un archivo de texto y mostrar las 10 palabras más frecuentes junto con su frecuencia de aparición. Es ideal para análisis exploratorio de textos, estadísticas básicas o como ejemplo educativo de procesamiento de cadenas en Python.

## Requisitos del sistema

- Python 3.6 o superior
- No requiere librerías externas (solo usa la biblioteca estándar de Python)

## Instalación

1. Clona este repositorio o descarga los archivos `contador.py` y `test_contador.py`.
2. (Opcional) Crea y activa un entorno virtual para aislar dependencias:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

## Ejecución

Para ejecutar el script principal y analizar un archivo de texto:

```bash
python contador.py
```

Se te pedirá que ingreses la ruta del archivo de texto a analizar.

## Ejemplo de uso

Supón que tienes un archivo llamado `prueba.txt` con el siguiente contenido:

```
Hola mundo. Hola Python. Python es genial.
```

Al ejecutar el script e ingresar la ruta de `prueba.txt`, la salida será similar a:

```
Total de palabras: 7

Las 10 palabras más frecuentes:
hola: 2
python: 2
mundo: 1
es: 1
genial: 1
```

## Pruebas

El archivo `test_contador.py` contiene pruebas unitarias para la función principal. Puedes ejecutarlas con:

```bash
python test_contador.py
```

## Licencia

Este proyecto se distribuye bajo la licencia MIT. Puedes usarlo, modificarlo y distribuirlo libremente.
