# Gestor de Tareas

Aplicación web sencilla para la gestión de tareas (to-do list) desarrollada con Flask.

## Descripción

Este proyecto permite a los usuarios agregar tareas, marcarlas como completadas y almacenar la lista de tareas en un archivo JSON. Es ideal como ejemplo educativo de una aplicación CRUD básica usando Python y Flask.

## Requisitos del sistema

- Python 3.7 o superior
- pip (gestor de paquetes de Python)

## Instalación

1. Clona este repositorio o descarga los archivos del proyecto.
2. Instala las dependencias necesarias ejecutando:

```bash
pip install -r requirements.txt
```

## Ejecución

1. Ejecuta el archivo principal:

```bash
python app.py
```

2. Abre tu navegador y accede a `http://127.0.0.1:5000/` para usar la aplicación.

## Ejemplo de uso

- Agrega una nueva tarea usando el formulario.
- Marca una tarea como completada haciendo clic en "Completar".
- Las tareas se guardan automáticamente en el archivo `tareas.json`.

## Estructura del proyecto

- `app.py`: Lógica principal de la aplicación Flask.
- `templates/index.html`: Plantilla HTML para la interfaz de usuario.
- `tareas.json`: Archivo generado automáticamente para almacenar las tareas.
- `requirements.txt`: Dependencias del proyecto.

## Licencia

Este proyecto se distribuye bajo la licencia MIT. Puedes usarlo, modificarlo y distribuirlo libremente.
