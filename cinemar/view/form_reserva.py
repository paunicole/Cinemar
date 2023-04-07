import tkinter as tk
from tkinter import ttk, Toplevel, messagebox
from model.funcion import Funcion
from model.reserva import Reserva
from model.descuento import Descuento
from model.pelicula import Pelicula
from model.tipo_pelicula import TipoPelicula

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
        self.nombre_pelicula = pelicula

        self.funcion = Funcion()
        self.pelicula = Pelicula()
        self.tipo_pelicula = TipoPelicula()
        self.ticket = Reserva()

        self.id_pelicula = self.pelicula.obtener_id(self.bdd, self.nombre_pelicula)
        self.peli = self.pelicula.obtener_pelicula(self.bdd, self.id_pelicula)
        self.funciones_peli = self.funcion.obtener_funciones_por_peli(self.bdd, self.id_pelicula)
        self.tipo = self.tipo_pelicula.obtener_tipo(self.bdd, self.peli[7])
        
        
        """FRAMES"""
        self.frame_fechas = tk.Frame(self)
        self.frame_entradas = tk.Frame(self)
        self.frame_butacas = tk.Frame(self)

        self.frame_cabecera1 = tk.Frame(self.frame_fechas)
        self.frame_datos1 = tk.Frame(self.frame_fechas)
        self.frame_botones1 = tk.Frame(self.frame_fechas)

        self.frame_cabecera2 = tk.Frame(self.frame_entradas)
        self.frame_datos2 = tk.Frame(self.frame_entradas)
        self.frame_botones2 = tk.Frame(self.frame_entradas)

        self.frame_cabecera3 = tk.Frame(self.frame_butacas)
        self.frame_datos3 = tk.Frame(self.frame_butacas)
        self.frame_botones3 = tk.Frame(self.frame_butacas)
        
        """WIDGETS"""
        #Titulo
        self.cabecera1 = ttk.Label(self.frame_cabecera1)
        self.cabecera2 = ttk.Label(self.frame_cabecera2)
        self.cabecera3 = ttk.Label(self.frame_cabecera3)

        #Labels
        self.label_comprador = ttk.Label(self.frame_datos1)
        self.label_pelicula = ttk.Label(self.frame_datos1)
        self.label_fecha = ttk.Label(self.frame_datos1) 
        self.label_formato = ttk.Label(self.frame_datos1)
        self.label_hora = ttk.Label(self.frame_datos1)

        self.label_entrada = ttk.Label(self.frame_datos2)
        self.label_precio = ttk.Label(self.frame_datos2)
        self.label_descuento = ttk.Label(self.frame_datos2)

        #Inputs
        self.input_comprador = ttk.Entry(self.frame_datos1)
        self.input_pelicula = ttk.Entry(self.frame_datos1)
        self.input_fecha = ttk.Combobox(self.frame_datos1)
        self.input_formato = ttk.Combobox(self.frame_datos1)
        self.input_hora = ttk.Combobox(self.frame_datos1)
        
        self.input_entrada = ttk.Combobox(self.frame_datos2)
        self.input_precio = ttk.Entry(self.frame_datos2)
        self.input_descuento = ttk.Entry(self.frame_datos2)

        #Botones
        self.button_continuar1 = ttk.Button(self.frame_botones1)
        self.button_cancelar1 = ttk.Button(self.frame_botones1)

        self.button_volver2 = ttk.Button(self.frame_botones2)
        self.button_continuar2 = ttk.Button(self.frame_botones2)
        self.button_cancelar2 = ttk.Button(self.frame_botones2)

        self.frames_config()
        self.frames_grid()

        self.widgets_config()
        self.widgets_grid()

        self.abrir_frame_fechas()


    def frames_config(self):
        self.frame_fechas.config(bg='black')
        self.frame_entradas.config(bg='black')
        self.frame_butacas.config(bg='black')

        """FRAME 1"""
        self.frame_cabecera1.config(border=15, bg='red')
        self.frame_datos1.config(bg='black')
        self.frame_botones1.config(bg='black')

        """FRAME 2"""
        self.frame_cabecera2.config(border=15, bg='red')
        self.frame_datos2.config(bg='black')
        self.frame_botones2.config(bg='black')

        """FRAME 3"""
        self.frame_cabecera3.config(border=15, bg='red')
        self.frame_datos3.config(bg='black')
        self.frame_botones3.config(bg='black')

    def frames_grid(self):
        self.frame_cabecera1.grid(row=0, column=0, rowspan=2, columnspan=3)
        self.frame_datos1.grid(row=2, column=0, rowspan=7, columnspan=3, pady=20)
        self.frame_botones1.grid(row=9, column=0, columnspan=3)

        self.frame_cabecera2.grid(row=0, column=0, rowspan=2, columnspan=3)
        self.frame_datos2.grid(row=2, column=0, rowspan=7, columnspan=3, pady=20)
        self.frame_botones2.grid(row=9, column=0, columnspan=3)

        self.frame_cabecera3.grid(row=0, column=0, rowspan=2, columnspan=3)
        self.frame_datos3.grid(row=2, column=0, rowspan=7, columnspan=3, pady=20)
        self.frame_botones3.grid(row=9, column=0, columnspan=3)

    def widgets_config(self):
        """FRAME 1"""
        self.input_insert()
        self.cabecera1.config(text='Completá los datos y reservá\ntu entrada', foreground='#FFFFFF', font=('Segoe UI Black', 25), background='red', justify='center')
        
        #Labels
        self.label_comprador.config(text='Comprador', foreground='#FFFFFF', font=('Segoe UI Black', 18), background='black')
        self.label_pelicula.config(text='Pelicula', foreground='#FFFFFF', font=('Segoe UI Black', 18), background='black')
        self.label_fecha.config(text='Fecha', foreground='#FFFFFF', font=('Segoe UI Black', 18), background='black')
        self.label_formato.config(text='Formato', foreground='#FFFFFF', font=('Segoe UI Black', 18), background='black')
        self.label_hora.config(text='Horario', foreground='#FFFFFF', font=('Segoe UI Black', 18), background='black')
        
        #Inputs
        self.input_comprador.config(width=30, state='readonly')
        self.input_pelicula.config(width=30, state='readonly')
        self.input_fecha.config(width=27, state='readonly')
        self.input_formato.config(width=27, state='readonly')
        self.input_hora.config(width=27, state='readonly')

        self.input_fecha.bind("<<ComboboxSelected>>", self.seleccion_fecha)
        self.input_formato.bind("<<ComboboxSelected>>", self.seleccion_formato)
        self.input_hora.bind("<<ComboboxSelected>>", self.seleccion_hora)

        self.button_continuar1.config(text='Continuar', command=self.abrir_frame_entradas)
        self.button_cancelar1.config(text='Cancelar', command=self.cancelar)

        """FRAME 2"""
        self.cabecera2.config(text='Completá los datos y reservá\ntu entrada', foreground='#FFFFFF', font=('Segoe UI Black', 25), background='red', justify='center')

        #Labels
        self.label_entrada.config(text='Entrada', foreground='#FFFFFF', font=('Segoe UI Black', 18), background='black')
        self.label_precio.config(text='Precio ($)', foreground='#FFFFFF', font=('Segoe UI Black', 18), background='black')
        self.label_descuento.config(text='Descuento (%)', foreground='#FFFFFF', font=('Segoe UI Black', 18), background='black')
        
        #Inputs
        self.input_entrada.config(width=27, state='readonly')
        self.input_precio.config(width=30, state='readonly')
        self.input_descuento.config(width=30, state='readonly')

        self.input_entrada.bind("<<ComboboxSelected>>", self.seleccion_entrada)

        self.button_volver2.config(text='Volver', command=self.abrir_frame_butacas)
        self.button_continuar2.config(text='Continuar', command=self.abrir_frame_butacas)
        self.button_cancelar2.config(text='Cancelar', command=self.cancelar)


    def widgets_grid(self):
        """FRAME 1"""
        self.cabecera1.grid(row=0, ipady=10)

        self.label_comprador.grid(row=0, column=0, padx=10, pady=10)
        self.input_comprador.grid(row=0, column=1, padx=10, pady=10)

        self.label_pelicula.grid(row=1, column=0, padx=10, pady=10)
        self.input_pelicula.grid(row=1, column=1, padx=10, pady=10)

        self.label_fecha.grid(row=2, column=0, padx=10, pady=10)
        self.input_fecha.grid(row=2, column=1, padx=10, pady=10)

        self.label_formato.grid(row=3, column=0, padx=10, pady=10)
        self.input_formato.grid(row=3, column=1, padx=10, pady=10)

        self.label_hora.grid(row=4, column=0, padx=10, pady=10)
        self.input_hora.grid(row=4, column=1, padx=10, pady=10)

        self.button_continuar1.grid(row=0, column=0, padx=20, pady=10, ipadx=5, ipady=5)
        self.button_cancelar1.grid(row=0, column=2, padx=20, pady=10, ipadx=5, ipady=5)

        """FRAME 2"""
        self.cabecera2.grid(row=0, ipady=10)

        self.label_entrada.grid(row=0, column=0, padx=10, pady=10)
        self.input_entrada.grid(row=0, column=1, padx=10, pady=10)

        self.label_precio.grid(row=1, column=0, padx=10, pady=10)
        self.input_precio.grid(row=1, column=1, padx=10, pady=10)

        self.label_descuento.grid(row=2, column=0, padx=10, pady=10)
        self.input_descuento.grid(row=2, column=1, padx=10, pady=10)

        self.button_volver2.grid(row=0, column=0, padx=20, pady=10, ipadx=5, ipady=5)
        self.button_continuar2.grid(row=0, column=1, padx=20, pady=10, ipadx=5, ipady=5)
        self.button_cancelar2.grid(row=0, column=2, padx=20, pady=10, ipadx=5, ipady=5)

    def input_insert(self):
        self.input_comprador.insert(0, self.comprador)
        self.input_pelicula.insert(0, self.nombre_pelicula)
        self.filtrar_fecha()
    
    def seleccion_fecha(self, event):
        self.filtrar_formato()
    
    def seleccion_formato(self, event):
        selec = self.input_fecha.get()
        self.filtrar_hora(selec)

    def seleccion_hora(self, event):
        selec = self.input_hora.get()

    def seleccion_entrada(self, event):
        entrada = self.input_entrada.get()
        self.input_insert_2(entrada)

    def filtrar_fecha(self):
        """Método que filtra una lista de todas las fechas de las funciones de una pelicula especifica, sin repetir."""
        fechas = []
        for funcion in self.funciones_peli:
            if funcion[1] not in fechas:
                fechas.append(funcion[1])
        self.input_fecha.config(values=fechas)
    
    def filtrar_formato(self):
        formatos = []
        for tipo in self.tipo:
            if tipo[1] not in formatos:
                formatos.append(tipo[1])
        self.input_formato.config(values=formatos)

    def filtrar_hora(self, fecha):
        """Método que filtra una lista de todas las horas de las funciones de una pelicula especifica, sin repetir."""
        horarios = []
        for funcion in self.funciones_peli:
            if funcion[1] == fecha:
                horarios.append(funcion[2])
        self.input_hora.config(values=horarios)
    
    def filtrar_entrada(self):
        entradas = [1, 2, 3, 4, 5, 6]
        self.input_entrada.config(values=entradas)

    def input_insert_2(self, entrada):
        self.input_precio.config(state='normal')
        self.input_precio.delete(0, 'end')
        self.input_precio.insert(0, f'{int(entrada) * 1500}')
        self.input_precio.config(state='readonly')

        self.input_descuento.insert(0, self.nombre_pelicula)

    def ocultar_frames(self):
        self.frame_fechas.grid_forget()
        self.frame_entradas.grid_forget()
        self.frame_butacas.grid_forget()

    def abrir_frame_fechas(self):
        self.ocultar_frames()
        self.frame_fechas.grid(row=0, column=0)

    def abrir_frame_entradas(self):
        self.filtrar_entrada()
        peli = self.input_pelicula.get()
        fecha = self.input_fecha.get()
        form = self.input_formato.get()
        hora = self.input_hora.get()

        if len(fecha) > 0 and len(form) and len(hora):
            if messagebox.askyesno('Atencion', f'SU SELECCIÓN: {peli} - {form}\n{fecha} {hora}Hs.\n\n¿Desea continuar?'):
                self.ocultar_frames()
                self.frame_entradas.grid(row=0, column=0)
        else:
            messagebox.showerror('Error en la reserva', 'Debe rellenar todos los campos')
    
    def abrir_frame_butacas(self):
        self.ocultar_frames()
        self.frame_butacas.grid(row=0, column=0)

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
            self.ticket = Reserva(None, comp, peli, butac, fecha, hora, precio)
            self.ticket.cargar_ticket(self.bdd)
            messagebox.showinfo('Aviso', 'Reserva realizada exitosamente!')
            self.master.frame_reserva.filtrar_tickets()
            self.cancelar()
        else:
            messagebox.showerror('Error', 'Debe rellenar todos los campos!')

    def cancelar(self):
        self.destroy()