#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Editor de Notas - Aplicación de Bloc de Notas Simplificado
Desarrollado con Tkinter y Programación Orientada a Objetos
"""

import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import os


class EditorNotas(tk.Tk):
    """
    Clase principal que hereda de tk.Tk para crear la aplicación del editor de notas.
    Implementa una interfaz gráfica completa con funcionalidades de archivo.
    """
    
    def __init__(self):
        """Inicializa la aplicación del editor de notas."""
        super().__init__()
        
        # Configuración de la ventana principal
        self.title("Editor de Notas")
        self.geometry("600x400")
        self.minsize(400, 300)  # Tamaño mínimo para evitar ventanas muy pequeñas
        
        # Variable para rastrear si el archivo ha sido modificado
        self.archivo_actual = None
        self.contenido_original = ""
        self.modificado = False
        
        # Configurar el área de texto
        self.configurar_area_texto()
        
        # Configurar el menú
        self.configurar_menu()
        
        # Configurar eventos de teclado
        self.configurar_eventos()
        
        # Configurar el protocolo de cierre de ventana
        self.protocol("WM_DELETE_WINDOW", self.salir)
        
        # Enfocar el área de texto al iniciar
        self.area_texto.focus_set()
    
    def configurar_area_texto(self):
        """Configura el área de texto principal con scrollbars."""
        # Frame principal para contener el área de texto y scrollbars
        frame_texto = tk.Frame(self)
        frame_texto.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Área de texto con scrollbars integrados
        self.area_texto = scrolledtext.ScrolledText(
            frame_texto,
            wrap=tk.WORD,  # Salto de línea por palabras
            undo=True,     # Habilitar deshacer/rehacer
            maxundo=0,     # Sin límite para deshacer
            font=("Consolas", 10),  # Fuente monoespaciada para mejor legibilidad
            bg="white",    # Fondo blanco
            fg="black",    # Texto negro
            insertbackground="black",  # Color del cursor
            selectbackground="lightblue",  # Color de selección
            padx=10,       # Padding horizontal interno
            pady=10        # Padding vertical interno
        )
        self.area_texto.pack(fill=tk.BOTH, expand=True)
        
        # Configurar el área de texto para detectar cambios
        self.area_texto.bind("<Key>", self.marcar_modificado)
        self.area_texto.bind("<Button-1>", self.marcar_modificado)
    
    def configurar_menu(self):
        """Configura la barra de menú con todas las opciones."""
        # Crear la barra de menú
        self.menu_bar = tk.Menu(self)
        self.config(menu=self.menu_bar)
        
        # Menú Archivo
        self.menu_archivo = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Archivo", menu=self.menu_archivo)
        
        # Opciones del menú Archivo
        self.menu_archivo.add_command(label="Nuevo", command=self.nuevo_archivo, 
                                    accelerator="Ctrl+N")
        self.menu_archivo.add_command(label="Abrir...", command=self.abrir_archivo, 
                                    accelerator="Ctrl+O")
        self.menu_archivo.add_command(label="Guardar", command=self.guardar_archivo, 
                                    accelerator="Ctrl+S")
        self.menu_archivo.add_command(label="Guardar como...", command=self.guardar_como, 
                                    accelerator="Ctrl+Shift+S")
        self.menu_archivo.add_separator()
        self.menu_archivo.add_command(label="Salir", command=self.salir, 
                                    accelerator="Ctrl+Q")
        
        # Menú Editar
        self.menu_editar = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Editar", menu=self.menu_editar)
        
        # Opciones del menú Editar
        self.menu_editar.add_command(label="Deshacer", command=self.deshacer, 
                                   accelerator="Ctrl+Z")
        self.menu_editar.add_command(label="Rehacer", command=self.rehacer, 
                                   accelerator="Ctrl+Y")
        self.menu_editar.add_separator()
        self.menu_editar.add_command(label="Cortar", command=self.cortar, 
                                   accelerator="Ctrl+X")
        self.menu_editar.add_command(label="Copiar", command=self.copiar, 
                                   accelerator="Ctrl+C")
        self.menu_editar.add_command(label="Pegar", command=self.pegar, 
                                   accelerator="Ctrl+V")
        self.menu_editar.add_separator()
        self.menu_editar.add_command(label="Seleccionar todo", command=self.seleccionar_todo, 
                                   accelerator="Ctrl+A")
        
        # Menú Ayuda
        self.menu_ayuda = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Ayuda", menu=self.menu_ayuda)
        self.menu_ayuda.add_command(label="Acerca de", command=self.acerca_de)
    
    def configurar_eventos(self):
        """Configura los eventos de teclado para atajos."""
        # Atajos de teclado - solo los que no están manejados nativamente por Tkinter
        self.bind("<Control-n>", lambda e: self.nuevo_archivo())
        self.bind("<Control-o>", lambda e: self.abrir_archivo())
        self.bind("<Control-s>", lambda e: self.guardar_archivo())
        self.bind("<Control-S>", lambda e: self.guardar_como())  # Ctrl+Shift+S
        self.bind("<Control-q>", lambda e: self.salir())
        self.bind("<Control-a>", lambda e: self.seleccionar_todo())
        
        # No vincular Ctrl+X, Ctrl+C, Ctrl+V, Ctrl+Z, Ctrl+Y aquí para evitar duplicación
        # Estos eventos ya están manejados nativamente por Tkinter
    
    def marcar_modificado(self, event=None):
        """Marca el documento como modificado cuando se detecta un cambio."""
        # Obtener el contenido actual
        contenido_actual = self.area_texto.get(1.0, tk.END)
        
        # Solo marcar como modificado si el contenido realmente cambió
        if contenido_actual != self.contenido_original:
            if not self.modificado:
                self.modificado = True
                self.actualizar_titulo()
        else:
            # Si el contenido es igual al original, no está modificado
            if self.modificado:
                self.modificado = False
                self.actualizar_titulo()
    
    def actualizar_titulo(self):
        """Actualiza el título de la ventana para mostrar el estado del archivo."""
        titulo = "Editor de Notas"
        if self.archivo_actual:
            nombre_archivo = os.path.basename(self.archivo_actual)
            titulo = f"{nombre_archivo} - {titulo}"
        if self.modificado:
            titulo = f"*{titulo}"
        self.title(titulo)
    
    def nuevo_archivo(self):
        """Crea un nuevo archivo, preguntando si guardar cambios si es necesario."""
        if self.verificar_cambios_no_guardados():
            self.archivo_actual = None
            self.area_texto.delete(1.0, tk.END)
            self.contenido_original = ""
            self.modificado = False
            self.actualizar_titulo()
    
    def abrir_archivo(self):
        """Abre un archivo de texto existente."""
        if self.verificar_cambios_no_guardados():
            try:
                # Abrir diálogo para seleccionar archivo
                archivo = filedialog.askopenfilename(
                    title="Abrir archivo",
                    filetypes=[
                        ("Archivos de texto", "*.txt"),
                        ("Todos los archivos", "*.*")
                    ],
                    defaultextension=".txt"
                )
                
                if archivo:  # Si se seleccionó un archivo
                    self.cargar_archivo(archivo)
                    
            except Exception as e:
                messagebox.showerror(
                    "Error",
                    f"No se pudo abrir el archivo:\n{str(e)}"
                )
    
    def cargar_archivo(self, ruta_archivo):
        """Carga el contenido de un archivo en el área de texto."""
        try:
            # Intentar detectar la codificación del archivo
            codificaciones = ['utf-8', 'latin-1', 'cp1252']
            contenido = None
            
            for codificacion in codificaciones:
                try:
                    with open(ruta_archivo, 'r', encoding=codificacion) as archivo:
                        contenido = archivo.read()
                    break
                except UnicodeDecodeError:
                    continue
            
            if contenido is None:
                raise Exception("No se pudo leer el archivo. Posible archivo binario.")
            
            # Limpiar el área de texto y cargar el contenido
            self.area_texto.delete(1.0, tk.END)
            self.area_texto.insert(1.0, contenido)
            
            # Actualizar variables de estado
            self.archivo_actual = ruta_archivo
            self.contenido_original = contenido
            self.modificado = False
            self.actualizar_titulo()
            
            # Mover el cursor al inicio
            self.area_texto.see(1.0)
            
        except Exception as e:
            messagebox.showerror(
                "Error",
                f"No se pudo cargar el archivo '{ruta_archivo}':\n{str(e)}"
            )
    
    def guardar_archivo(self):
        """Guarda el archivo actual o abre diálogo si es nuevo."""
        if self.archivo_actual:
            self.guardar_contenido(self.archivo_actual)
        else:
            self.guardar_como()
    
    def guardar_como(self):
        """Abre diálogo para guardar archivo con nuevo nombre."""
        try:
            archivo = filedialog.asksaveasfilename(
                title="Guardar archivo como",
                filetypes=[
                    ("Archivos de texto", "*.txt"),
                    ("Todos los archivos", "*.*")
                ],
                defaultextension=".txt"
            )
            
            if archivo:
                self.guardar_contenido(archivo)
                
        except Exception as e:
            messagebox.showerror(
                "Error",
                f"No se pudo guardar el archivo:\n{str(e)}"
            )
    
    def guardar_contenido(self, ruta_archivo):
        """Guarda el contenido actual en el archivo especificado."""
        try:
            contenido = self.area_texto.get(1.0, tk.END)
            
            with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
                archivo.write(contenido)
            
            # Actualizar variables de estado
            self.archivo_actual = ruta_archivo
            self.contenido_original = contenido
            self.modificado = False
            self.actualizar_titulo()
            
            messagebox.showinfo(
                "Éxito",
                f"Archivo guardado exitosamente:\n{ruta_archivo}"
            )
            
        except Exception as e:
            messagebox.showerror(
                "Error",
                f"No se pudo guardar el archivo:\n{str(e)}"
            )
    
    def verificar_cambios_no_guardados(self):
        """Verifica si hay cambios no guardados y pregunta al usuario."""
        if self.modificado:
            respuesta = messagebox.askyesnocancel(
                "Cambios no guardados",
                "¿Desea guardar los cambios antes de continuar?",
                icon=messagebox.WARNING
            )
            
            if respuesta is None:  # Cancelar
                return False
            elif respuesta:  # Sí, guardar
                return self.guardar_archivo()
            # No, continuar sin guardar
        return True
    
    def salir(self):
        """Cierra la aplicación, verificando cambios no guardados."""
        if self.verificar_cambios_no_guardados():
            self.quit()
    
    # Métodos del menú Editar
    def deshacer(self):
        """Deshace la última acción."""
        try:
            self.area_texto.edit_undo()
            self.marcar_modificado()  # Marcar como modificado después de deshacer
        except tk.TclError:
            pass  # No hay nada que deshacer
    
    def rehacer(self):
        """Rehace la última acción deshecha."""
        try:
            self.area_texto.edit_redo()
            self.marcar_modificado()  # Marcar como modificado después de rehacer
        except tk.TclError:
            pass  # No hay nada que rehacer
    
    def cortar(self):
        """Corta el texto seleccionado."""
        try:
            # Usar directamente la funcionalidad de Tkinter
            self.area_texto.event_generate("<<Cut>>")
            self.marcar_modificado()  # Marcar como modificado después de cortar
        except tk.TclError:
            pass  # No hay texto seleccionado
    
    def copiar(self):
        """Copia el texto seleccionado."""
        try:
            # Usar directamente la funcionalidad de Tkinter
            self.area_texto.event_generate("<<Copy>>")
        except tk.TclError:
            pass  # No hay texto seleccionado
    
    def pegar(self):
        """Pega el texto del portapapeles."""
        try:
            # Usar directamente la funcionalidad de Tkinter
            self.area_texto.event_generate("<<Paste>>")
            self.marcar_modificado()  # Marcar como modificado después de pegar
        except tk.TclError:
            pass  # Error al pegar
    
    def seleccionar_todo(self):
        """Selecciona todo el texto."""
        try:
            self.area_texto.tag_add(tk.SEL, "1.0", tk.END)
            self.area_texto.mark_set(tk.INSERT, "1.0")
            self.area_texto.see(tk.INSERT)
            return 'break'  # Prevenir el comportamiento por defecto
        except tk.TclError:
            pass  # Error al seleccionar
    
    def acerca_de(self):
        """Muestra información sobre la aplicación."""
        messagebox.showinfo(
            "Acerca de Editor de Notas",
            "Editor de Notas v1.0\n\n"
            "Una aplicación de bloc de notas simplificada\n"
            "desarrollada con Python y Tkinter.\n\n"
            "Funcionalidades:\n"
            "• Crear, abrir y guardar archivos de texto\n"
            "• Edición básica con deshacer/rehacer\n"
            "• Interfaz gráfica intuitiva\n"
            "• Manejo de errores robusto\n\n"
            "Desarrollado como proyecto educativo."
        )


def main():
    """Función principal que inicia la aplicación."""
    try:
        # Crear y ejecutar la aplicación
        app = EditorNotas()
        app.mainloop()
    except Exception as e:
        # Manejo de errores críticos
        print(f"Error crítico al iniciar la aplicación: {e}")
        messagebox.showerror(
            "Error Crítico",
            f"No se pudo iniciar la aplicación:\n{str(e)}"
        )


if __name__ == "__main__":
    main()
