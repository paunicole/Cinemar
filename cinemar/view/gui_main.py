import tkinter as tk
from tkinter import ttk, messagebox
from model.cuenta import Cuenta
from view.form_registro import FormularioRegistro
from view.gui_administrador import Administrador
from view.gui_cliente import Cliente

class Main(tk.Tk):
    def __init__(self, base_datos=None):
        tk.Tk.__init__(self)
        self.geometry('645x450')
        self.config(bg='black')
        self.title('Cinemar')
        self.iconbitmap('assets\logo.ico')
        self.resizable(0, 0)

        self.bdd = base_datos
        self.cuenta = Cuenta()

        """IMAGENES"""
        self.img_cine = tk.PhotoImage(file="assets\main.png")
        self.img_cine = self.img_cine.subsample(7)

        """FRAMES"""
        self.frame_cabecera = tk.Frame(self)
        self.frame_login = tk.Frame(self)
        self.frame_registro = tk.Frame(self)

        """WIDGETS"""
        self.cabecera = ttk.Label(self.frame_cabecera)

        self.label_login = ttk.Label(self.frame_login)
        self.label_usuario = ttk.Label(self.frame_login)
        self.entry_usuario = ttk.Entry(self.frame_login)
        self.label_password = ttk.Label(self.frame_login)
        self.entry_password = ttk.Entry(self.frame_login)

        self.img_deco = tk.Label(self.frame_registro)
        self.label_registro = ttk.Label(self.frame_registro)

        self.button_login = ttk.Button(self.frame_login)
        self.button_registrarse = ttk.Button(self.frame_registro)

        self.frames_settings()
        self.frames_grid()
        
        self.widgets_settings()
        self.widgets_grid()

    def frames_settings(self):
        self.frame_cabecera.config(border=5, background='#FFFFFF')
        self.frame_login.config(border=20, bg='black')
        self.frame_registro.config(border=20, bg='black')
    
    def frames_grid(self):
        self.frame_cabecera.grid(row=0, column=0, columnspan=3, pady=20)
        self.frame_login.grid(row=1, column=0)
        self.frame_registro.grid(row=1, column=2)
    
    def widgets_settings(self):
        self.cabecera.config(text='Bienvenid@ a Cinemar', foreground='#FFFFFF', font=('Segoe UI Black', 40), background='red')
        
        self.label_login.config(text='Inicio de Sesión', foreground='#FFFFFF', font=('Segoe UI Black', 15), background='red', justify='center')
        self.label_usuario.config(text='Usuario', foreground='#FFFFFF', font=('Segoe UI Black', 12), background='black')
        self.label_password.config(text='Contraseña', foreground='#FFFFFF', font=('Segoe UI Black', 12), background='black')
        self.label_registro.config(text='¿Todavia no tenés una cuenta? Create una', foreground='#FFFFFF', font=('Segoe UI Black', 12), background='black')  
        
        self.entry_usuario.config(width=20)
        self.entry_usuario.focus()
        self.entry_password.config(width=20, show='*')
        
        self.img_deco.config(image=self.img_cine)
        
        self.button_login.config(text='Ingresar', command=self.login)
        self.bind('<Return>', lambda e: self.button_login.invoke())
        self.button_registrarse.config(text='Registrate', command=self.registrar)

    def widgets_grid(self):
        self.cabecera.grid(padx=0, ipady=5)
        self.label_login.grid(row=0, ipady=10, pady=10, padx=30)
        self.label_usuario.grid(row=1, column=0, pady=5)
        self.entry_usuario.grid(row=2, column=0)
        self.label_password.grid(row=3, column=0, pady=5)
        self.entry_password.grid(row=4, column=0)
        self.img_deco.grid(row=0, column=0, pady=20)
        self.label_registro.grid()
        self.button_login.grid(ipady=5, ipadx=5, pady=30)
        self.button_registrarse.grid(ipady=5, ipadx=5, pady=10)

    def login(self):
        usuario = self.entry_usuario.get()
        password = self.entry_password.get()

        if len(usuario) > 0 and len(password) > 0:
            mensaje = self.cuenta.iniciar_sesion(self.bdd, usuario, password)
            
            if mensaje == 'Inicio de sesión exitoso!':
                self.entry_usuario.delete(0, 'end')
                self.entry_password.delete(0, 'end')
                self.withdraw()

                if self.cuenta.admin == 'cliente':
                    ventana = Cliente(self, self.cuenta, self.bdd)
                else:
                    ventana = Administrador(self, self.cuenta, self.bdd)

                ventana.mainloop()
            else:
                messagebox.showerror('Error', mensaje)
        else:
            messagebox.showerror('Error', 'Debe rellenar todos los campos!')
    
    def registrar(self):
        self.withdraw()
        ventana = FormularioRegistro(self, self.bdd)
        ventana.mainloop()