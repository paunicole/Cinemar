import tkinter as tk
from tkinter import ttk
from model.pelicula import Pelicula
from view.frame_pelicula import PeliculaCliente
from view.frame_ubicacion import Ubicacion

class Cartelera(tk.Frame):
    def __init__(self, ventana_padre=None, master=None, cuenta_usuario=None, base_datos=None):
        tk.Frame.__init__(self, master)
        self.ventana_padre = ventana_padre
        self.master = master
        self.cuenta_usuario = cuenta_usuario
        self.bdd = base_datos
        self.pelicula = Pelicula()

        """NOTEBOOK"""
        self.notebook = ttk.Notebook(self)

        """FRAMES"""
        self.p1 = PeliculaCliente(self, self.notebook, self.cuenta_usuario, self.bdd)
        #self.p2 = Ubicacion(self, self.notebook, self.cuenta_usuario, self.bdd)

        """WIDGETS"""
        self.label_anterior = ttk.Label(self)
        self.button_continuar1 = ttk.Button(self)

        self.notebook_config()
        self.notebook_grid()

        self.widgets_config()
        self.widgets_grid()


    def notebook_config(self):
        self.notebook.add(self.p1, text='Cartelera')
        #self.notebook.add(self.p2, text='Ubicaciones')

    def notebook_grid(self):
        self.notebook.grid(row=1, column=0)

    def widgets_config(self):
        self.label_anterior.config(text='Elegí una peli y reserva tu lugar', foreground='#FFFFFF', font=('Segoe UI Black', 18), background='black', justify='center')
        self.button_continuar1.config(text='Continuar', command=self.continuar1)

    def widgets_grid(self):
        self.label_anterior.grid(row=0, column=0, columnspan=8, pady=20, ipady=10)
        self.button_continuar1.grid(row=2, column=0, ipadx=5, ipady=5, padx=20, pady=20, sticky='E')

    def continuar1(self):
        pass
        #self.notebook.select(self.p2)