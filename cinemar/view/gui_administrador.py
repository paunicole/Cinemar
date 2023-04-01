import tkinter as tk
from tkinter import Toplevel, messagebox

from view.frame_inicio import Inicio
from view.frame_reservas import ReservaAdministrador
from view.frame_sala import SalaAdministrador
from view.frame_pelicula import PeliculaAdministrador
from view.frame_funciones import FuncionAdministrador
from view.frame_descuento import DescuentoAdministrador

class Administrador(Toplevel):
    def __init__(self, master=None, cuenta_usuario=None, base_datos=None):
        Toplevel.__init__(self, master)
        self.master = master
        self.geometry('1080x720')
        self.config(bg='black')
        self.title('Sistema de Autogestión - Cinemar')
        self.iconbitmap('assets\logo.ico')
        self.protocol('WM_DELETE_WINDOW', self.Logout)
        self.resizable(0, 0)

        self.cuenta_usuario = cuenta_usuario
        self.bdd = base_datos

        """FRAMES"""
        self.frame_principal = tk.Frame(self)
        self.frame_inicio = Inicio(self.frame_principal, 2)
        self.frame_descuento = DescuentoAdministrador(self.frame_principal, self.bdd)
        self.frame_pelicula = PeliculaAdministrador(self, self.frame_principal, self.bdd)
        self.frame_sala = SalaAdministrador(self.frame_principal, self.bdd)
        self.frame_funcion = FuncionAdministrador(self, self.frame_principal, self.bdd)
        self.frame_reserva = ReservaAdministrador(self.frame_principal, self.bdd)

        """BOTONES PRINCIPALES"""
        self.button_inicio = tk.Button(self.frame_principal)
        self.button_descuento = tk.Button(self.frame_principal)
        self.button_peliculas = tk.Button(self.frame_principal)
        self.button_salas = tk.Button(self.frame_principal)
        self.button_funciones = tk.Button(self.frame_principal)
        self.button_reservas = tk.Button(self.frame_principal)
        self.button_logout = tk.Button(self.frame_principal)

        self.frames_config()
        self.frame_principal.grid(row=0, column=0)
        self.menus_config()
        self.menus_grid()
        self.menu_inicio()
    

    def frames_config(self):
        self.frame_principal.config(bg='black')
        self.frame_inicio.config(bg='black')
        self.frame_descuento.config(bg='black')
        self.frame_pelicula.config(bg='black')
        self.frame_sala.config(bg='black')
        self.frame_funcion.config(bg='black')
        self.frame_reserva.config(bg='black')

    def menus_config(self):
        self.button_inicio.config(text='INICIO', font=('Arial', 10, 'bold'), fg='white', bg='red', cursor='hand2', activebackground='tomato', command=self.menu_inicio)
        self.button_descuento.config(text='DESCUENTOS', font=('Arial', 10, 'bold'), fg='white', bg='red', cursor='hand2', activebackground='tomato', command=self.menu_perfil)
        self.button_peliculas.config(text='PELICULAS', font=('Arial', 10, 'bold'), fg='white', bg='red', cursor='hand2', activebackground='tomato', command=self.menu_pelicula)
        self.button_salas.config(text='SALAS', font=('Arial', 10, 'bold'), fg='white', bg='red', cursor='hand2', activebackground='tomato', command=self.menu_sala)
        self.button_funciones.config(text='FUNCIONES', font=('Arial', 10, 'bold'), fg='white', bg='red', cursor='hand2', activebackground='tomato', command=self.menu_funcion)
        self.button_reservas.config(text='RESERVAS', font=('Arial', 10, 'bold'), fg='white', bg='red', cursor='hand2', activebackground='tomato', command=self.menu_reserva)
        self.button_logout.config(text='SALIR', font=('Arial', 10, 'bold'), fg='white', bg='red', cursor='hand2', activebackground='tomato', command=self.Logout)

    def menus_grid(self):
        self.button_inicio.grid(row=0, column=1, ipadx=13, ipady=5)
        self.button_descuento.grid(row=0, column=2, ipadx=40, ipady=5)
        self.button_peliculas.grid(row=0, column=3, ipadx=40, ipady=5)
        self.button_salas.grid(row=0, column=4, ipadx=40, ipady=5)
        self.button_funciones.grid(row=0, column=5, ipadx=40, ipady=5)
        self.button_reservas.grid(row=0, column=6, ipadx=40, ipady=5)
        self.button_logout.grid(row=0, column=7, ipadx=40, ipady=5)   

    def menu_inicio(self):
        self.ocultar_frames()
        self.frame_inicio.grid(row=2, column=0, columnspan=8)

    def menu_perfil(self):
        self.ocultar_frames()
        self.frame_descuento.grid(row=2, column=0, columnspan=8)

    def menu_pelicula(self):
        self.ocultar_frames()
        self.frame_pelicula.grid(row=2, column=0, columnspan=8)

    def menu_sala(self):
        self.ocultar_frames()
        self.frame_sala.grid(row=2, column=0, columnspan=8)

    def menu_funcion(self):
        self.ocultar_frames()
        self.frame_funcion.grid(row=2, column=0, columnspan=8)

    def menu_reserva(self):
        self.ocultar_frames()
        self.frame_reserva.grid(row=2, column=0, columnspan=8)

    def ocultar_frames(self):
        self.frame_inicio.grid_forget()
        self.frame_descuento.grid_forget()
        self.frame_pelicula.grid_forget()
        self.frame_sala.grid_forget()
        self.frame_funcion.grid_forget()
        self.frame_reserva.grid_forget()

    def Logout(self):
        resultado = messagebox.askquestion("Salir", "¿Está seguro que desea salir?")
        if resultado == "yes":
            self.cuenta_usuario.cerrar_sesion()
            self.destroy()
            self.master.deiconify()