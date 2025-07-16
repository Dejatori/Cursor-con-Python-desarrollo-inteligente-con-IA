#!/usr/bin/env python3
"""
Organizador de Archivos
=======================

Script que organiza automáticamente archivos en subcarpetas según su tipo de extensión.
Utiliza pathlib para operaciones de archivos y es compatible con Python 3.10+.

Autor: Dejatori
Fecha: 2025
"""

import os
import shutil
from pathlib import Path
from typing import Dict, List, Optional


class OrganizadorArchivos:
    """Clase principal para organizar archivos por categorías."""
    
    def __init__(self, directorio_objetivo: Optional[Path] = None):
        """
        Inicializa el organizador de archivos.
        
        Args:
            directorio_objetivo: Directorio a organizar. Si es None, usa Downloads.
        """
        self.directorio_objetivo = directorio_objetivo or Path.home() / "Downloads"
        
        # Mapeo de extensiones a categorías
        self.categorias = {
            "Imágenes": [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tiff", ".webp"],
            "Documentos": [".pdf", ".docx", ".txt", ".xlsx", ".doc", ".xls", ".ppt", ".pptx"],
            "Videos": [".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm"],
            "Música": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a"],
            "Comprimidos": [".zip", ".rar", ".7z", ".tar", ".gz"],
            "Programas": [".exe", ".msi", ".dmg", ".pkg", ".deb", ".rpm"],
            "Otros": []  # Para extensiones no reconocidas
        }
        
        # Contador de archivos movidos por categoría
        self.contador_movimientos = {categoria: 0 for categoria in self.categorias.keys()}
    
    def obtener_categoria(self, extension: str) -> str:
        """
        Determina la categoría de un archivo basándose en su extensión.
        
        Args:
            extension: Extensión del archivo (incluyendo el punto)
            
        Returns:
            Nombre de la categoría correspondiente
        """
        extension = extension.lower()
        
        for categoria, extensiones in self.categorias.items():
            if extension in extensiones:
                return categoria
        
        return "Otros"
    
    def crear_directorio_si_no_existe(self, directorio: Path) -> None:
        """
        Crea un directorio si no existe.
        
        Args:
            directorio: Ruta del directorio a crear
        """
        if not directorio.exists():
            directorio.mkdir(parents=True, exist_ok=True)
            print(f"✓ Creado directorio: {directorio}")
    
    def obtener_nombre_unico(self, archivo_destino: Path) -> Path:
        """
        Genera un nombre único para evitar sobrescribir archivos existentes.
        
        Args:
            archivo_destino: Ruta del archivo de destino
            
        Returns:
            Ruta con nombre único
        """
        if not archivo_destino.exists():
            return archivo_destino
        
        # Si el archivo existe, agregar un sufijo numérico
        contador = 1
        nombre_base = archivo_destino.stem
        extension = archivo_destino.suffix
        directorio = archivo_destino.parent
        
        while archivo_destino.exists():
            nuevo_nombre = f"{nombre_base}_{contador}{extension}"
            archivo_destino = directorio / nuevo_nombre
            contador += 1
        
        return archivo_destino
    
    def mover_archivo(self, archivo_origen: Path, categoria: str) -> bool:
        """
        Mueve un archivo a su categoría correspondiente.
        
        Args:
            archivo_origen: Ruta del archivo a mover
            categoria: Categoría de destino
            
        Returns:
            True si el archivo fue movido exitosamente, False en caso contrario
        """
        try:
            # Crear directorio de categoría
            directorio_categoria = self.directorio_objetivo / categoria
            self.crear_directorio_si_no_existe(directorio_categoria)
            
            # Generar ruta de destino con nombre único
            archivo_destino = directorio_categoria / archivo_origen.name
            archivo_destino = self.obtener_nombre_unico(archivo_destino)
            
            # Mover el archivo
            archivo_origen.rename(archivo_destino)
            
            # Actualizar contador
            self.contador_movimientos[categoria] += 1
            
            print(f"✓ Movido: {archivo_origen.name} → {categoria}/")
            return True
            
        except Exception as e:
            print(f"✗ Error moviendo {archivo_origen.name}: {e}")
            return False
    
    def organizar_archivos(self) -> None:
        """
        Función principal que organiza todos los archivos en el directorio objetivo.
        """
        print(f"🔍 Escaneando directorio: {self.directorio_objetivo}")
        print("=" * 50)
        
        # Verificar que el directorio existe
        if not self.directorio_objetivo.exists():
            print(f"❌ Error: El directorio {self.directorio_objetivo} no existe.")
            return
        
        # Obtener nombre del script actual para omitirlo
        script_actual = Path(__file__).name
        
        archivos_procesados = 0
        archivos_movidos = 0
        
        # Iterar sobre todos los archivos en el directorio
        for archivo in self.directorio_objetivo.iterdir():
            # Omitir directorios y el script actual
            if archivo.is_dir() or archivo.name == script_actual:
                continue
            
            archivos_procesados += 1
            
            # Determinar categoría basándose en la extensión
            extension = archivo.suffix
            categoria = self.obtener_categoria(extension)
            
            # Mover archivo a su categoría
            if self.mover_archivo(archivo, categoria):
                archivos_movidos += 1
        
        # Mostrar resumen
        self.mostrar_resumen(archivos_procesados, archivos_movidos)
    
    def mostrar_resumen(self, archivos_procesados: int, archivos_movidos: int) -> None:
        """
        Muestra un resumen de la operación de organización.
        
        Args:
            archivos_procesados: Total de archivos procesados
            archivos_movidos: Total de archivos movidos exitosamente
        """
        print("\n" + "=" * 50)
        print("📊 RESUMEN DE LA ORGANIZACIÓN")
        print("=" * 50)
        
        print(f"📁 Archivos procesados: {archivos_procesados}")
        print(f"✅ Archivos movidos: {archivos_movidos}")
        
        if archivos_movidos > 0:
            print("\n📂 Archivos movidos por categoría:")
            for categoria, cantidad in self.contador_movimientos.items():
                if cantidad > 0:
                    print(f"   • {categoria}: {cantidad} archivo(s)")
        
        if archivos_procesados == 0:
            print("\n💡 No se encontraron archivos para organizar.")
        elif archivos_movidos == 0:
            print("\n💡 No se movió ningún archivo.")
        else:
            print(f"\n🎉 ¡Organización completada! {archivos_movidos} archivo(s) organizado(s).")


def main():
    """
    Función principal del script.
    """
    import sys
    
    print("🗂️  ORGANIZADOR DE ARCHIVOS")
    print("=" * 50)
    
    # Determinar directorio objetivo
    if len(sys.argv) > 1:
        directorio_objetivo = Path(sys.argv[1])
        if not directorio_objetivo.exists():
            print(f"❌ Error: El directorio '{directorio_objetivo}' no existe.")
            print("💡 Uso: python organizar.py [directorio]")
            return
    else:
        # Usar Downloads por defecto
        directorio_objetivo = Path.home() / "Downloads"
        print(f"📁 Usando directorio por defecto: {directorio_objetivo}")
    
    # Confirmar con el usuario
    print(f"\n⚠️  ADVERTENCIA: Este script moverá archivos en {directorio_objetivo}")
    print("💡 Se recomienda hacer una copia de seguridad antes de continuar.")
    
    respuesta = input("\n¿Desea continuar? (s/N): ").strip().lower()
    if respuesta not in ['s', 'si', 'sí', 'y', 'yes']:
        print("❌ Operación cancelada por el usuario.")
        return
    
    # Crear y ejecutar el organizador
    organizador = OrganizadorArchivos(directorio_objetivo)
    organizador.organizar_archivos()


if __name__ == "__main__":
    main()
