import tkinter as tk
from tkinter import messagebox
import random
import time
from PIL import Image, ImageTk
import winsound

CORRECT_SOUND = "correct.wav"

class JuegoMatematicas:
    def __init__(self, root, nombre, operacion, nivel):
        self.root = root
        self.nombre = nombre
        self.operacion = operacion
        self.nivel = nivel
        self.puntos = 0
        self.operaciones_realizadas = set()
        self.tiempo_inicial = time.time()  # Tiempo de inicio

        # Tamaño de matriz según el nivel
        if self.nivel == 1:
            self.matriz_tamaño = 6
        elif self.nivel == 2:
            self.matriz_tamaño = 9
        else:
            self.matriz_tamaño = 12

        self.crear_widgets()
        self.iniciar_juego()

    def crear_widgets(self):
        self.matriz_frame = tk.Frame(self.root)
        self.matriz_frame.pack(pady=20)

        # Símbolo de operación en la esquina superior izquierda
        operador = "*" if self.operacion == "multiplicacion" else "/"
        operador_label = tk.Label(self.matriz_frame, text=operador, width=5, font=('Arial', 14, 'bold'), bg='orange')
        operador_label.grid(row=0, column=0)

        # Encabezados superiores (números 1, 2, ..., matriz_tamaño)
        for j in range(self.matriz_tamaño):
            encabezado = tk.Label(self.matriz_frame, text=str(j + 1), width=5, font=('Arial', 14, 'bold'), bg='orange')
            encabezado.grid(row=0, column=j + 1)  # Desplazado a la derecha

        # Encabezados laterales y creación de celdas de la matriz
        self.labels_matriz = []
        for i in range(self.matriz_tamaño):
            encabezado = tk.Label(self.matriz_frame, text=str(i + 1), width=5, font=('Arial', 14, 'bold'), bg='orange')
            encabezado.grid(row=i + 1, column=0)  # Desplazado hacia abajo

            fila = []
            for j in range(self.matriz_tamaño):
                celda = tk.Label(self.matriz_frame, text="", width=5, font=('Arial', 14), bg='white', fg='black', borderwidth=2, relief='solid')
                celda.grid(row=i + 1, column=j + 1)
                fila.append(celda)
            self.labels_matriz.append(fila)

        # Etiquetas y entrada
        self.operacion_label = tk.Label(self.root, text="", font=('Arial', 16), bg='white', relief='solid')
        self.operacion_label.pack(pady=10)
        
        self.entrada = tk.Entry(self.root, font=('Arial', 14))
        self.entrada.pack(pady=10)
        self.entrada.bind('<Return>', self.verificar_respuesta)

        self.marcador_label = tk.Label(self.root, text=f"Puntos: {self.puntos}", font=('Arial', 14))
        self.marcador_label.pack(pady=10)

        self.tiempo_label = tk.Label(self.root, text="Tiempo: 0 s", font=('Arial', 14))
        self.tiempo_label.pack(pady=10)

        # Frame para los botones en una sola fila
        botones_frame = tk.Frame(self.root)
        botones_frame.pack(pady=5)

        # Botones en el mismo nivel
        self.boton_reiniciar = tk.Button(botones_frame, text="Reiniciar Juego", command=self.reiniciar_juego, font=('Arial', 14), bg='green', fg='white')
        self.boton_reiniciar.pack(side=tk.LEFT, padx=5)
        
        self.boton_volver = tk.Button(botones_frame, text="Volver al Menú", command=self.volver_al_menu, font=('Arial', 14), bg='turquoise', fg='black')
        self.boton_volver.pack(side=tk.LEFT, padx=5)
        
        self.boton_salir = tk.Button(botones_frame, text="Salir", command=self.salir, font=('Arial', 14), bg='red', fg='white')
        self.boton_salir.pack(side=tk.LEFT, padx=5)

        self.actualizar_tiempo()

    def iniciar_juego(self):
        self.generar_matriz_operaciones()

    def volver_al_menu(self):
        # Destruir widgets del juego actual
        for widget in self.root.winfo_children():
            widget.destroy()
        # Reestablecer el fondo y regresar al menú de operaciones
        establecer_fondo(self.root)
        seleccion_operacion(self.root, self.nombre)

    def generar_matriz_operaciones(self):
        # Generar todos los valores en la matriz
        self.valores_matriz = []
        for i in range(1, self.matriz_tamaño + 1):
            fila = []
            for j in range(1, self.matriz_tamaño + 1):
                self.labels_matriz[i-1][j-1].config(text="")  # Limpiar celdas
            self.valores_matriz.append(fila)

        # Generar la primera operación al iniciar el juego
        self.generar_operacion()

    def generar_operacion(self):
        while True:
            self.num1 = random.randint(1, self.matriz_tamaño)
            self.num2 = random.randint(1, self.matriz_tamaño)

            # Configuración para multiplicación y división
            if self.operacion == "multiplicacion":
                self.resultado = self.num1 * self.num2
                self.operacion_label.config(text=f"{self.num1} * {self.num2} = ?")
                self.respuesta_correcta = self.resultado
            else:  # División
                # Asegurarse de que el primer número sea el mayor (dividendo)
                dividendo = max(self.num1, self.num2) * min(self.num1, self.num2)
                divisor = min(self.num1, self.num2)
                self.resultado = dividendo // divisor
                self.operacion_label.config(text=f"{dividendo} / {divisor} = ?")
                self.respuesta_correcta = self.resultado
                self.dividendo = dividendo  # Almacenar el dividendo para mostrar en la matriz

            # Asegurarse de que no se repita la operación
            if (self.num1, self.num2) not in self.operaciones_realizadas:
                self.operaciones_realizadas.add((self.num1, self.num2))
                break

    def verificar_respuesta(self, event):
        try:
            respuesta_usuario = int(self.entrada.get())
            if respuesta_usuario == self.respuesta_correcta:
                self.puntos += 10
                self.marcador_label.config(text=f"Puntos: {self.puntos}")
                self.reproducir_sonido(CORRECT_SOUND)
                # Mostrar el resultado o dividendo en la matriz
                if self.operacion == "multiplicacion":
                    self.labels_matriz[self.num1-1][self.num2-1].config(text=str(self.respuesta_correcta))
                else:
                    self.labels_matriz[self.num1-1][self.num2-1].config(text=str(self.dividendo))  # Mostrar el dividendo

                self.entrada.delete(0, tk.END)

                # Verificar si completó la matriz
                if len(self.operaciones_realizadas) == self.matriz_tamaño ** 2:
                    self.mostrar_resumen()
                else:
                    self.generar_operacion()
            else:
                self.puntos -= 5
                self.marcador_label.config(text=f"Puntos: {self.puntos}")
                messagebox.showerror("Error", "Respuesta incorrecta.")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa un número válido.")
    
    def reproducir_sonido(self, sonido):
        winsound.PlaySound(sonido, winsound.SND_ASYNC)

    def actualizar_tiempo(self):
        tiempo_total = int(time.time() - self.tiempo_inicial)
        self.tiempo_label.config(text=f"Tiempo: {tiempo_total} s")
        self.root.after(1000, self.actualizar_tiempo)

    def reiniciar_juego(self):
        self.puntos = 0
        self.puntos = 0
        self.operaciones_realizadas.clear()
        self.tiempo_inicial = time.time()
        self.generar_matriz_operaciones()

    def salir(self):
        tiempo_total = int(time.time() - self.tiempo_inicial)
        resumen = f"Nombre: {self.nombre}\nPuntos: {self.puntos}\nTiempo: {tiempo_total} segundos."
        messagebox.showinfo("Resumen del Juego", resumen)
        self.root.quit()

    def mostrar_resumen(self):
        tiempo_total = int(time.time() - self.tiempo_inicial)
        resumen = f"Nombre del jugador: {self.nombre}\nPuntos totales: {self.puntos}\nTiempo jugado: {tiempo_total} segundos."
        messagebox.showinfo("¡Juego Completo!", resumen)
        self.reiniciar_juego()

