# Proyectos del Curso "Cursor con Python: Desarrollo Inteligente con IA"

Bienvenido/a a este repositorio, que recopila los proyectos desarrollados durante el curso **"Cursor con Python: Desarrollo Inteligente con IA"** impartido por Santander Open Academy. Aquí encontrarás ejemplos prácticos que demuestran cómo Python, junto con la asistencia de inteligencia artificial de Cursor, puede emplearse para resolver una amplia variedad de retos de programación.

---

## 🚀 Proyectos Incluidos

Cada carpeta corresponde a un proyecto independiente, enfocado en diferentes áreas y herramientas del ecosistema Python:

- **analisis_ventas**  
  Análisis de datos de ventas a partir de un archivo CSV. Calcula métricas clave (ventas mensuales, productos más vendidos/rentables) y genera visualizaciones con `pandas` y `matplotlib`.

- **bloc_de_notas**  
  Aplicación de escritorio con interfaz gráfica (Tkinter) para escribir, abrir y guardar notas en archivos de texto.

- **calculadora_simple**  
  Calculadora de consola interactiva que permite realizar operaciones básicas (suma, resta, multiplicación, división) de forma repetitiva.

- **contador_palabras**  
  Script sencillo para contar palabras en un texto, ideal para practicar manipulación de cadenas y archivos.

- **days-learning**  
  Aplicación gráfica para aprender los días de la semana en varios idiomas (inglés, español, japonés: Romaji, Hiragana y Kanji).

- **fizzbuzz**  
  Implementación clásica del problema FizzBuzz, útil para practicar bucles y condicionales.

- **gestor_tareas**  
  Aplicación web para gestionar tareas pendientes (to-do list) desarrollada con Flask. Permite añadir, listar y marcar tareas como completadas.

- **mini_data_analyst**  
  Proyecto de análisis de datos que realiza estadísticas básicas y genera visualizaciones a partir de archivos CSV.

- **organizador_de_archivos**  
  Script de automatización que organiza archivos en carpetas según su extensión, utilizando `pathlib`.

---

## 🛠️ Tecnologías y Herramientas Utilizadas

- **Python 3.8+**  
  Lenguaje principal de todos los proyectos.

- **Cursor**  
  Editor de código potenciado por IA, fundamental en el desarrollo y aprendizaje durante el curso.

- **Principales librerías y frameworks:**
  - `Flask` (gestor_tareas)
  - `pandas`, `matplotlib` (analisis_ventas, mini_data_analyst)
  - `Tkinter` (bloc_de_notas)
  - Módulos estándar: `os`, `pathlib`, `json`, entre otros.

---

## ⚡ Cómo Ejecutar los Proyectos

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/dejatori/Cursor-con-Python-desarrollo-inteligente-con-IA.git
   cd Cursor-con-Python-desarrollo-inteligente-con-IA
   ```

2. **Navega a la carpeta del proyecto:**
   ```bash
   cd nombre_del_proyecto_a_ejecutar
   ```

3. **Crea y activa un entorno virtual (recomendado):**
   ```bash
   python -m venv venv
   # En Windows:
   .\venv\Scripts\activate
   # En macOS/Linux:
   source venv/bin/activate
   ```

4. **Instala las dependencias (si existen):**
   ```bash
   pip install -r requirements.txt
   ```
   > Si no hay un `requirements.txt`, puedes omitir este paso.

5. **Ejecuta el script principal:**
   ```bash
   python tu_script_principal.py
   ```
   Ejemplos:
   - `python app.py` (Flask)
   - `python analisis.py` (análisis de datos)
   - `python bloc_de_notas.py` (notas)

---

## 🎓 Aprendizajes Clave del Curso

Este curso me permitió:

- Consolidar habilidades en Python y buenas prácticas de desarrollo.
- Aprender a programar de forma conversacional y asistida por IA.
- Generar código rápidamente con sugerencias inteligentes.
- Recibir explicaciones y refactorizaciones contextuales.
- Mejorar la productividad y la calidad del código con herramientas modernas.

La experiencia con Cursor demostró cómo la IA puede ser un aliado invaluable para acelerar el aprendizaje y el desarrollo de software.

---

## 📄 Licencia

Este repositorio está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.