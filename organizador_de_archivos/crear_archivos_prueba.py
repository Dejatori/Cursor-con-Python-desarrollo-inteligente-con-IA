#!/usr/bin/env python3
"""
Script para crear archivos de prueba para el organizador de archivos.
Este script crea archivos ficticios de diferentes tipos para demostrar
el funcionamiento del organizador.
"""

import os
from pathlib import Path
import random
import string


def generar_nombre_aleatorio(longitud=8):
    """Genera un nombre de archivo aleatorio."""
    letras = string.ascii_lowercase
    return ''.join(random.choice(letras) for _ in range(longitud))


def crear_archivo_prueba(directorio, nombre, contenido=""):
    """Crea un archivo de prueba con contenido específico."""
    ruta_archivo = directorio / nombre
    with open(ruta_archivo, 'w', encoding='utf-8') as f:
        f.write(f"Este es un archivo de prueba: {nombre}\n")
        f.write(f"Contenido generado automáticamente para demostrar el organizador.\n")
        f.write(contenido)
    return ruta_archivo


def crear_archivos_prueba():
    """Crea una variedad de archivos de prueba para demostrar el organizador."""
    
    # Directorio de prueba
    directorio_prueba = Path("carpeta_de_prueba")
    directorio_prueba.mkdir(exist_ok=True)
    
    print("🗂️  CREANDO ARCHIVOS DE PRUEBA")
    print("=" * 50)
    print(f"📁 Directorio de prueba: {directorio_prueba.absolute()}")
    print()
    
    # Lista de archivos a crear con sus extensiones
    archivos_prueba = [
        # Imágenes
        ("foto_vacaciones.jpg", "Foto de vacaciones en la playa"),
        ("captura_pantalla.png", "Captura de pantalla del sistema"),
        ("logo_empresa.gif", "Logo animado de la empresa"),
        ("imagen_webp.webp", "Imagen optimizada para web"),
        
        # Documentos
        ("informe_2024.pdf", "Informe anual 2024"),
        ("presentacion.pptx", "Presentación de ventas"),
        ("datos_ventas.xlsx", "Hoja de cálculo con datos de ventas"),
        ("notas_reunion.txt", "Notas de la reunión de ayer"),
        ("documento_word.docx", "Documento de Word con formato"),
        
        # Videos
        ("tutorial_python.mp4", "Video tutorial de Python"),
        ("presentacion_equipo.avi", "Presentación del equipo"),
        ("demo_producto.mkv", "Demostración del producto"),
        
        # Música
        ("cancion_favorita.mp3", "Mi canción favorita"),
        ("podcast_tecnologia.wav", "Podcast sobre tecnología"),
        ("musica_relajante.flac", "Música para relajarse"),
        
        # Comprimidos
        ("backup_datos.zip", "Respaldo de datos importantes"),
        ("documentos_rar.rar", "Documentos comprimidos"),
        
        # Programas
        ("instalador_app.exe", "Instalador de aplicación"),
        ("actualizacion.msi", "Actualización del sistema"),
        
        # Otros (extensiones no reconocidas)
        ("configuracion.conf", "Archivo de configuración"),
        ("datos_exportados.csv", "Datos exportados en CSV"),
        ("script_python.py", "Script de Python"),
        ("archivo_markdown.md", "Documento en Markdown"),
    ]
    
    archivos_creados = []
    
    for nombre_archivo, descripcion in archivos_prueba:
        ruta = crear_archivo_prueba(directorio_prueba, nombre_archivo, descripcion)
        archivos_creados.append(ruta)
        print(f"✓ Creado: {nombre_archivo}")
    
    print()
    print("=" * 50)
    print("📊 RESUMEN DE ARCHIVOS CREADOS")
    print("=" * 50)
    print(f"📁 Total de archivos creados: {len(archivos_creados)}")
    print(f"📂 Ubicación: {directorio_prueba.absolute()}")
    print()
    print("💡 Ahora puedes ejecutar el organizador:")
    print(f"   python organizar.py \"{directorio_prueba.absolute()}\"")
    print()
    print("⚠️  Recuerda: Estos son archivos de prueba. Puedes eliminarlos después.")
    
    return directorio_prueba


def limpiar_archivos_prueba():
    """Elimina los archivos de prueba creados."""
    directorio_prueba = Path("carpeta_de_prueba")
    
    if directorio_prueba.exists():
        import shutil
        shutil.rmtree(directorio_prueba)
        print(f"🗑️  Eliminado directorio de prueba: {directorio_prueba}")
    else:
        print("📁 No se encontró directorio de prueba para eliminar.")


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--limpiar":
        limpiar_archivos_prueba()
    else:
        crear_archivos_prueba() 
