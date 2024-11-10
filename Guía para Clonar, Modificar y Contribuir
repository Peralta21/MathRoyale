# Guía para Clonar, Modificar y Contribuir al Proyecto en GitHub

## 1. Clonar un Repositorio de GitHub

### Paso 1: Encuentra el repositorio que deseas clonar
- Dirígete a la página del proyecto en GitHub. Un ejemplo de la URL de un repositorio podría ser `https://github.com/usuario/repositorio`.
- Asegúrate de que el repositorio esté público o que tengas acceso a él si es privado.

### Paso 2: Copia la URL del repositorio
- En la página del repositorio en GitHub, haz clic en el botón verde **"Code"**.
- En el cuadro que aparece, copia la URL del repositorio. Si estás usando HTTPS, la URL se verá algo así: `https://github.com/usuario/repositorio.git`.

### Paso 3: Clona el repositorio
- Abre tu terminal o consola de comandos.
- Navega hasta el directorio donde deseas clonar el repositorio, usando el comando `cd`.
- Luego, ejecuta el siguiente comando:

    ```bash
    git clone https://github.com/usuario/repositorio.git
    ```

    Esto descargará el repositorio a tu máquina local en una carpeta con el mismo nombre que el repositorio.

## 2. Modificar el Proyecto Localmente

Una vez que hayas clonado el repositorio, puedes empezar a modificarlo en tu máquina local.

### Paso 1: Navega al directorio del proyecto
Después de clonar el repositorio, navega hasta el directorio del proyecto en tu terminal:

```bash
cd repositorio
```

### Paso 2: Crea una rama nueva para tus cambios
Antes de empezar a modificar el código, es recomendable crear una rama nueva. Esto te permitirá trabajar en una copia aislada del proyecto y mantener el código principal (en la rama `main` o `master`) sin cambios hasta que estés listo.

Ejecuta el siguiente comando para crear y cambiarte a una nueva rama:

```bash
git checkout -b nombre-de-tu-rama
```

Puedes llamar a la rama de acuerdo con el tipo de cambios que vas a realizar, por ejemplo: `nueva-funcionalidad`, `correccion-de-bugs`, etc.

### Paso 3: Realiza tus cambios
Ahora puedes empezar a modificar el código como desees usando tu editor de código favorito (por ejemplo, [Visual Studio Code](https://code.visualstudio.com/), [PyCharm](https://www.jetbrains.com/pycharm/), etc.).

### Paso 4: Revisa los cambios antes de hacer commit
Para ver qué archivos han sido modificados, puedes usar:

```bash
git status
```

Esto te mostrará los archivos que han sido cambiados y los que están listos para ser confirmados (committed).

### Paso 5: Añadir los cambios
Antes de hacer un commit, necesitas añadir los archivos modificados. Si quieres añadir todos los cambios, usa:

```bash
git add .
```

Si prefieres añadir archivos específicos, usa:

```bash
git add archivo1.py archivo2.py
```

### Paso 6: Hacer commit de tus cambios
Haz commit de tus cambios con un mensaje descriptivo para explicar lo que has hecho:

```bash
git commit -m "Descripción de los cambios realizados"
```

## 3. Subir los Cambios a GitHub

Una vez que hayas realizado tus cambios localmente y estés listo para compartirlos, debes subirlos (push) a tu repositorio en GitHub.

### Paso 1: Subir tus cambios
Para subir tus cambios a GitHub, primero asegúrate de estar en la rama correcta. Luego, ejecuta el siguiente comando para hacer push:

```bash
git push origin nombre-de-tu-rama
```

Este comando sube tus cambios a la rama que especificaste en tu repositorio de GitHub.

## 4. Contribuir al Proyecto en GitHub

Si el repositorio es de un proyecto público y deseas que tus cambios sean aceptados, necesitarás hacer un **pull request**.

### Paso 1: Crear un pull request (PR)
- Después de hacer push de tus cambios a GitHub, ve a la página del repositorio en GitHub.
- Verás un mensaje que dice algo como **"Compare & pull request"** en la parte superior de la página. Haz clic en ese botón.
- En la página de creación del PR, agrega una descripción detallada de los cambios que has realizado.
- Selecciona la rama a la que deseas hacer el pull request. Por lo general, esto será a la rama `main` o `master` del repositorio original.
- Haz clic en **Create pull request** para enviar tus cambios.

### Paso 2: Revisión y comentarios
- El mantenedor del proyecto revisará tu pull request. Puede dejar comentarios o sugerencias, y es posible que te pida hacer algunos cambios antes de aceptarlo.
- Si es necesario hacer más cambios, realiza las modificaciones en tu rama local, haz commit y push de nuevo. GitHub actualizará automáticamente el pull request con los nuevos cambios.

### Paso 3: Aceptación del pull request
- Si todo está bien, el mantenedor aceptará tu pull request, y tus cambios se fusionarán (merge) en el repositorio principal.

## 5. Mantener tu Fork Actualizado (si contribuyes a un fork)

Si estás contribuyendo a un repositorio que has "forkeado" (copiado) en tu cuenta, necesitarás mantener tu fork actualizado con los cambios del repositorio original.

### Paso 1: Añadir el repositorio original como un remoto
Primero, añade el repositorio original como un remoto para poder obtener los cambios:

```bash
git remote add upstream https://github.com/usuario/repositorio-original.git
```

### Paso 2: Obtener los cambios del repositorio original
Luego, actualiza tu fork con los cambios más recientes:

```bash
git fetch upstream
```

### Paso 3: Fusionar los cambios del repositorio original
Finalmente, fusiona los cambios en tu rama `main`:

```bash
git checkout main
git merge upstream/main
```

Si hay conflictos, Git te indicará qué archivos necesitan resolución. Resuelve los conflictos, haz commit y luego sube los cambios a tu repositorio.

## Resumen de los Comandos Clave:

1. **Clonar un repositorio**:
   ```bash
   git clone https://github.com/usuario/repositorio.git
   ```

2. **Crear y cambiar a una nueva rama**:
   ```bash
   git checkout -b nombre-de-tu-rama
   ```

3. **Añadir archivos**:
   ```bash
   git add .
   ```

4. **Hacer commit de los cambios**:
   ```bash
   git commit -m "Descripción de los cambios"
   ```

5. **Subir los cambios a GitHub**:
   ```bash
   git push origin nombre-de-tu-rama
   ```

6. **Actualizar tu fork con el repositorio original**:
   ```bash
   git remote add upstream https://github.com/usuario/repositorio-original.git
   git fetch upstream
   git checkout main
   git merge upstream/main
   ```
