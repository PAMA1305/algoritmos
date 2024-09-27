import tkinter as tk
from tkinter import messagebox, ttk, filedialog
import random
import time
import pygame

# Inicializa Pygame para el reproductor de música
pygame.mixer.init()


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego Memórame")
        self.root.geometry("700x600")
        self.root.configure(bg="black")  # Color de fondo negro

        # Almacén de usuarios y niveles
        self.usuarios = {}
        self.colores = ["#39FF14", "#FF073A", "#FFEC40", "#A800FF"]  # Colores neón
        self.secuencia = []
        self.intentos = []

        self.inicio_menu()

    def inicio_menu(self):
        self.clear_frame()

        inicio_frame = tk.Frame(self.root, bg="black")  # Color de fondo negro
        inicio_frame.pack(expand=True, fill=tk.BOTH)

        title = tk.Label(inicio_frame, text="¿RECUERDAS EL COLOR?", font=("Stencil", 24), bg="black", fg="blue")
        title.pack(pady=20)

        nota = tk.Label(inicio_frame, text="SI AÚN NO SABES JUGAR YO RECOMIENDO QUE ENTRES A LAS REGLAS DEL JUEGO",
                        font=("Arial", 12), bg="black", fg="white", wraplength=400)
        nota.pack(pady=10)

        btn_nuevo_juego = tk.Button(inicio_frame, text="Registrar Usuario", command=self.nuevo_juego, bg="#4A90E2",
                                    fg="white", width=25, height=2)
        btn_nuevo_juego.pack(pady=10)

        btn_avance = tk.Button(inicio_frame, text="Estadisticas", command=self.mostrar_avance, bg="#4A90E2",
                               fg="white", width=25, height=2)
        btn_avance.pack(pady=10)

        btn_reglas = tk.Button(inicio_frame, text="Reglas del Juego", command=self.mostrar_reglas, bg="#4A90E2",
                               fg="white", width=25, height=2)
        btn_reglas.pack(pady=10)

        btn_reproductor = tk.Button(inicio_frame, text="Reproductor de Música", command=self.reproductor_musica,
                                    bg="#4A90E2", fg="white", width=25, height=2)
        btn_reproductor.pack(pady=10)

        # Botón para cerrar la aplicación
        btn_cerrar = tk.Button(inicio_frame, text="Cerrar", command=self.root.quit, bg="#FF073A", fg="white", width=25,
                               height=2)
        btn_cerrar.pack(pady=10)

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def mostrar_avance(self):
        self.clear_frame()

        avance_frame = tk.Frame(self.root, bg="black")  # Color de fondo negro
        avance_frame.pack(expand=True, fill=tk.BOTH)

        title = tk.Label(avance_frame, text="Avances de usuario", font=("Stencil", 20), bg="black", fg="yellow")
        title.pack(pady=20)

        self.tabla_avance = ttk.Treeview(avance_frame, columns=("Usuario", "Aciertos", "Errores"), show='headings')
        self.tabla_avance.heading("Usuario", text="Usuario")
        self.tabla_avance.heading("Aciertos", text="Aciertos")
        self.tabla_avance.heading("Errores", text="Errores")

        self.tabla_avance.tag_configure('center', anchor='center')
        self.tabla_avance.column("Usuario", anchor='center')
        self.tabla_avance.column("Aciertos", anchor='center')
        self.tabla_avance.column("Errores", anchor='center')

        self.tabla_avance.pack(pady=20)

        for usuario, datos in self.usuarios.items():
            self.tabla_avance.insert("", "end", values=(usuario, datos['aciertos'], datos['errores']), tags=('center',))

        btn_regresar = tk.Button(avance_frame, text="Regresar al Menú INICIO", command=self.inicio_menu, bg="#4A90E2",
                                 fg="white", width=25, height=2)
        btn_regresar.pack(pady=10)

    def mostrar_reglas(self):
        self.clear_frame()

        reglas_frame = tk.Frame(self.root, bg="black")  # Color de fondo negro
        reglas_frame.pack(expand=True, fill=tk.BOTH)

        title = tk.Label(reglas_frame, text="Reglas del Juego", font=("Stencil", 20), bg="black", fg="orange")
        title.pack(pady=20)

        reglas_texto = tk.Label(reglas_frame, text=(
            "Cómo jugar:\n"
            "1. Para poder empezar a jugar necesitas presionar el botón de “Registrar Usuario” al momento de presionarlo te mandará a un menú en el cual podrás registrar un usuario.\n"
            "2. Si ya te registraste, tu usuario ahora podrá presionar el botón de “Iniciar Juego de Memoria” y ¡Que comience la diversión!\n"
            "3. Si pierdes o ganas recuerda que todos tus puntajes como: aciertos y errores se estarán guardando automáticamente en tu avance de usuario, este lo puedes ver o encontrar en el menú principal solo seleccionando el botón “Estadísticas”.\n"
            "4. Recuerda que antes de empezar a jugar también tenemos la opción de colocar una canción de fondo con nuestro reproductor, el cual reproduce música en mp3. Solo necesitas tener descargada la canción en tu PC y podrás seleccionarla. Para poder seleccionar la canción de tu agrado, necesitas presionar el botón en el menú inicial “Reproductor de Música”, después en el menú de Reproductor de música presiona el botón “Seleccionar Canción” y te desplegará una ventana con tus archivos mp3 que tengas en tu PC, solo escoges la canción de tu agrado y presionas el botón “Reproducir Música” y listo, ahora puedes disfrutar del juego con una buena melodía.\n"
            "\nReglas del Juego:\n"
            "1. Recuerda las posiciones de los colores que se encienden.\n"
            "2. Haz clic en los colores encendidos en el mismo orden.\n"
            "3. Gana puntos por cada acierto y si fallas, perderás puntos.\n"
            "4. El juego termina cuando se alcanza el número máximo de secuencias o decides salir."
        ), wraplength=400, bg="black", fg="white", justify="left")
        reglas_texto.pack(pady=20)

        btn_regresar = tk.Button(reglas_frame, text="Regresar al Menú INICIO", command=self.inicio_menu, bg="#4A90E2",
                                 fg="white", width=25, height=2)
        btn_regresar.pack(pady=10)

    def nuevo_juego(self):
        self.clear_frame()

        nuevo_juego_frame = tk.Frame(self.root, bg="black")  # Color de fondo negro
        nuevo_juego_frame.pack(expand=True, fill=tk.BOTH)

        title = tk.Label(nuevo_juego_frame, text="Registro de Usuario", font=("Stencil", 20), bg="black", fg="white")
        title.pack(pady=20)

        self.usuario_entry = tk.Entry(nuevo_juego_frame)
        self.usuario_entry.pack(pady=10)
        self.usuario_entry.insert(0, "")

        btn_guardar = tk.Button(nuevo_juego_frame, text="Registrar Usuario", command=self.guardar_usuario, bg="#4A90E2",
                                fg="white", width=25, height=2)
        btn_guardar.pack(pady=10)

        btn_jugar = tk.Button(nuevo_juego_frame, text="Iniciar Juego de Memoria", command=self.iniciar_juego,
                              bg="#4A90E2", fg="white", width=25, height=2)
        btn_jugar.pack(pady=10)

        btn_regresar = tk.Button(nuevo_juego_frame, text="Regresar al Menú INICIO", command=self.inicio_menu,
                                 bg="#4A90E2", fg="white", width=25, height=2)
        btn_regresar.pack(pady=10)

    def guardar_usuario(self):
        usuario = self.usuario_entry.get().strip()
        if usuario and usuario not in self.usuarios:
            self.usuarios[usuario] = {'aciertos': 0, 'errores': 0}  # Inicializa aciertos y errores
            messagebox.showinfo("Éxito", f"Usuario '{usuario}' registrado.")
            self.usuario_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Error", "Usuario ya existe o nombre vacío.")

    def iniciar_juego(self):
        self.clear_frame()
        self.secuencia = []
        self.intentos = []
        self.dificultad = 4  # número de colores a mostrar
        self.jugar()

    def jugar(self):
        if len(self.secuencia) < 5:  # Cambia el límite a 5 secuencias
            nuevo_color = random.choice(self.colores)
            self.secuencia.append(nuevo_color)
            self.mostrar_colores()
        else:
            self.finalizar_juego()  # Llama al método para finalizar el juego

    def mostrar_colores(self):
        for i, color in enumerate(self.secuencia):
            self.root.after(i * 1000, self.encender_cuadro, color)
        self.root.after(len(self.secuencia) * 1000, self.pedir_intentos)

    def encender_cuadro(self, color):
        cuadro = tk.Frame(self.root, bg=color, width=200, height=200)
        cuadro.grid(row=0, column=0, padx=5, pady=5)
        self.root.update()
        time.sleep(0.5)
        cuadro.destroy()

    def pedir_intentos(self):
        self.intentos = []
        self.mostrar_tablero()

    def mostrar_tablero(self):
        self.cuadros = []
        # Ajustar tamaño y espaciado de los cuadros de colores
        for i, color in enumerate(self.colores):
            cuadro = tk.Frame(self.root, bg=color, width=150, height=150)  # Aumentar tamaño
            cuadro.grid(row=i // 2, column=i % 2, padx=10, pady=10)  # Reducir espaciado
            cuadro.bind("<Button-1>", lambda e, c=color: self.registrar_intento(c))
            self.cuadros.append(cuadro)

        # Centra la cuadrícula
        for i in range(2):  # Dos filas
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(2):  # Dos columnas
            self.root.grid_columnconfigure(i, weight=1)

    def registrar_intento(self, color):
        self.intentos.append(color)
        if len(self.intentos) == len(self.secuencia):
            self.comprobar_intentos()

    def comprobar_intentos(self):
        if self.intentos == self.secuencia:
            usuario_actual = list(self.usuarios.keys())[-1]  # Asume que el último usuario registrado es el actual
            self.usuarios[usuario_actual]['aciertos'] += 1
            messagebox.showinfo("¡Correcto!", "¡Has acertado!")
            self.jugar()
        else:
            usuario_actual = list(self.usuarios.keys())[-1]
            self.usuarios[usuario_actual]['errores'] += 1
            messagebox.showerror("¡Incorrecto!", "Has fallado, Padrino. Sigue echándole ganas.")
            self.intentos = []
            self.secuencia = []
            self.inicio_menu()

    def finalizar_juego(self):
        messagebox.showinfo("¡Felicidades!", "¡Felicidades, ya ganaste, Padrino!")
        self.intentos = []
        self.secuencia = []
        self.inicio_menu()  # Regresa al menú de inicio después de finalizar

    def reproductor_musica(self):
        self.clear_frame()

        reproductor_frame = tk.Frame(self.root, bg="black")  # Color de fondo negro
        reproductor_frame.pack(expand=True, fill=tk.BOTH)

        title = tk.Label(reproductor_frame, text="Reproductor de Música", font=("Stencil", 20), bg="black", fg="pink")
        title.pack(pady=20)

        btn_seleccionar = tk.Button(reproductor_frame, text="Seleccionar Canción", command=self.seleccionar_cancion,
                                    bg="#4A90E2", fg="white", width=25, height=2)
        btn_seleccionar.pack(pady=10)

        btn_play = tk.Button(reproductor_frame, text="Reproducir Música", command=self.play_music, bg="#4A90E2",
                             fg="white", width=25, height=2)
        btn_play.pack(pady=10)

        btn_stop = tk.Button(reproductor_frame, text="Detener Música", command=self.stop_music, bg="#4A90E2",
                             fg="white", width=25, height=2)
        btn_stop.pack(pady=10)

        btn_regresar = tk.Button(reproductor_frame, text="Regresar al Menú INICIO", command=self.inicio_menu,
                                 bg="#4A90E2", fg="white", width=25, height=2)
        btn_regresar.pack(pady=10)

        self.current_music = None

    def seleccionar_cancion(self):
        self.current_music = filedialog.askopenfilename(title="Seleccionar Canción",
                                                        filetypes=[("Archivos de Audio", "*.mp3;*.wav")])
        if self.current_music:
            messagebox.showinfo("Éxito", f"Canción seleccionada: {self.current_music}")

    def play_music(self):
        if self.current_music:
            pygame.mixer.music.load(self.current_music)
            pygame.mixer.music.play(-1)  # Reproduce en bucle
        else:
            messagebox.showwarning("Error", "No se ha seleccionado ninguna canción.")

    def stop_music(self):
        pygame.mixer.music.stop()


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
