import tkinter as tk
from tkinter import IntVar, ttk
from model.reserva import Reserva
from model.funcion import Funcion
from model.butaca import Butaca

class Ubicacion(tk.Frame):
    def __init__(self, ventana_padre=None, master=None, cuenta_usuario=None, base_datos=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.ventana_padre = ventana_padre
        self.cuenta_usuario = cuenta_usuario
        self.bdd = base_datos
        self.reserva = Reserva()
        self.reserva = self.reserva.tickets_comprador(self.bdd, self.cuenta_usuario.dni)
        self.reserva = self.reserva[-1]
        self.funcion = Funcion()
        self.sala = self.funcion.devolver_sala(self.bdd, self.reserva[2], self.reserva[4], self.reserva[5])
        self.sala = list(self.sala)
        self.sala = self.sala[0]
        print(self.sala)
        self.butacas = Butaca()
        self.butacas = self.butacas.devolver_butacas_por_sala(self.bdd, self.sala)
        print(self.butacas)

        """FRAMES"""
        self.frame_principal = tk.Frame(self)
        self.frame_asientos = tk.Frame(self.frame_principal)

        """WIDGETS"""
        #Titulo
        self.cabecera = ttk.Label(self.frame_principal)

        #Reservar
        self.label_reservar = ttk.Label(self.frame_principal)
        self.button_reservar = ttk.Button(self.frame_principal)

        self.frames_config()
        self.frames_grid()

        self.widgets_config()
        self.widgets_grid()

    def frames_config(self):

        filas = 2
        columnas = 9
        cant_butacas = len(self.butacas)
        letras = 'ABCDEFGHIJKLMN'
        cont = 1
        self.valor = IntVar()
        for i in range(filas):
            #Letra
            letra = tk.Label(self.frame_asientos, text=letras[i], font='Arial')
            letra.grid(row=i, column=0, padx=5, pady=5)
            #Asientos
            for j in range(1, columnas+1):
                a = letras[i] + str(cont)
                butaca = tk.Checkbutton(self.frame_asientos,
                                    text=f"{cont}",
                                    variable=self.valor,
                                    bd=3,
                                    font='Arial',
                                    width=3,
                                    selectcolor='yellow',
                                    onvalue=a,
                                    offvalue=0,
                                    indicatoron=False,
                                    command=self.seleccion)
                if self.butacas[cont-1][3] == 'Si':
                    butaca.config(selectcolor='red', fg='black', state='disabled')
                    butaca.select()
                butaca.grid(row=i, column=j, padx=5, pady=5)
                cont += 1
            #Letra
            letra = tk.Label(self.frame_asientos, text=letras[i], font='Arial')
            letra.grid(row=i, column=j+1, padx=5, pady=5)

    def frames_grid(self):
        self.frame_principal.grid(row=0, column=0, padx=30, pady=30)
        self.frame_asientos.grid(row=1, column=0)

    def widgets_config(self):
        self.cabecera.config(text='Elegí tus butacas', foreground='#FFFFFF', font=('Segoe UI Black', 18), background='black', justify='center')

        self.label_reservar.config(text='Por ultimo reserva', foreground='#FFFFFF', font=('Segoe UI Black', 18), background='black', justify='center')
        self.button_reservar.config(text='Reservar', command=self.reservar)

    def widgets_grid(self):
        #Titulo
        self.cabecera.grid(row=0, column=0, padx=20, pady=20)

        #Reservar
        self.label_reservar.grid(row=4, column=0, padx=20, pady=20)
        self.button_reservar.grid(row=5, column=0, padx=5, pady=5, ipadx=5, ipady=5)
    
    def seleccion(self):
        print(self.valor.get())

    def reservar():
        pass