def establecer_fondo(root):
    # Cargar y mostrar el fondo
    bg_image = Image.open("Math-Background.jpg")  
    bg_image = bg_image.resize((1600, 850), Image.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = tk.Label(root, image=bg_photo)
    bg_label.image = bg_photo  # Necesario para evitar que la imagen sea eliminada por el recolector de basura
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

def main():
    root = tk.Tk()
    root.title("Juego de Matemáticas")
    root.geometry("1900x1200")
    root.configure(bg="white")
    
    # Establecer el fondo
    establecer_fondo(root)

    # Pantalla de bienvenida con estilo
    bienvenida_frame = tk.Frame(root, bg="white", bd=2, relief="solid")
    bienvenida_frame.place(relx=0.5, rely=0.5, anchor="center", width=650, height=300)

    bienvenida_label = tk.Label(bienvenida_frame, text="Bienvenido a MathRoyale!", font=("Arial", 24), fg="blue", bg="white")
    bienvenida_label.pack(pady=20)

    nombre_label = tk.Label(bienvenida_frame, text="Ingresa tu nombre:", font=("Arial", 14), fg="black", bg="white")
    nombre_label.pack()

    nombre_entry = tk.Entry(bienvenida_frame, font=("Arial", 14))
    nombre_entry.pack(pady=10)

    def iniciar_juego():
        nombre = nombre_entry.get()
        if nombre:
            bienvenida_frame.destroy()
            seleccion_operacion(root, nombre)
        else:
            messagebox.showerror("Error", "Por favor ingresa tu nombre.")

    boton_iniciar = tk.Button(bienvenida_frame, text="Iniciar Juego", font=("Arial", 14), command=iniciar_juego, bg="green", fg="white")
    boton_iniciar.pack(pady=20)

    root.mainloop()

def seleccion_operacion(root, nombre):
    seleccion_frame = tk.Frame(root, bg="white", bd=2, relief="solid")
    seleccion_frame.place(relx=0.5, rely=0.5, anchor="center", width=650, height=300)

    operacion_label = tk.Label(seleccion_frame, text="Selecciona la operación:", font=("Arial", 24), fg="blue", bg="white")
    operacion_label.pack(pady=20)

    def seleccion_multiplicacion():
        seleccion_frame.destroy()
        seleccion_nivel(root, nombre, "multiplicacion")

    def seleccion_division():
        seleccion_frame.destroy()
        seleccion_nivel(root, nombre, "division")

    boton_multiplicacion = tk.Button(seleccion_frame, text="Multiplicación", font=("Arial", 14), command=seleccion_multiplicacion, bg="fuchsia", fg="white")
    boton_multiplicacion.pack(pady=10)

    boton_division = tk.Button(seleccion_frame, text="División", font=("Arial", 14), command=seleccion_division, bg="fuchsia", fg="white")
    boton_division.pack(pady=10)

def seleccion_nivel(root, nombre, operacion):
    seleccion_nivel_frame = tk.Frame(root, bg="white", bd=2, relief="solid")
    seleccion_nivel_frame.place(relx=0.5, rely=0.5, anchor="center", width=650, height=300)

    nivel_label = tk.Label(seleccion_nivel_frame, text="Selecciona el nivel:", font=("Arial", 24), fg="blue", bg="white")
    nivel_label.pack(pady=20)

    def seleccion_nivel_1():
        seleccion_nivel_frame.destroy()
        JuegoMatematicas(root, nombre, operacion, 1)

    def seleccion_nivel_2():
        seleccion_nivel_frame.destroy()
        JuegoMatematicas(root, nombre, operacion, 2)

    def seleccion_nivel_3():
        seleccion_nivel_frame.destroy()
        JuegoMatematicas(root, nombre, operacion, 3)

    boton_nivel_1 = tk.Button(seleccion_nivel_frame, text="Nivel 1", font=("Arial", 14), command=seleccion_nivel_1, bg="turquoise", fg="black")
    boton_nivel_1.pack(pady=10)

    boton_nivel_2 = tk.Button(seleccion_nivel_frame, text="Nivel 2", font=("Arial", 14), command=seleccion_nivel_2, bg="turquoise", fg="black")
    boton_nivel_2.pack(pady=10)

    boton_nivel_3 = tk.Button(seleccion_nivel_frame, text="Nivel 3", font=("Arial", 14), command=seleccion_nivel_3, bg="turquoise", fg="black")
    boton_nivel_3.pack(pady=10)

if __name__ == "__main__":
    main()
