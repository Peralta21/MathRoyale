import tkinter as tk
from tkinter import messagebox
import random
import time
import winsound

# Rutas de los sonidos
CORRECT_SOUND = "correct.wav"
INCORRECT_SOUND = "incorrect.wav"

class JuegoMatematicas:
    def __init__(self, root, nombre, operacion):
        self.root = root
        self.nombre = nombre
        self.operacion = operacion
        self.nivel = 1
        self.puntos = 0
        self.operaciones_realizadas = set()

        self.matriz_tamaño = 3
        self.matriz_ancho = 11
        self.tiempo_inicial = time.time()  # Tiempo de inicio
        self.actualizar_tiempo_id = None  # ID para el temporizador

        self.crear_widgets()
        self.iniciar_juego()

    def crear_widgets(self):
        self.matriz_frame = tk.Frame(self.root)
        self.matriz_frame.pack(pady=20)

        # Encabezados de la matriz
        self.labels_encabezados = [tk.Label(self.matriz_frame, text="", width=5, font=('Arial', 14, 'bold'), bg='blue', fg='white', borderwidth=2, relief='solid') for _ in range(self.matriz_ancho)]
        self.labels_encabezados[0].config(text="x")
        for i in range(1, self.matriz_ancho):
            self.labels_encabezados[i].config(text=str(i))
        for j, label in enumerate(self.labels_encabezados):
            label.grid(row=0, column=j)

        self.labels_matriz = [[tk.Label(self.matriz_frame, text="", width=5, font=('Arial', 14, 'bold'), bg='white', fg='black', borderwidth=2, relief='solid') for _ in range(self.matriz_ancho)] for _ in range(self.matriz_tamaño)]

        for i in range(self.matriz_tamaño):
            for j in range(self.matriz_ancho):
                self.labels_matriz[i][j].grid(row=i + 1, column=j)  # Colocar en la matriz

        self.reset_matriz()  # Inicializar la matriz

        self.operacion_label = tk.Label(self.root, text="", font=('Arial', 16))
        self.operacion_label.pack(pady=10)

        self.entrada = tk.Entry(self.root, font=('Arial', 14))
        self.entrada.pack(pady=10)
        self.entrada.bind('<Return>', self.verificar_respuesta)

        self.marcador_label = tk.Label(self.root, text=f"Puntos: {self.puntos}", font=('Arial', 14))
        self.marcador_label.pack(pady=10)

        self.nivel_label = tk.Label(self.root, text=f"Nivel: {self.nivel}", font=('Arial', 14))
        self.nivel_label.pack(pady=10)

        self.tiempo_label = tk.Label(self.root, text="Tiempo: 0 s", font=('Arial', 14))
        self.tiempo_label.pack(pady=10)

        self.boton_reiniciar = self.crear_boton("Reiniciar Juego", self.reiniciar_juego)
        self.boton_reiniciar.pack(pady=5)

        self.boton_salir = self.crear_boton("Salir", self.salir)
        self.boton_salir.pack(pady=5)

        self.actualizar_tiempo()  # Comenzar la actualización del tiempo

    def crear_boton(self, texto, comando):
        canvas = tk.Canvas(self.root, width=200, height=40, bg='blue', highlightthickness=0)
        canvas.pack(pady=5)
        self.create_rounded_rectangle(canvas, 0, 0, 200, 40, radius=20, fill='blue')
        btn = tk.Button(canvas, text=texto, command=comando, font=('Arial', 14, 'bold'), bg='blue', fg='white', borderwidth=0)
        btn.place(relx=0.5, rely=0.5, anchor='center')
        return btn

    def create_rounded_rectangle(self, canvas, x1, y1, x2, y2, radius, **kwargs):
        points = [
            x1 + radius, y1,
            x2 - radius, y1,
            x2, y1 + radius,
            x2, y2 - radius,
            x2 - radius, y2,
            x1 + radius, y2,
            x1, y2 - radius,
            x1, y1 + radius
        ]
        return canvas.create_polygon(points, **kwargs, smooth=True)

    def iniciar_juego(self):
        self.generar_operacion()

    def generar_operacion(self):
        while True:
            if self.nivel == 1:
                self.num1 = random.randint(1, 3)
                self.num2 = random.randint(1, 10)
            elif self.nivel == 2:
                self.num1 = random.randint(4, 6)
                self.num2 = random.randint(1, 10)
            else:
                self.num1 = random.randint(7, 9)
                self.num2 = random.randint(1, 10)

            if self.operacion == "multiplicacion":
                self.resultado = self.num1 * self.num2
                self.operacion_label.config(text=f"{self.num1} * ? = {self.resultado}")
                self.respuesta_correcta = self.num2
            else:  # División
                self.resultado = self.num1 * self.num2
                self.operacion_label.config(text=f"{self.resultado} / ? = {self.num1}")
                self.respuesta_correcta = self.num2

            if (self.num1, self.num2) not in self.operaciones_realizadas:
                self.operaciones_realizadas.add((self.num1, self.num2))
                break

    def verificar_respuesta(self, event):
        try:
            respuesta_usuario = int(self.entrada.get())
            if respuesta_usuario == self.respuesta_correcta:
                self.puntos += 1
                self.marcador_label.config(text=f"Puntos: {self.puntos}")
                self.reproducir_sonido(CORRECT_SOUND)

                # Colocar el resultado en la posición correcta
                fila = self.num1 - 1 if self.nivel == 1 else (self.num1 - 4 if self.nivel == 2 else self.num1 - 7)
                columna = self.num2

                # Verificar si fila y columna están dentro de los límites de la matriz
                if 0 <= fila < self.matriz_tamaño and 0 <= columna < self.matriz_ancho:
                    self.labels_matriz[fila][columna].config(text=f"{self.respuesta_correcta}")

                self.entrada.delete(0, tk.END)

                if len(self.operaciones_realizadas) == self.matriz_tamaño * (self.matriz_ancho - 1):
                    self.subir_nivel()

                self.generar_operacion()
            else:
                self.reproducir_sonido(INCORRECT_SOUND)
                messagebox.showerror("Error", "Respuesta incorrecta. Intenta de nuevo.")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa un número válido.")

    def reproducir_sonido(self, sonido):
        winsound.PlaySound(sonido, winsound.SND_ASYNC)

    def subir_nivel(self):
        self.nivel += 1
        self.operaciones_realizadas.clear()  
        if self.nivel > 3:
            tiempo_total = int(time.time() - self.tiempo_inicial)
            self.mostrar_resumen(tiempo_total)  # Muestra el resumen al finalizar
            return
        else:
            self.nivel_label.config(text=f"Nivel: {self.nivel}")
            messagebox.showinfo("Felicidades", f"¡Felicidades, has completado el Nivel {self.nivel - 1}!")
            self.reset_matriz()

    def reset_matriz(self):
        for i in range(self.matriz_tamaño):
            for j in range(self.matriz_ancho):
                self.labels_matriz[i][j].config(text="", bg='white', fg='black')
        
        # Actualizar los números de las filas
        for i in range(self.matriz_tamaño):
            fila_num = (self.nivel - 1) * 3 + (i + 1)
            self.labels_matriz[i][0].config(text=str(fila_num), bg='blue', fg='white')

    def actualizar_tiempo(self):
        tiempo_total = int(time.time() - self.tiempo_inicial)
        self.tiempo_label.config(text=f"Tiempo: {tiempo_total} s")
        self.actualizar_tiempo_id = self.root.after(1000, self.actualizar_tiempo)  # Guardar el ID

    def mostrar_resumen(self, tiempo_total):
        resumen = f"Nombre del jugador: {self.nombre}\nPuntos totales: {self.puntos}\nTiempo jugado: {tiempo_total} segundos."
        messagebox.showinfo("Resumen del Juego", resumen)
        self.root.destroy()  # Cerrar la ventana del juego
        self.volver_al_menu()

    def volver_al_menu(self):
        main()  # Volver a la pantalla de inicio

    def reiniciar_juego(self):
        self.nivel = 1
        self.puntos = 0
        self.operaciones_realizadas.clear()
        self.reset_matriz()
        self.marcador_label.config(text=f"Puntos: {self.puntos}")
        self.nivel_label.config(text=f"Nivel: {self.nivel}")
        self.tiempo_inicial = time.time()  # Reiniciar el tiempo
        self.generar_operacion()

    def salir(self):
        self.root.after_cancel(self.actualizar_tiempo_id)  # Detener la actualización del tiempo
        tiempo_total = int(time.time() - self.tiempo_inicial)
        resumen = f"Nombre del jugador: {self.nombre}\nPuntos totales: {self.puntos}\nTiempo jugado: {tiempo_total} segundos."
        messagebox.showinfo("Resumen del Juego", resumen)
        self.root.quit()

def main():
    root = tk.Tk()
    root.title("Juego de Matemáticas")

    def iniciar_juego(operacion):
        nombre = nombre_entry.get()
        if nombre:  # Asegúrate de que el nombre no esté vacío
            juego = JuegoMatematicas(root, nombre, operacion)
            menu_frame.pack_forget()  # Ocultar el menú
            juego.root.deiconify()  # Mostrar el juego

    # Ventana de inicio
    menu_frame = tk.Frame(root)
    menu_frame.pack(pady=20)

    tk.Label(menu_frame, text="Ingresa tu nombre:", font=('Arial', 16)).pack(pady=10)
    nombre_entry = tk.Entry(menu_frame, font=('Arial', 14))
    nombre_entry.pack(pady=10)

    tk.Button(menu_frame, text="Multiplicaciones", command=lambda: iniciar_juego("multiplicacion")).pack(pady=5)
    tk.Button(menu_frame, text="Divisiones", command=lambda: iniciar_juego("division")).pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
