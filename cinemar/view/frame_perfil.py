import tkinter as tk
from tkinter import ttk

class Perfil(tk.Frame):
    def __init__(self, master=None, cuenta_usuario=None, base_datos=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.cuenta_usuario = cuenta_usuario
        self.bdd = base_datos

        """WIDGETS"""
        #Labels
        self.label_titulo = ttk.Label(self)
        self.label_apellido = ttk.Label(self)
        self.label_nombre = ttk.Label(self)
        self.label_dni = ttk.Label(self)
        self.label_mail = ttk.Label(self)
        self.label_telefono = ttk.Label(self)
        self.label_usuario = ttk.Label(self)
        self.label_password = ttk.Label(self)

        #Entrys
        self.input_apellido = ttk.Entry(self)
        self.input_nombre = ttk.Entry(self)
        self.input_dni = ttk.Entry(self)
        self.input_email = ttk.Entry(self)
        self.input_telefono = ttk.Entry(self)
        self.input_usuario = ttk.Entry(self)
        self.input_password = ttk.Entry(self)
        
        #Botones
        self.button_ver_contrasena = ttk.Button(self)
        self.button_ocultar_contrasena = ttk.Button(self)

        self.widgets_config()
        self.widgets_grid()

    def widgets_config(self):
        #Labels
        self.label_titulo.config(text='Datos Personales', foreground='#FFFFFF', font=('Segoe UI Black', 36), background='red', justify='center')
        self.label_apellido.config(text='Apellido', foreground='#FFFFFF', font=('Segoe UI Black', 18), background='black')
        self.label_nombre.config(text='Nombre', foreground='#FFFFFF', font=('Segoe UI Black', 18), background='black')
        self.label_dni.config(text='DNI', foreground='#FFFFFF', font=('Segoe UI Black', 18), background = 'black')
        self.label_mail.config(text='Correo Electrónico', foreground='#FFFFFF', font=('Segoe UI Black', 18), background='black')
        self.label_telefono.config(text='Telefono', foreground='#FFFFFF', font=('Segoe UI Black', 18), background='black')
        self.label_usuario.config(text='Usuario', foreground='#FFFFFF', font=('Segoe UI Black', 18), background='black')
        self.label_password.config(text='Contraseña', foreground='#FFFFFF', font=('Segoe UI Black', 18), background='black')
        #Inputs
        self.input_insert()
        self.input_apellido.config(width=30, state="readonly")
        self.input_nombre.config(width=30, state="readonly")
        self.input_dni.config(width=30, state="readonly")
        self.input_email.config(width=30, state="readonly")
        self.input_telefono.config(width=30, state="readonly")
        self.input_usuario.config(width=30, state="readonly")
        self.input_password.config(width=30, state='readonly', show='*')
        #Botones
        self.button_ver_contrasena.config(text='Mostrar Contraseña', command=self.ver_contrasena)
        self.button_ocultar_contrasena.config(text='Ocultar contraseña', command=self.ocultar_contrasena)

        
    def input_insert(self):
        self.input_apellido.insert(0, self.cuenta_usuario.apellido)
        self.input_nombre.insert(0, self.cuenta_usuario.nombre)
        self.input_dni.insert(0, self.cuenta_usuario.dni)
        self.input_email.insert(0, self.cuenta_usuario.email)
        self.input_telefono.insert(0, self.cuenta_usuario.telefono)
        self.input_usuario.insert(0, self.cuenta_usuario.usuario)
        self.input_password.insert(0, self.cuenta_usuario.password)

    def widgets_grid(self):
        #Labels
        self.label_titulo.grid(row=0, column=0, columnspan=2, pady=20, ipady=10)
        self.label_apellido.grid(row=1, column=0, pady=5)
        self.label_nombre.grid(row=2, column=0, pady=5)
        self.label_dni.grid(row=3, column=0, pady=5)
        self.label_mail.grid(row=4, column=0, pady=5)
        self.label_telefono.grid(row=5, column=0, pady=5)
        self.label_usuario.grid(row=6, column=0, pady=5)
        self.label_password.grid(row=7, column=0, pady=5)
        #Inputs
        self.input_apellido.grid(row=1, column=1, padx=20)
        self.input_nombre.grid(row=2, column=1, padx=20)
        self.input_dni.grid(row=3, column=1, padx=20)
        self.input_email.grid(row=4, column=1, padx=20)
        self.input_telefono.grid(row=5, column=1, padx=20)
        self.input_usuario.grid(row=6, column=1, padx=20)
        self.input_password.grid(row=7, column=1, padx=20)
        #Botones
        self.button_ver_contrasena.grid(row=8, column=0, columnspan=2, pady=20, padx=10, ipady=5, ipadx=5)

    def ver_contrasena(self):
        self.input_password.config(show = '')
        self.button_ver_contrasena.grid_forget()
        self.button_ocultar_contrasena.grid(row=8, column=0, columnspan=2, pady=20, padx=10, ipady=5, ipadx=5)
    
    def ocultar_contrasena(self):
        self.input_password.config(show='*')
        self.button_ocultar_contrasena.grid_forget()
        self.button_ver_contrasena.grid(row=8, column=0, columnspan=2, pady=20, padx=10, ipady=5, ipadx=5)