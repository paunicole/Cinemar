import tkinter as tk
from tkinter import ttk, messagebox
from model.descuento import Descuento

class DescuentoAdministrador(tk.Frame):
    def __init__(self, master=None, base_datos=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.bdd = base_datos
        self.descuento = Descuento()

        """WIDGETS"""
        #Titulo
        self.cabecera = ttk.Label(self)
        
        #Tabla
        self.tabla = ttk.Treeview(self)
       
        #Labels
        self.label_editar = ttk.Label(self)
        self.label_dia = ttk.Label(self)
        self.label_porcentaje = ttk.Label(self)

        #Inputs
        self.input_dia = ttk.Combobox(self)
        self.input_porcentaje = ttk.Entry(self)

        #Buttons
        self.button_editar = ttk.Button(self)

        self.widgets_config()
        self.widgets_grid()
        self.input_fill()


    def tabla_config(self):
        self.tabla.config(columns=(1,2))
        self.tabla.column('#0', width=90, anchor='center')
        self.tabla.column('#1', width=120, anchor='center')
        self.tabla.column('#2', width=100, anchor='center')

        self.tabla.heading('#0', text='ID Descuento')
        self.tabla.heading('#1', text='Dia')
        self.tabla.heading('#2', text='Porcentaje (%)')
    
    def widgets_config(self):
        #Titulo
        self.cabecera.config(text='Descuentos', foreground='#FFFFFF', font=('Segoe UI Black', 36), background='red')
        #Tabla
        self.tabla_config()
        #Editar
        self.label_editar.config(text='Edita un descuento', foreground='#FFFFFF', font=('Segoe UI Black', 18), background='black')
        self.label_dia.config(text='Dia', foreground='#FFFFFF', font=('Segoe UI Black', 18), background='black')
        self.input_dia.config(width=10, state='readonly')
        self.label_porcentaje.config(text='Porcentaje', foreground='#FFFFFF', font=('Segoe UI Black', 18), background='black')
        self.input_porcentaje.config(width=13)
        self.button_editar.config(text='Editar', command=self.editar)

    def widgets_grid(self):
        #Titulo
        self.cabecera.grid(row=0, column=0, columnspan=8, pady=20, ipady=10)
        
        #Tabla
        self.tabla.grid(row=1, column=0, rowspan=4, columnspan=5, padx=60, pady=(0,20))
        
        #Labels
        self.label_editar.grid(row=1, column=5, columnspan=2)
        self.label_dia.grid(row=2, column=5)
        self.label_porcentaje.grid(row=3, column=5, padx=(0, 10))     

        self.input_dia.grid(row=2, column=6)
        self.input_porcentaje.grid(row=3, column=6)
        
        #Buttons
        self.button_editar.grid(row=4, column=5, columnspan=2)

    def input_fill(self):
        self.tabla.delete(*self.tabla.get_children())

        descuentos = self.descuento.mostrar_desc(self.bdd)
        dias = []
        for desc in descuentos:
            self.tabla.insert('', 'end', text=f'{desc[0]}', values=(desc[1], desc[2]))
            dias.append(desc[1])
        
        self.input_dia.config(values=dias)

    def editar(self):
        dia = self.input_dia.get()
        por = self.input_porcentaje.get()

        if len(dia) > 0 and len(por) > 0:
            self.descuento.modificar_desc(self.bdd, dia, por)
            self.input_fill()
            self.input_porcentaje.delete(0, 'end')
            self.input_dia.set('')
            messagebox.showinfo('Aviso', 'Descuento modificado exitosamente!')
        else:
            messagebox.showerror('Error', 'Debe rellenar todos los campos!')