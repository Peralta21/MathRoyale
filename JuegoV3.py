import tkinter as tk
from tkinter import messagebox
import random
import time
import winsound

# Rutas de los sonidos
CORRECT_SOUND = "correct.wav"
INCORRECT_SOUND = "incorrect.wav"

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
        operador_label = tk.Label(self.matriz_frame, text=operador, width=5, font=('Arial', 14, 'bold'), bg='lightgray')
        operador_label.grid(row=0, column=0)

        # Encabezados superiores (números 1, 2, ..., matriz_tamaño)
        for j in range(self.matriz_tamaño):
            encabezado = tk.Label(self.matriz_frame, text=str(j + 1), width=5, font=('Arial', 14, 'bold'), bg='lightgray')
            encabezado.grid(row=0, column=j + 1)  # Desplazado a la derecha

        # Encabezados laterales y creación de celdas de la matriz
        self.labels_matriz = []
        for i in range(self.matriz_tamaño):
            encabezado = tk.Label(self.matriz_frame, text=str(i + 1), width=5, font=('Arial', 14, 'bold'), bg='lightgray')
            encabezado.grid(row=i + 1, column=0)  # Desplazado hacia abajo

            fila = []
            for j in range(self.matriz_tamaño):
                celda = tk.Label(self.matriz_frame, text="", width=5, font=('Arial', 14), bg='white', fg='black', borderwidth=2, relief='solid')
                celda.grid(row=i + 1, column=j + 1)
                fila.append(celda)
            self.labels_matriz.append(fila)

        # Etiquetas y entrada
        self.operacion_label = tk.Label(self.root, text="", font=('Arial', 16))
        self.operacion_label.pack(pady=10)
        
        self.entrada = tk.Entry(self.root, font=('Arial', 14))
        self.entrada.pack(pady=10)
        self.entrada.bind('<Return>', self.verificar_respuesta)

        self.marcador_label = tk.Label(self.root, text=f"Puntos: {self.puntos}", font=('Arial', 14))
        self.marcador_label.pack(pady=10)

        self.tiempo_label = tk.Label(self.root, text="Tiempo: 0 s", font=('Arial', 14))
        self.tiempo_label.pack(pady=10)

        # Botones
        self.boton_reiniciar = tk.Button(self.root, text="Reiniciar Juego", command=self.reiniciar_juego, font=('Arial', 14), bg='blue', fg='white')
        self.boton_reiniciar.pack(pady=5)
        
        self.boton_salir = tk.Button(self.root, text="Salir", command=self.salir, font=('Arial', 14), bg='red', fg='white')
        self.boton_salir.pack(pady=5)

        self.actualizar_tiempo()

    def iniciar_juego(self):
        self.generar_matriz_operaciones()

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
                self.puntos += 1
                self.marcador_label.config(text=f"Puntos: {self.puntos}")
                
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
                messagebox.showerror("Error", "Respuesta incorrecta.")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa un número válido.")

    def actualizar_tiempo(self):
        tiempo_total = int(time.time() - self.tiempo_inicial)
        self.tiempo_label.config(text=f"Tiempo: {tiempo_total} s")
        self.root.after(1000, self.actualizar_tiempo)

    def reiniciar_juego(self):
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


def main():
    root = tk.Tk()
    root.title("Juego de Matemáticas")

    def seleccionar_operacion():
        nombre = nombre_entry.get()
        if nombre:
            nombre_frame.pack_forget()
            operacion_frame.pack()

    def seleccionar_nivel(operacion):
        operacion_frame.pack_forget()
        nivel_frame.pack()
        for nivel in range(1, 4):
            tk.Button(nivel_frame, text=f"Nivel {nivel}", font=('Arial', 14), command=lambda n=nivel: iniciar_juego(nombre_entry.get(), operacion, n)).pack(pady=5)

    def iniciar_juego(nombre, operacion, nivel):
        nivel_frame.pack_forget()
        JuegoMatematicas(root, nombre, operacion, nivel)

    # Pantalla de nombre
    nombre_frame = tk.Frame(root)
    nombre_frame.pack(pady=20)
    tk.Label(nombre_frame, text="Ingresa tu nombre:", font=('Arial', 16)).pack(pady=10)
    nombre_entry = tk.Entry(nombre_frame, font=('Arial', 14))
    nombre_entry.pack(pady=10)
    tk.Button(nombre_frame, text="Siguiente", command=seleccionar_operacion, font=('Arial', 14)).pack(pady=10)

    # Pantalla de operación
    operacion_frame = tk.Frame(root)
    tk.Label(operacion_frame, text="Selecciona una operación:", font=('Arial', 16)).pack(pady=10)
    tk.Button(operacion_frame, text="Multiplicación", command=lambda: seleccionar_nivel("multiplicacion"), font=('Arial', 14)).pack(pady=5)
    tk.Button(operacion_frame, text="División", command=lambda: seleccionar_nivel("division"), font=('Arial', 14)).pack(pady=5)

    # Pantalla de nivel
    nivel_frame = tk.Frame(root)

    root.mainloop()

if __name__ == "__main__":
    main()
