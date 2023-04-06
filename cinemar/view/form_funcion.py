import tkinter as tk
from tkinter import ttk, Toplevel, messagebox
from model.funcion import Funcion
from model.pelicula import Pelicula
from model.sala import Sala

class FormularioFuncion(Toplevel):
    def __init__(self, master=None, base_datos=None):
        Toplevel.__init__(self, master)
        self.master = master
        self.geometry('358x550')
        self.config(bg='black')
        self.title('Agregar Función')
        self.iconbitmap('assets\logo.ico')
        self.protocol('WM_DELETE_WINDOW', self.cancelar)
        self.resizable(0,0)

        self.bdd = base_datos
        self.funcion = Funcion()
        self.pelicula = Pelicula()
        self.sala = Sala()
        
        """FRAMES"""
        self.frame_cabecera = tk.Frame(self)
        self.frame_datos = tk.Frame(self)
        self.frame_botones = tk.Frame(self)

        """WIDGETS"""
        #Titulo
        self.cabecera = ttk.Label(self.frame_cabecera)

        #Labels
        self.label_sala = ttk.Label(self.frame_datos)
        self.label_peli = ttk.Label(self.frame_datos)
        self.label_butaca = ttk.Label(self.frame_datos)
        self.label_fecha = ttk.Label(self.frame_datos)
        self.label_hora = ttk.Label(self.frame_datos)
        self.label_precio = ttk.Label(self.frame_datos)

        #Inputs
        self.input_sala = ttk.Combobox(self.frame_datos)
        self.input_peli = ttk.Combobox(self.frame_datos)
        self.input_butaca = ttk.Entry(self.frame_datos)
        self.input_feha = ttk.Entry(self.frame_datos)
        self.input_hora = ttk.Entry(self.frame_datos)
        self.input_precio = ttk.Entry(self.frame_datos)

        #Buttons
        self.button_cargar = ttk.Button(self.frame_botones)
        self.button_editar = ttk.Button(self.frame_botones)

        self.filtrar_peli()
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
        self.frame_datos.grid(row=2, column=0, rowspan=5, columnspan=3, pady=20)
        self.frame_botones.grid(row=7, column=0, columnspan=3)

    def widgets_config(self):
        #Titulo
        self.cabecera.config(text='Ingresá los datos de\nla nueva función', foreground='#FFFFFF', font=('Segoe UI Black', 25), background='red', justify='center')
        
        #Labels
        self.label_sala.config(text='Sala', foreground='#FFFFFF', font=('Segoe UI Black', 18), background='black')
        self.label_peli.config(text='Pelicula', foreground='#FFFFFF', font=('Segoe UI Black', 18), background='black')        
        self.label_butaca.config(text='Butacas', foreground='#FFFFFF', font=('Segoe UI Black', 18), background='black')
        self.label_fecha.config(text='Fecha', foreground='#FFFFFF', font=('Segoe UI Black', 18), background='black')
        self.label_hora.config(text='Horario', foreground='#FFFFFF', font=('Segoe UI Black', 18), background='black')
        self.label_precio.config(text='Precio ($)', foreground='#FFFFFF', font=('Segoe UI Black', 18), background='black')

        #Inputs
        self.input_sala.config(width=7, state='readonly')
        self.input_peli.config(width=27, state='readonly')
        self.input_butaca.config(width = 10, state = 'readonly')
        self.input_feha.config(width=30)
        self.input_hora.config(width=30)
        self.input_precio.config(width=10)

        self.input_sala.bind("<<ComboboxSelected>>", self.selected_sala)
        self.input_peli.bind("<<ComboboxSelected>>", self.selected_peli)

        #Buttons
        self.button_cargar.config(text='Cargar Datos', command=self.cargar)
        self.button_editar.config(text='Cancelar', command=self.cancelar)

    def widgets_grid(self):
        #Titulo
        self.cabecera.grid(row=0, ipady=10)
        #Sala
        self.label_sala.grid(row=0, column=2, padx=10, pady=10)
        self.input_sala.grid(row=1, column=2, padx=10, pady=10)
        #Pelicula
        self.label_peli.grid(row=0, column=0, padx=10, pady=10)
        self.input_peli.grid(row=1, column=0, padx=10, pady=10)
        #Butacas Disponibles
        self.label_butaca.grid(row=2, column=2, padx=10, pady=10)
        self.input_butaca.grid(row=3, column=2, padx=10, pady=10)
        #Fecha
        self.label_fecha.grid(row=2, column=0, padx=10, pady=10)
        self.input_feha.grid(row=3, column=0, padx=10, pady=10)
        #Horario
        self.label_hora.grid(row=4, column=0, padx=10, pady=10)
        self.input_hora.grid(row=5, column=0, padx=10, pady=10)
        #Precio
        self.label_precio.grid(row=4, column=2, padx=10, pady=10)
        self.input_precio.grid(row=5, column=2, padx=10, pady=10)
        #Botones
        self.button_cargar.grid(row=0, column=0, padx=20, pady=10, ipadx=5, ipady=5)
        self.button_editar.grid(row=0, column=2, padx=20, pady=10, ipadx=5, ipady=5)

    def filtrar_peli(self):
        input_peli = []

        pelis = self.pelicula.mostrar_nombres(self.bdd)
        for i in range(len(pelis)):
            input_peli.append(pelis[i][1])  
        self.input_peli.config(values=input_peli)
    
    def filtrar_sala(self):
        pelis = self.pelicula.mostrar_nombres(self.bdd)
        i = 0
        while pelis[i][1] != self.input_peli.get():
            i += 1
        tipo_peli = pelis[i][2]

        input_sala = []
        salas = self.sala.mostrar_salas(self.bdd)
        for j in range(len(salas)):
            if salas[j][2] == tipo_peli:
                input_sala.append(salas[j][0])
        self.input_sala.config(values=input_sala)
        
    def selected_sala(self, event):
        opc = self.input_sala.get()
        salas = self.sala.mostrar_salas(self.bdd)
        i = 0
        while salas[i][0] != int(opc):
            i += 1
        self.input_butaca.config(state='normal')
        self.input_butaca.delete(0, 'end')
        self.input_butaca.insert(0, f'{salas[i][1]}')
        self.input_butaca.config(state = 'readonly')
    
    def selected_peli(self, event):
        self.filtrar_sala()

    def cargar(self):
        sala = self.input_sala.get()
        peli = self.input_peli.get()
        butac = self.input_butaca.get()
        fecha = self.input_feha.get()
        hora = self.input_hora.get()
        precio = self.input_precio.get()
        if len(sala) > 0 and len(peli) > 0 and len(butac) > 0 and len(fecha) > 0 and len(hora) > 0 and len(precio) > 0:
            self.funcion.crear_funcion(self.bdd, sala, peli, butac, fecha, hora, precio)
            messagebox.showinfo('Aviso', 'Función agregada exitosamente!')
            self.master.frame_funcion.filtrar_input()
            self.cancelar()
        else:
            messagebox.showerror('Error', 'Debe completar todos los campos!')

    def cancelar(self):
        self.destroy()
        self.master.deiconify()



