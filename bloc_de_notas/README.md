# Editor de Notas - Aplicación de Bloc de Notas

Una aplicación de escritorio desarrollada en Python usando Tkinter que funciona como un bloc de notas simplificado con interfaz gráfica.

## Características

### Funcionalidades Principales

- **Crear nuevos archivos** de texto
- **Abrir archivos** existentes (.txt y otros formatos)
- **Guardar archivos** con nombre personalizado
- **Guardar como** para crear copias con diferente nombre
- **Interfaz gráfica intuitiva** con menús y atajos de teclado

### Funcionalidades de Edición

- **Deshacer/Rehacer** acciones (Ctrl+Z / Ctrl+Y)
- **Cortar, Copiar y Pegar** (Ctrl+X, Ctrl+C, Ctrl+V)
- **Seleccionar todo** el contenido (Ctrl+A)
- **Detección automática** de cambios no guardados
- **Área de texto con scrollbars** integrados

### Características Técnicas

- **Programación orientada a objetos** con clase `EditorNotas`
- **Manejo robusto de errores** con bloques try-except
- **Detección automática de codificación** de archivos (UTF-8, Latin-1, CP1252)
- **Interfaz responsive** con tamaño mínimo configurado
- **Atajos de teclado** para todas las funciones principales

## Requisitos

- Python 3.10 o superior
- Tkinter (incluido en la instalación estándar de Python)
- No se requieren librerías externas

## Instalación y Uso

### 1. Clonar o descargar el proyecto

```bash
git clone <url-del-repositorio>
cd bloc_de_notas
```

### 2. Activar el entorno virtual (recomendado)

```bash
# En Windows
venv\Scripts\activate

# En macOS/Linux
source venv/bin/activate
```

### 3. Ejecutar la aplicación

```bash
python notas.py
```

## Atajos de Teclado

| Función          | Atajo        |
| ---------------- | ------------ |
| Nuevo archivo    | Ctrl+N       |
| Abrir archivo    | Ctrl+O       |
| Guardar          | Ctrl+S       |
| Guardar como     | Ctrl+Shift+S |
| Salir            | Ctrl+Q       |
| Deshacer         | Ctrl+Z       |
| Rehacer          | Ctrl+Y       |
| Cortar           | Ctrl+X       |
| Copiar           | Ctrl+C       |
| Pegar            | Ctrl+V       |
| Seleccionar todo | Ctrl+A       |

## Estructura del Código

### Clase Principal: `EditorNotas`

- **Hereda de `tk.Tk`** para crear la ventana principal
- **Métodos organizados** por funcionalidad:
  - Configuración: `configurar_area_texto()`, `configurar_menu()`, `configurar_eventos()`
  - Gestión de archivos: `abrir_archivo()`, `guardar_archivo()`, `cargar_archivo()`
  - Edición: `deshacer()`, `copiar()`, `pegar()`, etc.
  - Utilidades: `actualizar_titulo()`, `verificar_cambios_no_guardados()`

### Características de Diseño

- **Separación de responsabilidades** en métodos específicos
- **Manejo de estado** con variables de instancia
- **Interfaz modular** con menús organizados
- **Gestión de eventos** centralizada

## Funcionalidades Detalladas

### Gestión de Archivos

- **Detección automática de codificación**: La aplicación intenta leer archivos con diferentes codificaciones (UTF-8, Latin-1, CP1252)
- **Protección contra archivos binarios**: Muestra error si no puede leer el archivo como texto
- **Verificación de cambios**: Pregunta antes de cerrar si hay cambios no guardados
- **Título dinámico**: Muestra el nombre del archivo y un asterisco (\*) si hay cambios

### Interfaz de Usuario

- **Tamaño inicial**: 600x400 píxeles
- **Tamaño mínimo**: 400x300 píxeles
- **Fuente monoespaciada**: Consolas para mejor legibilidad
- **Colores personalizados**: Fondo blanco, texto negro, selección azul claro
- **Scrollbars automáticos**: Se muestran cuando es necesario

### Manejo de Errores

- **Errores de archivo**: Muestra mensajes informativos si no se puede abrir/guardar
- **Errores de codificación**: Intenta múltiples codificaciones automáticamente
- **Errores críticos**: Manejo de excepciones en la función principal
- **Validación de entrada**: Verifica que se seleccione un archivo antes de procesar

## Limitaciones

- Solo maneja archivos de texto (no imágenes, documentos de Word, etc.)
- No incluye funciones avanzadas como búsqueda/reemplazo
- No tiene soporte para múltiples pestañas
- No incluye funciones de formato de texto (negrita, cursiva, etc.)

## Posibles Mejoras Futuras

- Búsqueda y reemplazo de texto
- Soporte para múltiples pestañas
- Formato de texto (negrita, cursiva, etc.)
- Numeración de líneas
- Temas de color personalizables
- Integración con control de versiones
- Autoguardado automático

## Licencia

Este proyecto es de código abierto y está disponible para uso educativo y personal.

## Autor

Desarrollado como proyecto educativo para demostrar el uso de Tkinter y programación orientada a objetos en Python.
