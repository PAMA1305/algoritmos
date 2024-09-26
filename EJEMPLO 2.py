import tkinter as tk
from tkinter import messagebox, ttk
import random
class App:
 def __init__(self, root):
 self.root = root
 self.root.title("Juego Memorame")
 self.root.geometry("400x400")
 self.user_data = {}
 self.current_frame = None
 self.level = 1
 self.show_inicio()
 def show_inicio(self):
 self.clear_frame()
 self.current_frame = tk.Frame(self.root, bg="lightblue")
 self.current_frame.pack(fill=tk.BOTH, expand=True)
 title_label = tk.Label(self.current_frame, text="INICIO", bg="lightblue", font=
("Arial", 24))
 title_label.pack(pady=20)
 btn_store_data = tk.Button(self.current_frame, text="Almacenar Datos",
command=self.store_data)
 btn_store_data.pack(pady=10)
 btn_show_progress = tk.Button(self.current_frame, text="Ver Avance",
command=self.show_progress)
 btn_show_progress.pack(pady=10)
 btn_game_rules = tk.Button(self.current_frame, text="Reglas del Juego",
command=self.show_rules)
 btn_game_rules.pack(pady=10)
 btn_new_game = tk.Button(self.current_frame, text="Nuevo Juego",
command=self.start_new_game)






