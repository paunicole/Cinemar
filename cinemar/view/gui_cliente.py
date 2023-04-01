import tkinter as tk
from tkinter import Toplevel, messagebox

from view.frame_inicio import Inicio
from view.frame_perfil import Perfil
from view.frame_pelicula import PeliculaCliente
from view.frame_reservas import ReservaCliente

class Cliente(Toplevel):
    def __init__(self, master=None, cuenta_usuario=None, base_datos=None):
        Toplevel.__init__(self, master)
        self.master = master
        self.geometry('1080x720')
        self.config(bg='black')
        self.title('Sistema de Autogestión - Cinemar')
        self.iconbitmap('assets\logo.ico')
        self.protocol('WM_DELETE_WINDOW', self.logout)
        self.resizable(0, 0)

        self.cuenta_usuario = cuenta_usuario
        self.bdd = base_datos

        """FRAMES"""
        self.frame_principal = tk.Frame(self)
        self.frame_inicio = Inicio(self.frame_principal, 1)
        self.frame_perfil = Perfil(self.frame_principal, self.cuenta_usuario, self.bdd)
        self.frame_pelicula = PeliculaCliente(self, self.frame_principal, self.cuenta_usuario, self.bdd)
        self.frame_reserva = ReservaCliente(self.frame_principal, self.cuenta_usuario, self.bdd)

        """BOTONES PRINCIPALES - MENU"""
        self.button_inicio = tk.Button(self.frame_principal)
        self.button_perfil = tk.Button(self.frame_principal)
        self.button_pelicula = tk.Button(self.frame_principal)
        self.button_reserva = tk.Button(self.frame_principal)
        self.button_logout = tk.Button(self.frame_principal)

        self.frames_config()
        self.frame_principal.grid(row=0, column=0)
        self.menu_config()
        self.menu_grid()
        self.menu_inicio()

    def frames_config(self):
        self.frame_principal.config(bg='black')
        self.frame_inicio.config(bg='black')
        self.frame_perfil.config(bg='black')
        self.frame_pelicula.config(bg='black')
        self.frame_reserva.config(bg='black')

    def menu_config(self):
        self.button_inicio.config(text='INICIO', font=('Arial', 10, 'bold'), fg='white', bg='red', cursor='hand2', activebackground='tomato', command=self.menu_inicio)
        self.button_perfil.config(text='MI PERFIL', font=('Arial', 10, 'bold'), fg='white', bg='red', cursor='hand2', activebackground='tomato', command=self.menu_perfil)
        self.button_pelicula.config(text='PELICULAS', font=('Arial', 10, 'bold'), fg='white', bg='red', cursor='hand2', activebackground='tomato', command=self.menu_pelicula)
        self.button_reserva.config(text='MIS RESERVAS', font=('Arial', 10, 'bold'), fg='white', bg='red', cursor='hand2', activebackground='tomato', command=self.menu_reservas)
        self.button_logout.config(text='SALIR', font=('Arial', 10, 'bold'), fg='white', bg='red', cursor='hand2', activebackground='tomato', command=self.logout)
        
    def menu_grid(self):
        self.button_inicio.grid(row=0, column=1, ipadx=70, ipady=5)
        self.button_perfil.grid(row=0, column=2, ipadx=70, ipady=5)
        self.button_pelicula.grid(row=0, column=3, ipadx=70, ipady=5)
        self.button_reserva.grid(row=0, column=4, ipadx=70, ipady=5)
        self.button_logout.grid(row=0, column=5, ipadx=70, ipady=5)
        
    def menu_inicio(self):
        self.ocultar_frames()
        self.frame_inicio.grid(row=2, column=0, columnspan=8)

    def menu_perfil(self):
        self.ocultar_frames()
        self.frame_perfil.grid(row=2, column=0, columnspan=8)

    def menu_pelicula(self):
        self.ocultar_frames()
        self.frame_pelicula.grid(row=2, column=0, columnspan=8)

    def menu_reservas(self):
        self.ocultar_frames()
        self.frame_reserva.grid(row=2, column=0, columnspan=8)

    def ocultar_frames(self):
        self.frame_inicio.grid_forget()
        self.frame_perfil.grid_forget()
        self.frame_pelicula.grid_forget()
        self.frame_reserva.grid_forget()

    def logout(self):
        resultado = messagebox.askquestion("Salir", "¿Está seguro que desea salir?")
        if resultado == "yes":
            self.cuenta_usuario.cerrar_sesion()
            self.destroy()
            self.master.deiconify()