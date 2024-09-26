import tkinter as tk
from tkinter import messagebox, ttk
import random



class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego Memorama")
        self.root.geometry("400x400")
        self.user_data = {}
        self.current_frame = None
        self.level = 1 # Inicializa Pygame para reproducir música
        self.show_inicio1()


    def show_main_menu(self):
            # Limpiar la ventana
            for widget in self.root.winfo_children():
                widget.destroy()



    def show_inicio(self):
        self.clear_frame()
        self.current_frame = tk.Frame(self.root, bg="lightblue")
        self.current_frame.pack(fill=tk.BOTH, expand=True)

        title_label = tk.Label(self.current_frame, text="INICIO", bg="lightblue", font=("Arial", 24))
        title_label.pack(pady=20)

        btn_store_data = tk.Button(self.current_frame, text="Almacenar Datos", command=self.store_data)
        btn_store_data.pack(pady=10)

        btn_show_progress = tk.Button(self.current_frame, text="Ver Avance", command=self.show_progress)
        btn_show_progress.pack(pady=10)

        btn_game_rules = tk.Button(self.current_frame, text="Reglas del Juego", command=self.show_rules)
        btn_game_rules.pack(pady=10)

        btn_new_game = tk.Button(self.current_frame, text="Nuevo Juego", command=self.start_new_game)
        btn_new_game.pack(pady=10)



    def show_inicio1(self):
        self.clear_frame()
        self.current_frame = tk.Frame(self.root, bg="lightblue")
        self.current_frame.pack(fill=tk.BOTH, expand=True)

        title_label = tk.Label(self.current_frame, text="INICIO", bg="lightblue", font=("Arial", 24))
        title_label.pack(pady=20)

        btn_store_data = tk.Button(self.current_frame, text="Almacenar Datos", command=self.store_data)
        btn_store_data.pack(pady=10)

        btn_show_progress = tk.Button(self.current_frame, text="Ver Avance", command=self.show_progress)
        btn_show_progress.pack(pady=10)

        btn_game_rules = tk.Button(self.current_frame, text="Reglas del Juego", command=self.show_rules)
        btn_game_rules.pack(pady=10)

        btn_new_game = tk.Button(self.current_frame, text="Nuevo Juego", command=self.start_new_game)
        btn_new_game.pack(pady=10)

    def clear_frame(self):
        if self.current_frame:
            self.current_frame.destroy()

    def store_data(self):
        self.clear_frame()
        self.current_frame = tk.Frame(self.root, bg="lightblue")
        self.current_frame.pack(fill=tk.BOTH, expand=True)

        label = tk.Label(self.current_frame, text="Ingrese su nombre:", bg="lightblue")
        label.pack(pady=10)

        self.user_entry = tk.Entry(self.current_frame)
        self.user_entry.pack(pady=10)

        btn_save = tk.Button(self.current_frame, text="Guardar", command=self.save_user_data)
        btn_save.pack(pady=10)

        btn_back = tk.Button(self.current_frame, text="Regresar", command=self.show_inicio1)
        btn_back.pack(pady=10)

    def save_user_data(self):
        user_name = self.user_entry.get()
        if user_name:
            self.user_data[user_name] = {"levels_completed": 0}
            messagebox.showinfo("Guardado", f"Datos de {user_name} guardados.")
            self.user_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingrese un nombre.")

    def show_progress(self):
        self.clear_frame()
        self.current_frame = tk.Frame(self.root, bg="lightblue")
        self.current_frame.pack(fill=tk.BOTH, expand=True)

        label = tk.Label(self.current_frame, text="Avance del Usuario", bg="lightblue", font=("Arial", 18))
        label.pack(pady=10)

        self.progress_tree = ttk.Treeview(self.current_frame, columns=("Usuario", "Niveles Completados"),
                                          show='headings')
        self.progress_tree.heading("Usuario", text="Usuario")
        self.progress_tree.heading("Niveles Completados", text="Niveles Completados")
        self.progress_tree.pack(pady=20)

        for user, data in self.user_data.items():
            self.progress_tree.insert("", "end", values=(user, data["levels_completed"]))


        btn_back = tk.Button(self.current_frame, text="Regresar", command=self.show_inicio1)
        btn_back.pack(pady=10)

    def show_rules(self):
        self.clear_frame()
        self.current_frame = tk.Frame(self.root, bg="lightblue")
        self.current_frame.pack(fill=tk.BOTH, expand=True)

        rules_label = tk.Label(self.current_frame, text="Reglas del Juego", bg="lightblue", font=("Arial", 18))
        rules_label.pack(pady=10)

        rules_text = (
            "1. Memoriza las cartas.\n"
            "2. Encuentra las parejas de números.\n"
            "3. Gana el juego emparejando todas las cartas.\n"
            "4. ¡Diviértete!"
        )
        rules_display = tk.Label(self.current_frame, text=rules_text, bg="lightblue", justify=tk.LEFT)
        rules_display.pack(pady=10)

        btn_back = tk.Button(self.current_frame, text="Regresar", command=self.show_inicio1)
        btn_back.pack(pady=10)

    def start_new_game(self):
        self.clear_frame()
        self.current_frame = tk.Frame(self.root, bg="lightblue")
        self.current_frame.pack(fill=tk.BOTH, expand=True)

        label = tk.Label(self.current_frame, text="Ingrese su nombre para iniciar el juego:", bg="lightblue")
        label.pack(pady=10)

        self.new_game_entry = tk.Entry(self.current_frame)
        self.new_game_entry.pack(pady=10)

        btn_start = tk.Button(self.current_frame, text="Iniciar Juego", command=self.initiate_game)
        btn_start.pack(pady=10)

        btn_back = tk.Button(self.current_frame, text="Regresar", command=self.show_inicio1)
        btn_back.pack(pady=10)

    def initiate_game(self):
        user_name = self.new_game_entry.get()
        if user_name in self.user_data:
            self.new_game_entry.delete(0, tk.END)
            self.level = 1
            self.show_game_board(user_name, self.level)
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingrese un nombre registrado.")

    def show_game_board(self, user_name, level):
        self.clear_frame()
        self.current_frame = tk.Frame(self.root, bg="lightblue")
        self.current_frame.pack(fill=tk.BOTH, expand=True)

        if level == 1:
            self.cards = list(range(1, 11)) * 2  # Números del 1 al 10
        elif level == 2:
            self.cards = list(range(11, 21)) * 2  # Números del 11 al 20
        elif level == 3:
            self.cards = list(range(21, 31)) * 2  # Números del 21 al 30
        elif level == 4:
            self.cards = list(range(31, 41)) * 2  # Números del 31 al 40
        else:
            self.cards = list(range(41, 51)) * 2  # Números del 41 al 50

        random.shuffle(self.cards)
        self.buttons = []

        for i in range(4):  # 4 filas
            row = []
            for j in range(5):  # 5 columnas
                btn = tk.Button(self.current_frame, text="?", width=5, height=2,
                                command=lambda x=i, y=j: self.flip_card(x, y, user_name, level))
                btn.grid(row=i, column=j, padx=5, pady=5)
                row.append(btn)
            self.buttons.append(row)

        self.first_card = None
        self.second_card = None
        self.first_card_pos = None
        self.second_card_pos = None

        btn_back = tk.Button(self.current_frame, text="Regresar", command=self.show_inicio1)
        btn_back.grid(row=5, columnspan=5, pady=10)

    def flip_card(self, row, col, user_name, level):
        button = self.buttons[row][col]
        card_value = self.cards[row * 5 + col]

        button.config(text=card_value, state="disabled")

        if self.first_card is None:
            self.first_card = card_value
            self.first_card_pos = (row, col)
        else:
            self.second_card = card_value
            self.second_card_pos = (row, col)
            self.root.after(1000, self.check_match, user_name, level)

    def check_match(self, user_name, level):
        if self.first_card == self.second_card:
            messagebox.showinfo("¡Coincidencia!", "¡Encontraste un par!")
            self.user_data[user_name]["levels_completed"] += 1
        else:
            messagebox.showinfo("No coincide", "No es un par.")
            self.buttons[self.first_card_pos[0]][self.first_card_pos[1]].config(text="?", state="normal")
            self.buttons[self.second_card_pos[0]][self.second_card_pos[1]].config(text="?", state="normal")

        self.first_card = None
        self.second_card = None

        # Verifica si el juego ha terminado
        if all(btn["text"] != "?" for row in self.buttons for btn in row):
            if level < 5:
                messagebox.showinfo("Nivel Completo", f"¡Felicidades! Has completado el Nivel {level}.")
                self.level += 1
                self.show_game_board(user_name, self.level)
            else:
                messagebox.showinfo("Juego terminado", f"¡Felicidades, {user_name}! Has terminado el juego.")
                self.show_inicio1()





if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
