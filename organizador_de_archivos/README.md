# 🗂️ Organizador de Archivos

Un script en Python que organiza automáticamente archivos en subcarpetas según su tipo de extensión.

## 📋 Características

- **Organización automática**: Mueve archivos a carpetas categorizadas según su extensión
- **Prevención de sobrescritura**: Genera nombres únicos para evitar conflictos
- **Interfaz amigable**: Salida clara con emojis y estadísticas detalladas
- **Seguridad**: Confirmación del usuario antes de ejecutar
- **Flexibilidad**: Permite especificar directorio personalizado o usar Downloads por defecto

## 🎯 Categorías de Archivos

El script organiza los archivos en las siguientes categorías:

| Categoría       | Extensiones Soportadas                            |
| --------------- | ------------------------------------------------- |
| **Imágenes**    | .png, .jpg, .jpeg, .gif, .bmp, .tiff, .webp       |
| **Documentos**  | .pdf, .docx, .txt, .xlsx, .doc, .xls, .ppt, .pptx |
| **Videos**      | .mp4, .avi, .mkv, .mov, .wmv, .flv, .webm         |
| **Música**      | .mp3, .wav, .flac, .aac, .ogg, .m4a               |
| **Comprimidos** | .zip, .rar, .7z, .tar, .gz                        |
| **Programas**   | .exe, .msi, .dmg, .pkg, .deb, .rpm                |
| **Otros**       | Cualquier extensión no reconocida                 |

## 🚀 Instalación y Uso

### Requisitos

- Python 3.10 o superior
- Librerías estándar de Python (no requiere instalación adicional)

### Uso Básico

1. **Ejecutar en Downloads (por defecto):**

   ```bash
   python organizar.py
   ```

2. **Ejecutar en directorio específico:**

   ```bash
   python organizar.py "C:\Users\TuUsuario\Desktop"
   ```

3. **Ejecutar en directorio actual:**
   ```bash
   python organizar.py .
   ```

### Ejemplo de Ejecución

```
🗂️  ORGANIZADOR DE ARCHIVOS
==================================================
📁 Usando directorio por defecto: C:\Users\Usuario\Downloads

⚠️  ADVERTENCIA: Este script moverá archivos en C:\Users\Usuario\Downloads
💡 Se recomienda hacer una copia de seguridad antes de continuar.

¿Desea continuar? (s/N): s

🔍 Escaneando directorio: C:\Users\Usuario\Downloads
==================================================
✓ Creado directorio: C:\Users\Usuario\Downloads\Imágenes
✓ Movido: foto_vacaciones.jpg → Imágenes/
✓ Creado directorio: C:\Users\Usuario\Downloads\Documentos
✓ Movido: informe_2024.pdf → Documentos/
✓ Movido: presentacion.pptx → Documentos/

==================================================
📊 RESUMEN DE LA ORGANIZACIÓN
==================================================
📁 Archivos procesados: 3
✅ Archivos movidos: 3

📂 Archivos movidos por categoría:
   • Imágenes: 1 archivo(s)
   • Documentos: 2 archivo(s)

🎉 ¡Organización completada! 3 archivo(s) organizado(s).
```

## 🛡️ Características de Seguridad

### Prevención de Sobrescritura

- Si existe un archivo con el mismo nombre, se agrega un sufijo numérico
- Ejemplo: `documento.pdf` → `documento_1.pdf` → `documento_2.pdf`

### Confirmación del Usuario

- El script pide confirmación antes de ejecutar
- Muestra claramente qué directorio será afectado

### Omitir el Script

- El propio archivo `organizar.py` no se mueve durante la ejecución

## 📁 Estructura del Proyecto

```
organizador_de_archivos/
├── organizar.py          # Script principal
├── README.md            # Documentación
└── venv/               # Entorno virtual (opcional)
```

## 🔧 Funcionalidades Técnicas

### Librerías Utilizadas

- **pathlib**: Operaciones de archivos y directorios
- **os**: Funciones del sistema operativo
- **shutil**: Operaciones de archivos avanzadas
- **typing**: Anotaciones de tipo para mejor código

### Arquitectura del Código

- **Clase OrganizadorArchivos**: Lógica principal encapsulada
- **Métodos modulares**: Cada función tiene una responsabilidad específica
- **Manejo de errores**: Try-catch para operaciones críticas
- **Documentación completa**: Docstrings en todos los métodos

## ⚠️ Advertencias Importantes

1. **Hacer copia de seguridad**: Siempre respalda archivos importantes antes de usar el script
2. **Probar primero**: Ejecuta en una carpeta de prueba con archivos no críticos
3. **Verificar permisos**: Asegúrate de tener permisos de escritura en el directorio objetivo
4. **Compatible con Windows**: Probado en Windows 10/11, compatible con otros sistemas

## 🐛 Solución de Problemas

### Error: "El directorio no existe"

- Verifica que la ruta especificada sea correcta
- Usa rutas absolutas si es necesario

### Error: "Permiso denegado"

- Ejecuta como administrador si es necesario
- Verifica permisos de escritura en el directorio

### Archivos no se mueven

- Verifica que los archivos no estén en uso por otras aplicaciones
- Asegúrate de que haya espacio suficiente en disco

## 📝 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Haz fork del proyecto
2. Crea una rama para tu feature
3. Commit tus cambios
4. Push a la rama
5. Abre un Pull Request

---

**Desarrollado con ❤️ usando Python y librerías estándar**
