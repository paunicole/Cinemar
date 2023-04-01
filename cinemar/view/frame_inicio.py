import tkinter as tk

class Inicio(tk.Frame):
    def __init__(self, master = None, admin = 0):
        tk.Frame.__init__(self, master)
        self.master = master

        if admin == 1:
            self.img_bienvenido = tk.PhotoImage(file="assets\main.png")
            self.img_bienvenido = self.img_bienvenido.subsample(2)
        else:
            self.img_bienvenido = tk.PhotoImage(file="assets\main.png")
            self.img_bienvenido = self.img_bienvenido.subsample(2)
        
        """WIDGETS"""
        self.label_inicio = tk.Label(self)

        self.widgets_config()
        self.widgets_grid()


    def widgets_config(self):
        self.label_inicio.config(image=self.img_bienvenido, border=0)
    
    def widgets_grid(self):
        self.label_inicio.grid(row=0, column=0, columnspan=8)