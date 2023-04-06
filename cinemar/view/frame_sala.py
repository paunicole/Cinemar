import tkinter as tk
from tkinter import ttk, messagebox
from model.sala import Sala

class SalaAdministrador(tk.Frame):
    def __init__(self, master = None, base_datos = None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.bdd = base_datos
        self.sala = Sala()

        """WIDGETS"""
        #Titulo
        self.cabecera_principal = ttk.Label(self)
        #Tabla
        self.tabla = ttk.Treeview(self)
        #Eliminar
        self.label_eliminar = ttk.Label(self)
        self.input_eliminar = ttk.Combobox(self)
        self.button_eliminar = ttk.Button(self)
        #Agregar
        self.label_agregar = ttk.Label(self)
        self.button_agregar = ttk.Button(self)

        self.label_numero = ttk.Label(self)
        self.input_numero = ttk.Entry(self)
        self.label_capacidad = ttk.Label(self)
        self.input_capacidad = ttk.Entry(self)
        self.label_formato = ttk.Label(self)
        self.input_formato = ttk.Combobox(self)


        self.widgets_config()
        self.widgets_grid()
        self.input_fill()


    def tabla_config(self):
        self.tabla.config(columns = (1,2,3))
        self.tabla.column('#0', width = 70, anchor = 'center')
        self.tabla.column('#1', width = 70, anchor = 'center')
        self.tabla.column('#2', width = 160, anchor = 'center')
        self.tabla.column('#3', width = 70, anchor = 'center')

        self.tabla.heading('#0', text = 'ID Sala', anchor = 'center')
        self.tabla.heading('#1', text = 'Número', anchor = 'center')
        self.tabla.heading('#2', text = 'Cantidad de Butacas', anchor = 'center')
        self.tabla.heading('#3', text = 'Formato', anchor = 'center')
    
    def widgets_config(self):
        #Titulo
        self.cabecera_principal.config(text='Salas', foreground='#FFFFFF', font=('Segoe UI Black', 36), background='red')
        #Tabla
        self.tabla_config()
        #Eliminar
        self.label_eliminar.config(text='Elimina una sala', foreground='#FFFFFF', font=('Segoe UI Black', 18), background='red')
        self.input_eliminar.config(width=5, state='readonly')
        self.button_eliminar.config(text='Eliminar', command=self.Eliminar)
        #Añadir
        self.label_agregar.config(text='Agregar una nueva sala', foreground='#FFFFFF', font=('Segoe UI Black', 18), background='red')
        self.label_numero.config(text='Sala', foreground='#FFFFFF', font=('Segoe UI Black', 18), background='black')
        self.input_numero.config(width=6)
        self.label_capacidad.config(text='Butacas', foreground='#FFFFFF', font=('Segoe UI Black', 18), background='black')
        self.input_capacidad.config(width=6)
        self.label_formato.config(text='Formato', foreground='#FFFFFF', font=('Segoe UI Black', 18), background='black')
        self.input_formato.config(width=3, state='readonly', values=['2D', '3D'])
        self.button_agregar.config(text='Agregar', command=self.Agregar)

    def input_fill(self):
        self.tabla.delete(*self.tabla.get_children())
        salas = self.sala.mostrar_salas(self.bdd)
        id_salas = []

        for sala in salas:
            self.tabla.insert('', 'end', text=f'{sala[0]}', values=(sala[1], sala[2], sala[3]))
            id_salas.append(sala[0])
        
        self.input_eliminar.config(values=id_salas)
    
    def widgets_grid(self):
        #Titulo
        self.cabecera_principal.grid(row=0, column=0, columnspan=8, pady=20, ipady=10)
        #Tabla
        self.tabla.grid(row = 1, column=0, rowspan=4, columnspan=5, padx=60, pady=(0, 20))
        #Eliminar
        self.label_eliminar.grid(row=2, column=5, columnspan=3)
        self.input_eliminar.grid(row=3, column=5)
        self.button_eliminar.grid(row=3, column=7)
        #Añadir
        self.label_agregar.grid(row=5, column=0, columnspan=8, pady=10)
        self.label_numero.grid(row=6, column=2)
        self.input_numero.grid(row=7, column=2)
        self.label_capacidad.grid(row=6, column=3)
        self.input_capacidad.grid(row=7, column=3)
        self.label_formato.grid(row=6, column=4)
        self.input_formato.grid(row=7, column= 4)
        self.button_agregar.grid(row=7, column=5)

    def Agregar(self):
        id = self.input_numero.get()
        butac = self.input_capacidad.get()
        formato = self.input_formato.get()

        if len(id) > 0 and len(butac) > 0 and len(formato) > 0:
            self.sala.cargar_sala(self.bdd, id, butac, formato)
            self.input_fill()
            self.input_numero.delete(0, 'end')
            self.input_capacidad.delete(0, 'end')
            self.input_formato.set('')
            messagebox.showinfo('Aviso', 'Sala agregada exitosamente!')
        else:
            messagebox.showerror('Error', 'Debe rellenar todos los campos!')

    def Eliminar(self):
        id = self.input_eliminar.get()

        if len(id) > 0:
            self.sala.eliminar_sala(self.bdd, id)
            self.input_fill()
            self.input_eliminar.set('')
            messagebox.showinfo('Aviso', 'Sala eliminada exitosamente!')
        else:
            messagebox.showerror('Error', 'Debe seleccionar una sala!')