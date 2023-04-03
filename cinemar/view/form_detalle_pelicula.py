import tkinter as tk
from tkinter import ttk, Toplevel
from model.pelicula import Pelicula

class MasDetalles(Toplevel):
    def __init__(self, master=None, pelicula=None, base_datos=None):
        Toplevel.__init__(self, master)
        self.master = master
        self.geometry('700x480')
        self.config(bg='black')
        self.title('Más detalles')
        self.iconbitmap('assets\logo.ico')
        self.resizable(0, 0)

        self.bdd = base_datos
        self.pelicula = Pelicula()
        self.pelicula_detalles = self.pelicula.ver_mas(self.bdd, pelicula)
        
        """FRAMES"""
        self.frame = tk.Frame(self)
    
        """WIDGETS"""
        self.imagen = ttk.Label(self.frame)
        self.label_cabecera = ttk.Label(self.frame)
        self.label_duracion = ttk.Label(self.frame)
        self.label_genero = ttk.Label(self.frame)
        self.label_director = ttk.Label(self.frame)
        self.label_actor = ttk.Label(self.frame)
        self.label_sinopsis = ttk.Label(self.frame)

        self.frames_config()
        self.frames_grid()

        self.widgets_config()
        self.widgets_grid()

    def frames_config(self):
        self.frame.config(border=15, bg='black')
    
    def frames_grid(self):
        self.frame.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

    def widgets_config(self):
        self.label_cabecera.config(text=self.pelicula_detalles[0], wraplength=300, foreground='#FFFFFF', font=('Segoe UI Black', 25), background='black')
        
        self.imagen.config(text='Imagen', foreground='#FFFFFF', font=('Segoe UI Black', 10), background='black')

        self.label_duracion.config(text='Duración: ' + str(self.pelicula_detalles[1]), foreground='#FFFFFF', font=('Segoe UI Black', 10), background='black')
        self.label_genero.config(text='Género: ' + self.pelicula_detalles[2], wraplength=300, foreground='#FFFFFF', font=('Segoe UI Black', 10), background='black')
        self.label_director.config(text='Director: ' + self.pelicula_detalles[3], foreground='#FFFFFF', font=('Segoe UI Black', 10), background='black')
        self.label_actor.config(text='Actores: ' + self.pelicula_detalles[4], wraplength=300, foreground='#FFFFFF', font=('Segoe UI Black', 10), background='black')
        self.label_sinopsis.config(text='Sinopsis: \n' + self.pelicula_detalles[5], wraplength=650, foreground='#FFFFFF', font=('Segoe UI Black', 10), background='black')

    def widgets_grid(self):
        self.imagen.grid(row=0, column=0, rowspan=5, sticky='NS')
        self.label_cabecera.grid(row=0, column=1, sticky='W')
        
        self.label_genero.grid(row=1, column=1, pady=10, sticky='W')
        self.label_duracion.grid(row=3, column=1, pady=10, sticky='W')   
        self.label_actor.grid(row=5, column=1, pady=10, sticky='W')
        self.label_director.grid(row=7, column=1, pady=10, sticky='W') 
        self.label_sinopsis.grid(row=9, column=0, columnspan=2, pady=10, sticky='W')
    