import tkinter as tk
from tkinter import ttk, Toplevel, messagebox
from model.funcion import Funcion
from model.ticket import Ticket
from model.descuento import Descuento

class FormularioReserva(Toplevel):
    def __init__(self, master=None, comprador=None, pelicula=None, base_datos=None):
        Toplevel.__init__(self, master)
        self.master = master
        self.geometry('500x650')
        self.config(bg='black')
        self.title('Realiza tu Reserva')
        self.iconbitmap('assets\logo.ico')
        self.protocol('WM_DELETE_WINDOW', self.cancelar)
        self.resizable(0, 0)

        self.bdd = base_datos
        self.comprador = comprador
        self.pelicula = pelicula
        self.funcion = Funcion()
        self.funciones_peli = self.funcion.mostrar_por_pelicula(self.bdd, self.pelicula)
        self.ticket = Ticket()
        
        """FRAMES"""
        self.frame_cabecera = tk.Frame(self)
        self.frame_datos = tk.Frame(self)
        self.frame_botones = tk.Frame(self)
        
        """WIDGETS"""
        #Titulo
        self.cabecera = ttk.Label(self.frame_cabecera)
        
        #Labels
        self.label_comprador = ttk.Label(self.frame_datos)
        self.label_pelicula = ttk.Label(self.frame_datos)
        self.label_fecha = ttk.Label(self.frame_datos) 
        self.label_hora = ttk.Label(self.frame_datos)
        self.label_butaca = ttk.Label(self.frame_datos)
        self.label_precio = ttk.Label(self.frame_datos)
        self.label_descuento = ttk.Label(self.frame_datos)

        #Inputs
        self.input_comprador = ttk.Entry(self.frame_datos)
        self.input_pelicula = ttk.Entry(self.frame_datos)
        self.input_fecha = ttk.Combobox(self.frame_datos)
        self.input_hora = ttk.Combobox(self.frame_datos)
        self.input_butaca = ttk.Combobox(self.frame_datos)
        self.input_precio = ttk.Entry(self.frame_datos)
        self.input_descuento = ttk.Entry(self.frame_datos)
        
        #Botones
        self.button_reservar = ttk.Button(self.frame_botones)
        self.button_cancelar = ttk.Button(self.frame_botones)

        self.frames_config()
        self.frames_grid()

        self.widgets_config()
        self.widgets_grid()


    def frames_config(self):
        self.frame_cabecera.config(border=15, bg='red')
        self.frame_datos.config(bg='black')
        self.frame_botones.config(bg='black')
    
    def frames_grid(self):
        self.frame_cabecera.grid(row=0, column=0, rowspan=2, columnspan=3)
        self.frame_datos.grid(row=2, column=0, rowspan=7, columnspan=3, pady=20)
        self.frame_botones.grid(row=9, column=0, columnspan=3)

    def widgets_config(self):
        self.input_insert()

        self.cabecera.config(text='Completá los datos y reservá\ntu entrada', foreground='#FFFFFF', font=('Segoe UI Black', 25), background='red', justify='center')
        
        #Labels
        self.label_comprador.config(text='Comprador', foreground='#FFFFFF', font=('Segoe UI Black', 18), background='black')
        self.label_pelicula.config(text='Pelicula', foreground='#FFFFFF', font=('Segoe UI Black', 18), background='black')
        self.label_fecha.config(text='Fecha', foreground='#FFFFFF', font=('Segoe UI Black', 18), background='black')
        self.label_hora.config(text='Horario', foreground='#FFFFFF', font=('Segoe UI Black', 18), background='black')
        self.label_butaca.config(text='Cantidad de Butacas', foreground='#FFFFFF', font=('Segoe UI Black', 18), background='black')
        self.label_precio.config(text='Precio ($)', foreground='#FFFFFF', font=('Segoe UI Black', 18), background='black')
        self.label_descuento.config(text='Descuento (%)', foreground='#FFFFFF', font=('Segoe UI Black', 18), background='black')

        #Inputs
        self.input_comprador.config(width=30, state='readonly')
        self.input_pelicula.config(width=30, state='readonly')
        self.input_fecha.config(width=27, state='readonly')
        self.input_hora.config(width=27, state='readonly')
        self.input_butaca.config(width=27, state='readonly')
        self.input_precio.config(width=30, state='readonly')
        self.input_descuento.config(width=30, state='readonly')

        self.input_fecha.bind("<<ComboboxSelected>>", self.seleccion_fecha)
        self.input_hora.bind("<<ComboboxSelected>>", self.seleccion_hora)
        self.input_butaca.bind("<<ComboboxSelected>>", self.seleccion_butaca)

        self.button_reservar.config(text='Reservar', command=self.reservar)
        self.button_cancelar.config(text='Cancelar', command=self.cancelar)

    def widgets_grid(self):
        self.cabecera.grid(row=0, ipady=10)

        self.label_comprador.grid(row=0, column=0, padx=10, pady=10)
        self.input_comprador.grid(row=0, column=1, padx=10, pady=10)

        self.label_pelicula.grid(row=1, column=0, padx=10, pady=10)
        self.input_pelicula.grid(row=1, column=1, padx=10, pady=10)

        self.label_fecha.grid(row=2, column=0, padx=10, pady=10)
        self.input_fecha.grid(row=2, column=1, padx=10, pady=10)

        self.label_hora.grid(row=3, column=0, padx=10, pady=10)
        self.input_hora.grid(row=3, column=1, padx=10, pady=10)

        self.label_butaca.grid(row=4, column=0, padx=10, pady=10)
        self.input_butaca.grid(row=4, column=1, padx=10, pady=10)

        self.label_precio.grid(row=5, column=0, padx=10, pady=10)
        self.input_precio.grid(row=5, column=1, padx=10, pady=10)

        self.label_descuento.grid(row=6, column=0, padx=10, pady=10)
        self.input_descuento.grid(row=6, column=1, padx=10, pady=10)

        self.button_reservar.grid(row=0, column=0, padx=20, pady=10, ipadx=5, ipady=5)
        self.button_cancelar.grid(row=0, column=2, padx=20, pady=10, ipadx=5, ipady=5)

    def input_insert(self):
        self.input_comprador.insert(0, self.comprador)
        self.input_pelicula.insert(0, self.pelicula)
        self.input_descuento.insert(0, '0')
        self.input_precio.insert(0, '0.00')
        self.filtrar_fecha()
    
    def seleccion_fecha(self, event):
        opc = self.input_fecha.get()
        self.filtrar_hora(opc)
    
    def seleccion_hora(self, event):
        opc = self.input_hora.get()
        self.filtrar_butaca(self.input_fecha.get(), opc)
    
    def seleccion_butaca(self, event):
        opc = self.input_butaca.get()
        self.filtrar_descuento()
        self.filtrar_precio(self.input_fecha.get(), self.input_hora.get(), opc)

    def filtrar_fecha(self):
        """Método que filtra una lista de todas las fechas de las funciones de una pelicula especifica, sin repetir."""
        fechas = []
        for i in range(len(self.funciones_peli)):
            if self.funciones_peli[i][4] not in fechas:
                fechas.append(self.funciones_peli[i][4])
        self.input_fecha.config(values=fechas)
    
    def filtrar_hora(self, fecha):
        """Método que filtra una lista de todas las horas de las funciones de una pelicula especifica, sin repetir."""
        horarios = []
        for i in range(len(self.funciones_peli)):
            if self.funciones_peli[i][4] == fecha:
                horarios.append(self.funciones_peli[i][5])
        self.input_hora.config(values=horarios)
    
    def filtrar_butaca(self, fecha, hora):
        """Método que filtra una lista de todas las butacas de la funcion de la fecha y hora pasadas por parametro."""
        butacas = []
        for i in range(len(self.funciones_peli)):
            if self.funciones_peli[i][4] == fecha and self.funciones_peli[i][5] == hora:
                cant = self.funciones_peli[i][3]
        for i in range(1, cant+1):
            butacas.append(i)
        self.input_butaca.config(values=butacas)

    def filtrar_precio(self, fecha, hora, butac):
        """Método que filtra el precio total de la funcion de la fecha y hora pasadas por parametro,
        teniendo en cuenta al cantidad de butacas compradas."""
        i = 0
        while self.funciones_peli[i][4] != fecha and self.funciones_peli[i][5] != hora:
            i += 1
        precio = int(self.funciones_peli[i][6]) * int(butac)
        desc = int(self.input_descuento.get())
        precio -= ((desc/100) * precio)
        self.input_precio.config(state='normal')
        self.input_precio.delete(0, 'end')
        self.input_precio.insert(0, f'{precio}')
        self.input_precio.config(state='readonly')

    def filtrar_descuento(self):
        """Método que filtra."""
        desc = Descuento().aplica_descuento(self.bdd, self.comprador, self.input_fecha.get())
        if desc > 0:
            messagebox.showinfo('Recompensa', f'Felicidades!\n\nPor venir al cine más de 5 veces en 3 meses, tenés como recompensa un descuento en tus entradas ({desc}%)\n\nGracias por elegirnos!')
        self.input_descuento.config(state='normal')
        self.input_descuento.delete(0, 'end')
        self.input_descuento.insert(0, f'{desc}')
        self.input_descuento.config(state='readonly')
        
    def reservar(self):
        comp = self.input_comprador.get()
        peli = self.input_pelicula.get()
        butac = self.input_butaca.get()
        fecha = self.input_fecha.get()
        hora = self.input_hora.get()
        precio = self.input_precio.get()

        if len(butac) > 0 and len(fecha) > 0 and len(hora) > 0:
            i = 0
            while i < len(self.funciones_peli):
                if self.funciones_peli[i][4] == fecha and self.funciones_peli[i][5] == hora:
                    break
                i += 1
            funcion = self.funciones_peli[i]
            self.funcion.modificar_funcion(self.bdd, funcion[0], butacas_libres=int(funcion[3]) - int(butac))
            self.ticket = Ticket(None, comp, peli, butac, fecha, hora, precio)
            self.ticket.cargar_ticket(self.bdd)
            messagebox.showinfo('Aviso', 'Reserva realizada exitosamente!')
            self.master.frame_reserva.filtrar_tickets()
            self.cancelar()
        else:
            messagebox.showerror('Error', 'Debe rellenar todos los campos!')

    def cancelar(self):
        self.destroy()