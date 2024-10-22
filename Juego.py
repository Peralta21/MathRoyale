import tkinter as tk
from tkinter import messagebox
import random

class JuegoMultiplicaciones:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego de Multiplicaciones y Divisiones")
        
        self.nivel = 1
        self.puntos = 0
        self.tiempo_jugado = 0  # Tiempo jugado en segundos
        
        self.matriz_tamaño = 3  # Número de filas (niveles)
        self.matriz_ancho = 11   # Número de columnas (1-10 + 1 para la fila de encabezado)
        self.operaciones_realizadas = set()
        
        self.crear_widgets()
        self.iniciar_juego()

    def crear_widgets(self):
        # Matriz
        self.matriz_frame = tk.Frame(self.root)
        self.matriz_frame.pack(pady=20)

        # Encabezados de la matriz
        self.labels_encabezados = [tk.Label(self.matriz_frame, text="", width=5, font=('Arial', 14)) for _ in range(self.matriz_ancho)]
        self.labels_encabezados[0].config(text="x")
        for i in range(1, self.matriz_ancho):
            self.labels_encabezados[i].config(text=str(i))
        for j, label in enumerate(self.labels_encabezados):
            label.grid(row=0, column=j)

        self.labels_matriz = [[tk.Label(self.matriz_frame, text="", width=5, font=('Arial', 14)) for _ in range(self.matriz_ancho)] for _ in range(self.matriz_tamaño)]
        for i in range(self.matriz_tamaño):
            self.labels_matriz[i][0].grid(row=i + 1, column=0)  # Colocar en la matriz
            self.labels_matriz[i][0].config(text=str(i + 1))  # Números en la primera columna
            for j in range(1, self.matriz_ancho):
                self.labels_matriz[i][j].grid(row=i + 1, column=j)

        # Estructura de la operación
        self.operacion_label = tk.Label(self.root, text="", font=('Arial', 16))
        self.operacion_label.pack(pady=10)

        # Entrada del jugador
        self.entrada = tk.Entry(self.root, font=('Arial', 14))
        self.entrada.pack(pady=10)
        self.entrada.bind('<Return>', self.verificar_respuesta)

        # Marcador
        self.marcador_label = tk.Label(self.root, text=f"Puntos: {self.puntos}", font=('Arial', 14))
        self.marcador_label.pack(pady=10)

        # Nivel
        self.nivel_label = tk.Label(self.root, text=f"Nivel: {self.nivel}", font=('Arial', 14))
        self.nivel_label.pack(pady=10)

        # Tiempo
        self.tiempo_label = tk.Label(self.root, text=f"Tiempo jugado: {self.tiempo_jugado} s", font=('Arial', 14))
        self.tiempo_label.pack(pady=10)

    def iniciar_juego(self):
        self.generar_operacion()
        self.actualizar_tiempo()

    def generar_operacion(self):
        while True:
            if self.nivel == 1:
                self.num1 = random.randint(1, 3)
                self.num2 = random.randint(1, 10)
            elif self.nivel == 2:
                self.num1 = random.randint(4, 6)  # Filas 4-6
                self.num2 = random.randint(1, 10)  # Columnas 1-10
            else:
                self.num1 = random.randint(7, 9)  # Filas 7-9
                self.num2 = random.randint(1, 10)  # Columnas 1-10

            self.resultado = self.num1 * self.num2

            if (self.num1, self.num2) not in self.operaciones_realizadas:
                self.operaciones_realizadas.add((self.num1, self.num2))
                self.operacion_label.config(text=f"{self.num1} * ? = {self.resultado}")
                break

    def verificar_respuesta(self, event):
        try:
            respuesta_usuario = int(self.entrada.get())
            if respuesta_usuario == self.num2:
                self.puntos += 1
                self.marcador_label.config(text=f"Puntos: {self.puntos}")

                # Colocar el resultado en la posición correcta
                if self.nivel == 1:
                    fila = self.num1 - 1  # 1-3
                elif self.nivel == 2:
                    fila = self.num1 - 4  # 4-6
                else:
                    fila = self.num1 - 7  # 7-9
                
                columna = self.num2  # La columna correcta

                self.labels_matriz[fila][columna].config(text=f"{self.resultado}")
                
                # Limpiar entrada
                self.entrada.delete(0, tk.END)
                
                if len(self.operaciones_realizadas) == self.matriz_tamaño * (self.matriz_ancho - 1):
                    self.subir_nivel()

                self.generar_operacion()
            else:
                messagebox.showerror("Error", "Respuesta incorrecta. Intenta de nuevo.")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa un número válido.")

    def subir_nivel(self):
        self.nivel += 1
        self.operaciones_realizadas.clear()  # Reiniciar operaciones para el nuevo nivel
        if self.nivel > 3:
            messagebox.showinfo("Fin del juego", f"¡Juego terminado! Puntuación final: {self.puntos}")
            self.root.quit()
            return
        else:
            self.nivel_label.config(text=f"Nivel: {self.nivel}")
            self.reset_matriz()

    def reset_matriz(self):
        for i in range(self.matriz_tamaño):
            for j in range(self.matriz_ancho):
                self.labels_matriz[i][j].config(text="")
        
        # Actualizar encabezados según el nuevo nivel
        self.labels_encabezados[0].config(text="x")
        for i in range(1, self.matriz_ancho):
            self.labels_encabezados[i].config(text=str(i))
        
        # Establecer números en la primera columna
        if self.nivel == 1:
            for i in range(3):
                self.labels_matriz[i][0].config(text=str(i + 1))  # Números 1, 2, 3
        elif self.nivel == 2:
            for i in range(3):
                self.labels_matriz[i][0].config(text=str(i + 4))  # Números 4, 5, 6
        else:
            for i in range(3):
                self.labels_matriz[i][0].config(text=str(i + 7))  # Números 7, 8, 9
        
        for j, label in enumerate(self.labels_encabezados):
            label.grid(row=0, column=j)

    def actualizar_tiempo(self):
        self.tiempo_jugado += 1
        self.tiempo_label.config(text=f"Tiempo jugado: {self.tiempo_jugado} s")
        self.root.after(1000, self.actualizar_tiempo)  # Actualizar cada segundo

if __name__ == "__main__":
    root = tk.Tk()
    juego = JuegoMultiplicaciones(root)
    root.mainloop()
