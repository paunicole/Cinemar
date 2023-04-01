import tkinter as tk
from tkinter import ttk, messagebox, Toplevel
from model.cuenta import Cuenta

class FormularioRegistro(Toplevel):
    def __init__(self, master=None, base_datos=None):
        Toplevel.__init__(self, master)
        self.master = master
        self.geometry('418x700')
        self.config(bg='black')
        self.title('Registro')
        self.iconbitmap('assets\logo.ico')
        self.protocol('WM_DELETE_WINDOW', self.Cancelar)
        self.resizable(0, 0)

        self.bdd = base_datos
        self.cuenta = Cuenta()
        
        """FRAMES"""
        self.frame_cabecera = tk.Frame(self)
        self.frame_persona = tk.Frame(self)
        self.frame_cuenta = tk.Frame(self)
        self.frame_botones = tk.Frame(self)

        """WIDGETS"""
        #Titulo - Principal
        self.cabecera = ttk.Label(self.frame_cabecera)
        #Titulo - Datos de la Persona
        self.cabecera_persona = ttk.Label(self.frame_persona)
        #Titulo - Datos de la Cuenta
        self.cabecera_cuenta = ttk.Label(self.frame_cuenta)
        #Apellido
        self.label_apellido = ttk.Label(self.frame_persona)
        self.input_apellido = ttk.Entry(self.frame_persona)
        #Nombre
        self.label_nombre = ttk.Label(self.frame_persona)
        self.input_nombre = ttk.Entry(self.frame_persona)
        #DNI
        self.label_dni = ttk.Label(self.frame_persona)
        self.input_dni = ttk.Entry(self.frame_persona)
        #Correo Electronico
        self.label_mail = ttk.Label(self.frame_persona)
        self.input_mail = ttk.Entry(self.frame_persona)
        #Telefono
        self.label_telefono = ttk.Label(self.frame_persona)
        self.input_telefono = ttk.Entry(self.frame_persona)
        #Usuario
        self.label_usuario = ttk.Label(self.frame_cuenta)
        self.input_usuario = ttk.Entry(self.frame_cuenta)
        #Contraseña
        self.label_password = ttk.Label(self.frame_cuenta)
        self.input_password = ttk.Entry(self.frame_cuenta)
        #Botones
        self.button_registrar = ttk.Button(self.frame_botones)
        self.button_cancelar = ttk.Button(self.frame_botones)

        self.frames_config()
        self.frames_grid()

        self.widgets_config()
        self.widgets_grid()

        

    def frames_config(self):
        self.frame_cabecera.config(border=15, bg='red')
        self.frame_persona.config(bg='black')
        self.frame_cuenta.config(bg='black')
        self.frame_botones.config(bg='black')

    def frames_grid(self):
        self.frame_cabecera.grid(row=0, column=0, columnspan=2)
        self.frame_persona.grid(row=1, column=0, columnspan=2, pady=20)
        self.frame_cuenta.grid(row=2, column=0, columnspan=2, pady=20)
        self.frame_botones.grid(row=3, column=0, columnspan=2)

    def widgets_config(self):
        #Titulos cabecera
        self.cabecera.config(text='Ingresá tus datos y creá\ntu cuenta ', foreground='#FFFFFF', font=('Segoe UI Black', 25), background='red', justify='center')
        self.cabecera_persona.config(text='Datos Personales', foreground='#FFFFFF', font=('Segoe UI Black', 24), background='blue')
        self.cabecera_cuenta.config(text='Cuenta de Usuario', foreground='#FFFFFF', font=('Segoe UI Black', 24), background = 'blue')
        
        #Labels
        self.label_apellido.config(text='Apellido', foreground='#FFFFFF', font=('Segoe UI Black', 14), background='black')
        self.label_nombre.config(text='Nombre', foreground='#FFFFFF', font=('Segoe UI Black', 14), background='black')        
        self.label_dni.config(text='DNI', foreground='#FFFFFF', font=('Segoe UI Black', 14), background='black')
        self.label_mail.config(text='Correo Electrónico', foreground='#FFFFFF', font=('Segoe UI Black', 14), background='black')
        self.label_telefono.config(text='Telefono', foreground= '#FFFFFF', font=('Segoe UI Black', 14), background='black')
        self.label_usuario.config(text='Usuario', foreground='#FFFFFF', font=('Segoe UI Black', 14), background='black')
        self.label_password.config(text='Contraseña', foreground='#FFFFFF', font=('Segoe UI Black', 14), background='black')

        #Inputs
        self.input_apellido.config(width=30)
        self.input_nombre.config(width=30)
        self.input_dni.config(width=30)
        self.input_mail.config(width=30)       
        self.input_telefono.config(width=30)
        self.input_usuario.config(width=30)
        self.input_password.config(width=30)

        #Botones
        self.button_registrar.config(text='Registrarse', command=self.Registrarse)
        self.button_cancelar.config(text='Cancelar', command=self.Cancelar)

    def widgets_grid(self):
        self.cabecera.grid(row=0, ipady=10)
        self.cabecera_persona.grid(row=0, column=0, columnspan=2)
        self.cabecera_cuenta.grid(row=0, column=0)

        #Datos de Persona
        self.label_apellido.grid(row=1, column=0, pady=5)
        self.label_nombre.grid(row=1, column=1, pady=5)

        self.input_apellido.grid(row=2, column=0, padx=10)
        self.input_nombre.grid(row=2, column=1, padx=10)

        self.label_dni.grid(row=3, column=0, pady=5)
        self.label_mail.grid(row=3, column=1, pady=5)

        self.input_dni.grid(row=4, column=0, padx=10)
        self.input_mail.grid(row=4, column=1, padx=10)

        self.label_telefono.grid(row=5, column=0, columnspan=2, pady=5)
        self.input_telefono.grid(row=6, column=0, columnspan=2)
        
        #Datos de Cuenta
        self.label_usuario.grid(row=1, column=0, pady=5)
        self.input_usuario.grid(row=2, column=0, padx=10)

        self.label_password.grid(row=3, column=0, pady=5)
        self.input_password.grid(row=4, column=0, padx=10)
       
        #Botones
        self.button_registrar.grid(row=5, column=0, padx=10, pady=10, ipadx=5, ipady=5)
        self.button_cancelar.grid(row=5, column=1, padx=10, pady=10, ipadx=5, ipady=5)

    def Registrarse(self):
        ap = self.input_apellido.get()
        nom = self.input_nombre.get()
        dni = self.input_dni.get()
        email = self.input_mail.get()
        tel = self.input_telefono.get()
        us = self.input_usuario.get()
        pas = self.input_password.get()

        if len(ap) > 0 and len(nom) > 0 and len(dni) > 0 and len(email) > 0 and len(tel) > 0 and len(us) > 0 and len(pas) > 0:
            mensaje = self.cuenta.registrarse(self.bdd, ap, nom, dni, email, tel, us, pas)
            messagebox.showinfo('Aviso', mensaje)
            if mensaje == 'Cuenta registrada exitosamente!':
                self.Cancelar()
        else:
            messagebox.showerror('Error', 'Debe rellenar todos los campos!')

    def Cancelar(self):
        self.destroy()
        self.master.deiconify()