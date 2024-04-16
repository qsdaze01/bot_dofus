import tkinter as tk

def get_screen_dimensions():
    root = tk.Tk()
    # Récupère les dimensions de l'écran
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.destroy()  # Ferme la fenêtre tkinter

    return screen_width, screen_height