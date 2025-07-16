"""
app.py
-------
Aplicación Flask para gestionar una lista de tareas (to-do list).
Permite agregar tareas, marcarlas como completadas y guarda los datos en un archivo JSON.
"""

from flask import Flask, request, redirect, render_template
import json
import os

app = Flask(__name__)

tareas = []  # Lista global de tareas
siguiente_id = 1  # ID incremental para nuevas tareas

def agregar_tarea(texto):
    """
    Agrega una nueva tarea a la lista de tareas.

    Args:
        texto (str): El texto descriptivo de la tarea.
    """
    global siguiente_id
    tarea = {
        'id': siguiente_id,
        'texto': texto,
        'hecho': False
    }
    tareas.append(tarea)
    siguiente_id += 1


def completar_tarea(id):
    """
    Marca como completada la tarea con el id dado.

    Args:
        id (int): El identificador de la tarea a completar.
    """
    for tarea in tareas:
        if tarea['id'] == id:
            tarea['hecho'] = True
            break


def guardar_datos():
    """
    Guarda la lista de tareas en un archivo JSON.
    """
    with open('tareas.json', 'w', encoding='utf-8') as f:
        json.dump(tareas, f, ensure_ascii=False, indent=2)


def cargar_datos():
    """
    Carga la lista de tareas desde un archivo JSON si existe.

    Returns:
        list: Lista de tareas cargadas o lista vacía si no existe el archivo.
    """
    if os.path.exists('tareas.json'):
        with open('tareas.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    return []


@app.route('/')
def index():
    """
    Ruta principal. Muestra la lista de tareas ordenadas (no hechas primero).

    Returns:
        str: Renderizado HTML de la lista de tareas.
    """
    global tareas
    tareas = cargar_datos()
    tareas_ordenadas = sorted(tareas, key=lambda x: x['hecho'])
    return render_template('index.html', tareas=tareas_ordenadas)


@app.route('/agregar', methods=['POST'])
def agregar():
    """
    Ruta para agregar una nueva tarea desde el formulario.

    Returns:
        werkzeug.wrappers.Response: Redirección a la página principal.
    """
    texto = request.form['texto']
    agregar_tarea(texto)
    guardar_datos()
    return redirect('/')


@app.route('/completar/<int:id>')
def completar(id):
    """
    Ruta para marcar una tarea como completada.

    Args:
        id (int): El identificador de la tarea a completar.

    Returns:
        werkzeug.wrappers.Response: Redirección a la página principal.
    """
    completar_tarea(id)
    guardar_datos()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