class EditFuncion(Toplevel):
    def __init__(self, master=None, id_funcion=None, base_datos=None):
        Toplevel.__init__(self, master)
        self.master = master
        self.geometry('330x550')
        self.config(bg='black')
        self.title('Editar Función')
        self.iconbitmap('assets\logo.ico')
        self.protocol('WM_DELETE_WINDOW', self.cancelar)
        self.resizable(0,0)

        self.bdd = base_datos
        self.funcion = Funcion()
        self.id_funcion = id_funcion
        self.pelicula = Pelicula()
        self.sala = Sala()
        
        """FRAMES"""
        self.frame_cabecera = tk.Frame(self)
        self.frame_datos = tk.Frame(self)
        self.frame_botones = tk.Frame(self)

        """WIDGETS"""
        #Titulo
        self.cabecera = ttk.Label(self.frame_cabecera)
        
        #Labels
        self.label_sala = ttk.Label(self.frame_datos)
        self.label_peli = ttk.Label(self.frame_datos)
        self.label_butaca = ttk.Label(self.frame_datos)
        self.label_fecha = ttk.Label(self.frame_datos)
        self.label_hora = ttk.Label(self.frame_datos)
        self.label_precio = ttk.Label(self.frame_datos)

        #Inputs
        self.input_sala = ttk.Combobox(self.frame_datos)
        self.input_peli = ttk.Entry(self.frame_datos)
        self.input_butaca = ttk.Entry(self.frame_datos)
        self.input_feha = ttk.Entry(self.frame_datos)
        self.input_hora = ttk.Entry(self.frame_datos)
        self.input_precio = ttk.Entry(self.frame_datos)
        
        #Buttons
        self.button_editar = ttk.Button(self.frame_botones)
        self.button_editar = ttk.Button(self.frame_botones)

        self.filtrar_input()

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
        self.frame_datos.grid(row=2, column=0, rowspan=5, columnspan=3, pady=20)
        self.frame_botones.grid(row=7, column=0, columnspan=3)

    def widgets_config(self):
        #Titulo
        self.cabecera.config(text = 'Modificá los datos\nde la función', foreground='#FFFFFF', font=('Segoe UI Black', 25), background='red', justify='center')
        
        #Labels
        self.label_sala.config(text='Sala', foreground = '#FFFFFF', font=('Segoe UI Black', 18), background='black')
        self.label_peli.config(text='Pelicula', foreground = '#FFFFFF', font=('Segoe UI Black', 18), background='black')
        self.label_butaca.config(text='Butacas', foreground = '#FFFFFF', font=('Segoe UI Black', 18), background='black')   
        self.label_fecha.config(text='Fecha', foreground='#FFFFFF', font=('Segoe UI Black', 18), background='black')
        self.label_hora.config(text='Horario', foreground='#FFFFFF', font=('Segoe UI Black', 18), background='black')
        self.label_precio.config(text='Precio ($)', foreground='#FFFFFF', font=('Segoe UI Black', 18), background='black')   

        #Inputs
        self.input_sala.config(width=7, state = 'readonly')
        self.input_peli.config(width=27, state = 'readonly')
        self.input_butaca.config(width=10, state = 'readonly')
        self.input_feha.config(width=27)
        self.input_hora.config(width=27)
        self.input_precio.config(width=10)

        self.input_sala.bind("<<ComboboxSelected>>", self.selected_sala)

        #Buttons
        self.button_editar.config(text='Editar Datos', command=self.editar)
        self.button_editar.config(text='Cancelar', command=self.cancelar)

    def widgets_grid(self):
        #Titulo
        self.cabecera.grid(row=0, ipady=10)
        #Sala
        self.label_sala.grid(row=0, column=2, padx=10, pady=10)
        self.input_sala.grid(row=1, column=2, padx=10, pady=10)
        #Pelicula
        self.label_peli.grid(row=0, column=0, padx=10, pady=10)
        self.input_peli.grid(row=1, column=0, padx= 10, pady=10)
        #Butacas Disponibles
        self.label_butaca.grid(row=2, column=2, padx=10, pady=10)
        self.input_butaca.grid(row=3, column=2, padx=10, pady=10)
        #Fecha
        self.label_fecha.grid(row=2, column=0, padx= 10, pady=10)
        self.input_feha.grid(row=3, column=0, padx= 10, pady=10)
        #Horario
        self.label_hora.grid(row=4, column=0, padx=10, pady=10)
        self.input_hora.grid(row=5, column=0, padx=10, pady=10)
        #Precio
        self.label_precio.grid(row=4, column=2, padx=10, pady=10)
        self.input_precio.grid(row=5, column=2, padx=10, pady=10)
        #Botones
        self.button_editar.grid(row=0, column=0, padx=20, pady=10, ipadx=5, ipady=5)
        self.button_editar.grid(row=0, column=2, padx=20, pady=10, ipadx=5, ipady=5)

    def filtrar_input(self):
        funciones = self.funcion.obtener_funciones(self.bdd)
        for func in funciones:
            if func[0] == self.id_funcion:
                self.funcion = Funcion(func[0], func[1], func[2], func[3], func[4], func[5], func[6])

        self.input_sala.insert(0, f'{self.funcion.sala}')
        self.input_peli.insert(0, f'{self.funcion.pelicula}')
        self.input_butaca.insert(0, f'{self.funcion.butacas_libres}')
        self.input_feha.insert(0, f'{self.funcion.fecha}')
        self.input_hora.insert(0, f'{self.funcion.horario}')
        self.input_precio.insert(0, f'{self.funcion.precio}')
        
        pelis = self.pelicula.mostrar_nombres(self.bdd)
        i = 0
        while pelis[i][1] != self.input_peli.get():
            i += 1
        tipo_peli = pelis[i][2]

        input_sala = []
        salas = self.sala.mostrar_salas(self.bdd)
        for j in range(len(salas)):
            if salas[j][2] == tipo_peli:
                input_sala.append(salas[j][0])
        self.input_sala.config(values=input_sala)

    def selected_sala(self, event):
        opc = self.input_sala.get()
        salas = self.sala.mostrar_salas(self.bdd)
        i = 0
        while salas[i][0] != int(opc):
            i += 1
        self.input_butaca.config(state='normal')
        self.input_butaca.delete(0, 'end')
        self.input_butaca.insert(0, f'{salas[i][1]}')
        self.input_butaca.config(state = 'readonly')
    
    def editar(self):
        self.funcion.modificar_funcion(self.bdd, self.id_funcion, sala=self.input_sala.get())
        self.funcion.modificar_funcion(self.bdd, self.id_funcion, pelicula=self.input_peli.get())
        self.funcion.modificar_funcion(self.bdd, self.id_funcion, butacas_libres=self.input_butaca.get())
        self.funcion.modificar_funcion(self.bdd, self.id_funcion, fecha=self.input_feha.get())
        self.funcion.modificar_funcion(self.bdd, self.id_funcion, horario=self.input_hora.get())
        self.funcion.modificar_funcion(self.bdd, self.id_funcion, precio=self.input_precio.get())
        messagebox.showinfo('Aviso', 'Función editada exitosamente!')
        self.master.F_funcion.filtrar_input()
        self.cancelar()

    def cancelar(self):
        self.destroy()
        self.master.deiconify()