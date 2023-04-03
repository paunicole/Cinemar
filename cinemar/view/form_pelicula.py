import tkinter as tk
from tkinter import ttk, Toplevel, messagebox
from model.pelicula import Pelicula

class FormularioPelicula(Toplevel):
    def __init__(self, master = None, base_datos = None):
        Toplevel.__init__(self, master)
        self.master = master
        self.geometry('720x720')
        self.config(bg='black')
        self.title('Agregar Pelicula')
        self.iconbitmap('assets\logo.ico')
        self.protocol('WM_DELETE_WINDOW', self.cancelar)
        self.resizable(0, 0)

        self.bdd = base_datos
        self.pelicula = Pelicula()

        """FRAMES"""
        self.frame_cabecera = tk.Frame(self)
        self.frame_datos = tk.Frame(self)
        self.frame_botones = tk.Frame(self)

        """WIDGETS"""
        #Titulo
        self.cabecera = ttk.Label(self.frame_cabecera)
        
        #Labels
        self.label_nombre = ttk.Label(self.frame_datos)
        self.label_duracion = ttk.Label(self.frame_datos)
        self.label_genero = ttk.Label(self.frame_datos)        
        self.label_tipo = ttk.Label(self.frame_datos)
        self.label_director = ttk.Label(self.frame_datos)
        self.label_actor = ttk.Label(self.frame_datos)    
        self.label_sinopsis = ttk.Label(self.frame_datos)

        #Inputs
        self.input_nombre = ttk.Entry(self.frame_datos)
        self.input_duracion = ttk.Entry(self.frame_datos)
        self.input_genero = ttk.Entry(self.frame_datos)
        self.input_tipo = ttk.Combobox(self.frame_datos)
        self.input_director = ttk.Entry(self.frame_datos)
        self.input_actor = tk.Text(self.frame_datos)        
        self.input_sinopsis = tk.Text(self.frame_datos)

        #Buttons
        self.button_cargar = ttk.Button(self.frame_botones)
        self.button_cancelar = ttk.Button(self.frame_botones)

        self.frames_config()
        self.widgets_config()

        self.frames_grid()
        self.widgets_grid()


    def frames_config(self):
        self.frame_cabecera.config(border=15, bg='red')
        self.frame_datos.config(bg='black')
        self.frame_botones.config(bg='black')

    def frames_grid(self):
        self.frame_cabecera.grid(row=0, column=0, rowspan=2, columnspan=3)
        self.frame_datos.grid(row=2, column=0, rowspan=12, columnspan=3, padx=30, pady=20)
        self.frame_botones.grid(row=14, column=0, columnspan=3)

    def widgets_config(self):
        #Titulo
        self.cabecera.config(text='Ingresá los datos de la nueva pelicula', foreground='#FFFFFF', font=('Segoe UI Black', 25), background='red')
        
        #Labels
        self.label_nombre.config(text='Nombre', foreground='#FFFFFF', font=('Segoe UI Black', 18), background='black')
        self.label_duracion.config(text='Duración', foreground='#FFFFFF', font=('Segoe UI Black', 18), background='black')        
        self.label_genero.config(text='Genero', foreground='#FFFFFF', font=('Segoe UI Black', 18), background='black')        
        self.label_tipo.config(text='Tipo', foreground='#FFFFFF', font=('Segoe UI Black', 18), background='black')
        self.label_director.config(text='Director', foreground='#FFFFFF', font=('Segoe UI Black', 18), background='black') 
        self.label_actor.config(text='Actores', foreground='#FFFFFF', font=('Segoe UI Black', 18), background='black')
        self.label_sinopsis.config(text='Sinopsis', foreground='#FFFFFF', font=('Segoe UI Black', 18), background='black')

        #Inputs
        self.input_nombre.config(width=30)
        self.input_duracion.config(width=30)
        self.input_genero.config(width=30)    
        self.input_tipo.config(width=27, state='readonly', values=['2D', '3D'])
        self.input_director.config(width=40)
        self.input_actor.config(width=80, height=4, wrap='word')
        self.input_sinopsis.config(width=80, height=7, wrap='word')

        #Buttons
        self.button_cargar.config(text='Cargar Datos', command=self.cargar)
        self.button_cancelar.config(text='Cancelar', command=self.cancelar)

    def widgets_grid(self):
        #Titulo
        self.cabecera.grid(row=0)   
        #Nombre
        self.label_nombre.grid(row=0, column=0, pady=10)
        self.input_nombre.grid(row=1, column=0)
        #Duracion
        self.label_duracion.grid(row=0, column=2, pady=10)
        self.input_duracion.grid(row=1, column=2)
        #Genero
        self.label_genero.grid(row=2, column=0, pady=10)
        self.input_genero.grid(row=3, column=0)
        #Tipo
        self.label_tipo.grid(row=2, column=2, pady=10)
        self.input_tipo.grid(row=3, column=2)
        #Director
        self.label_director.grid(row=4, column=0, columnspan=3, pady=10)
        self.input_director.grid(row=5, column=0, columnspan=3)
        #Actores
        self.label_actor.grid(row=6, column=0, columnspan=3, pady=10)
        self.input_actor.grid(row=7, column=0, rowspan=2, columnspan=3) 
        #Sinopsis
        self.label_sinopsis.grid(row=9, column=0, columnspan=3, pady=10)
        self.input_sinopsis.grid(row=10, column=0, rowspan=3, columnspan=3)
        #Botones
        self.button_cargar.grid(row=0, column=0, padx=20, pady=10, ipadx=5, ipady=5)
        self.button_cancelar.grid(row=0, column=2, padx=20, pady=10, ipadx =5, ipady=5)

    def cargar(self):
        nom = self.input_nombre.get()
        dur = self.input_duracion.get()
        gen = self.input_genero.get()
        tipo = self.input_tipo.get()
        dir = self.input_director.get()
        act = self.input_actor.get('1.0', 'end')
        sin = self.input_sinopsis.get('1.0', 'end')

        if len(nom) > 0 and len(dur) > 0 and len(gen) > 0 and len(tipo) > 0 and len(dir) > 0 and len(act) > 0 and len(sin) > 0:
            self.pelicula.cargar_pelicula(self.bdd, nom, dur, gen, tipo, dir, act, sin)
            messagebox.showinfo('Aviso', 'Pelicula agregada exitosamente!')
            self.master.frame_pelicula.filtrar_input()
            self.cancelar()
        else:
            messagebox.showerror('Error', 'Debe rellenar todos los campos!')

    def cancelar(self):
        self.destroy()
        self.master.deiconify()