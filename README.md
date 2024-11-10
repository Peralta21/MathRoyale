# MathRoyale

**MathRoyale** es un juego interactivo de matemáticas desarrollado con Python utilizando la biblioteca gráfica `Tkinter` y `Pillow` para la manipulación de imágenes. El objetivo del juego es mejorar las habilidades matemáticas de estudiantes de  primaria y secundaria a través de la resolución de operaciones matemáticas en una matriz.

En este juego, los jugadores pueden elegir entre dos tipos de operaciones: **Multiplicación** y **División**. Además, pueden seleccionar el nivel de dificultad (Nivel 1, 2, o 3), que afecta el tamaño de la matriz y la complejidad de las operaciones. El jugador debe responder correctamente a las operaciones de la matriz para obtener puntos. Si responde correctamente en el primer intento, obtiene más puntos; si responde en el segundo o tercer intento, obtendrá menos puntos.

## Funcionalidad

- **Operaciones**: El juego permite elegir entre multiplicación y división.
- **Modos de Juego**: El jugador puede elegir entre tres niveles de dificultad, donde el tamaño de la matriz aumenta con el nivel.
- **Sistema de Puntuación**: La puntuación se acumula en función de cuántos intentos le toma al jugador responder correctamente a cada operación.
  - 1er intento: 100 puntos
  - 2do intento: 50 puntos
  - 3er o más intentos: 25 puntos
- **Interfaz Gráfica**: Usa la biblioteca `Tkinter` para crear la interfaz gráfica, con botones, entradas de texto y una matriz de operaciones.
- **Sonidos**: El juego incluye efectos de sonido para las respuestas correctas.

## Requisitos

Para ejecutar el proyecto, necesitarás tener instalado Python y las siguientes bibliotecas:

- **Python 3.x**: Asegúrate de tener Python 3.x instalado. Puedes descargarlo desde [python.org](https://www.python.org/downloads/).
- **Tkinter**: Esta es una biblioteca estándar de Python para interfaces gráficas, pero algunos sistemas operativos pueden requerir que se instale por separado.
- **Pillow**: Esta es una biblioteca de Python para el procesamiento de imágenes. Puedes instalarla utilizando `pip`.

### Instalación de dependencias

1. **Instalar Python 3.9**:
   Si aún no tienes Python instalado, descarga e instala la última versión de [Python 3.9](https://www.python.org/downloads/) como versión minima.

2. **Instalar las dependencias**:
   En tu terminal o consola de comandos, instala la biblioteca `Pillow` (si no está instalada):

   ```bash
   pip install pillow
   ```

   **Tkinter** generalmente viene preinstalado con Python, pero si no lo tienes, puedes instalarlo de la siguiente manera:

   - En **Windows**: Tkinter debería estar incluido automáticamente con Python.
   - En **macOS**: Tkinter también debería venir con Python. Si no es así, puedes instalarlo a través de Homebrew.
   - En **Linux (Ubuntu/Debian)**: Instala Tkinter usando el siguiente comando:

     ```bash
     sudo apt-get install python3-tk
     ```

3. **Sonidos**:
   Asegúrate de tener un archivo de sonido llamado `correct.wav` en el mismo directorio del script para las respuestas correctas. Si no lo tienes, puedes descargar cualquier archivo de sonido en formato `.wav` y cambiar el nombre a `correct.wav`.

---

## Cómo Ejecutar el Juego

1. **Clona o descarga el repositorio**:
   Si tienes Git instalado, puedes clonar el repositorio usando el siguiente comando:

   ```bash
   git clone https://github.com/usuario/repositorio.git
   ```

   O bien, puedes descargar el archivo ZIP desde la página de GitHub y extraerlo en una carpeta de tu elección.

2. **Ejecutar el juego**:
   Entra al directorio donde se encuentra el archivo `JuegoMatematicas.py` y ejecuta el script con el siguiente comando en tu terminal o consola:

   ```bash
   python JuegoMatematicas.py
   ```

   Esto abrirá la ventana del juego.

---

## Cómo Jugar

1. **Pantalla de bienvenida**: 
   Cuando se inicie el juego, se mostrará una pantalla de bienvenida en la que se te pedirá ingresar tu nombre.

2. **Seleccionar operación**: 
   Luego de ingresar tu nombre, podrás elegir entre dos tipos de operaciones matemáticas:
   - **Multiplicación**
   - **División**

3. **Seleccionar nivel**:
   Después de elegir la operación, podrás seleccionar el nivel de dificultad:
   - **Nivel 1**: Matriz de tamaño 6x6.
   - **Nivel 2**: Matriz de tamaño 9x9.
   - **Nivel 3**: Matriz de tamaño 12x12.

4. **Juego de matriz**: 
   El objetivo es responder correctamente a las operaciones de la matriz. Los valores se colocan en las celdas de la matriz, y debes ingresar la respuesta correcta a cada operación.
   - Si la respuesta es correcta en el primer intento, obtendrás 100 puntos.
   - Si la respuesta es correcta en el segundo intento, obtendrás 50 puntos.
   - Si la respuesta es correcta en el tercer o más intentos, obtendrás 25 puntos.

5. **Puntuación y tiempo**: 
   Durante el juego, se mostrará la cantidad de puntos y el tiempo transcurrido. El jugador podrá reiniciar el juego o salir en cualquier momento.

6. **Final del juego**:
   Una vez que completes todas las operaciones de la matriz o el jugador decide salir, se mostrará un resumen con la puntuación total y el tiempo de juego.

---

## Funcionalidades Adicionales

- **Reiniciar el Juego**: Al presionar el botón "Reiniciar Juego", el puntaje y las operaciones previas se reinician, y el juego comienza de nuevo.
- **Volver al Menú Principal**: El jugador puede regresar al menú principal para elegir una operación y nivel diferentes.
- **Salir del Juego**: El jugador puede salir en cualquier momento, lo que mostrará un resumen de la puntuación obtenida.

---

## Estructura del Proyecto

La estructura de archivos del proyecto es la siguiente:

```
MathRoyale/
│
├── JuegoMatematicas.py    # El script principal del juego
├── correct.wav            # Archivo de sonido para las respuestas correctas
├── Math-Background.jpg    # Imagen de fondo para la interfaz gráfica
└── README.md              # Este archivo
```

---

## Contribuciones

Si deseas contribuir a este proyecto, sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una rama nueva para tus cambios (`git checkout -b nueva-funcionalidad`).
3. Realiza tus cambios y haz commit de ellos (`git commit -am 'Añadir nueva funcionalidad'`).
4. Sube tus cambios (`git push origin nueva-funcionalidad`).
5. Abre un pull request para que los cambios sean revisados y fusionados en el repositorio principal.

---

## Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

---

## Notas

- Asegúrate de tener la biblioteca `Tkinter` y `Pillow` instaladas correctamente para ejecutar el juego sin problemas.
- Si tienes problemas con la instalación o ejecución del proyecto, revisa los problemas abiertos en el repositorio o crea un nuevo problema para que otros usuarios puedan ayudarte.

---

Esta guía proporciona instrucciones claras sobre cómo instalar, ejecutar y utilizar el juego, así como detalles sobre la funcionalidad y las características del proyecto para que otros usuarios puedan comprender cómo usar y contribuir al proyecto.
