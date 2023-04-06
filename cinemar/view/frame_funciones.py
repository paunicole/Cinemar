import tkinter as tk
from tkinter import ttk, messagebox
from view.form_funcion import FormularioFuncion, EditFuncion
from model.funcion import Funcion

class FuncionAdministrador(tk.Frame):
    def __init__(self, ventana_padre = None, master = None, base_datos = None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.ventana_padre = ventana_padre
        self.bdd = base_datos
        self.funcion = Funcion()

        """WIDGETS"""
        #Titulo
        self.cabecera_principal = ttk.Label(self)
        
        #Tabla
        self.tabla = ttk.Treeview(self)
    
        #Labels
        self.label_agregar = ttk.Label(self)   
        self.label_editar = ttk.Label(self)
        self.label_eliminar = ttk.Label(self)

        #Inputs
        self.input_editar = ttk.Combobox(self)
        self.input_eliminar = ttk.Combobox(self)

        #Buttons
        self.button_agregar = ttk.Button(self)
        self.button_editar = ttk.Button(self)        
        self.button_eliminar = ttk.Button(self)

        self.widgets_config()
        self.widgets_grid()
        self.filtrar_input()


    def tabla_config(self):
        self.tabla.config(columns = (1,2,3,4))
        self.tabla.column('#0', width=70, anchor='center')
        self.tabla.column('#1', width=70, anchor='center')
        self.tabla.column('#2', width=180, anchor='center')
        self.tabla.column('#3', width=90, anchor='center')
        self.tabla.column('#4', width=70, anchor='center')

        self.tabla.heading('#0', text='ID', anchor='center')
        self.tabla.heading('#1', text='N° Sala', anchor='center')
        self.tabla.heading('#2', text='Pelicula', anchor='center')
        self.tabla.heading('#3', text='Fecha', anchor='center')
        self.tabla.heading('#4', text='Horario', anchor='center')

    def widgets_config(self):
        #Titulo
        self.cabecera_principal.config(text='Funciones', foreground='#FFFFFF', font=('Segoe UI Black', 36), background='red', justify='center')
        
        #Tabla
        self.tabla_config()

        #Labels
        self.label_editar.config(text='Editar Función', foreground='#FFFFFF', font=('Segoe UI Black', 18), background='black')
        self.label_agregar.config(text='Agregar Función', foreground='#FFFFFF', font=('Segoe UI Black', 18), background='black')
        self.label_eliminar.config(text='Eliminar Función', foreground='#FFFFFF', font = ('Segoe UI Black', 18), background='black')
        
        #Inputs
        self.input_editar.config(width=5, state='readonly')
        self.input_eliminar.config(width=5, state='readonly')

        #Buttons
        self.button_editar.config(text='Editar', command=self.editar)
        self.button_agregar.config(text='Agregar', command=self.agregar)
        self.button_eliminar.config(text='Eliminar', command=self.eliminar)

    def widgets_grid(self):
        #Titulo
        self.cabecera_principal.grid(row=0, column=0, columnspan=8, pady=20, ipady=10)
        #Tabla
        self.tabla.grid(row=1, column=0, rowspan=5, columnspan=5, padx=20, pady=(0, 20))
        #Editar
        self.label_editar.grid(row=2, column=5, columnspan=3)
        self.input_editar.grid(row=3, column=5, columnspan=2)
        self.button_editar.grid(row=3, column=7, columnspan=1)
        #Añadir
        self.label_agregar.grid(row=6, column=1)
        self.button_agregar.grid(row=7, column=1, pady=10)
        #Eliminar
        self.label_eliminar.grid(row=6, column=4, columnspan=2)
        self.input_eliminar.grid(row=7, column=4)
        self.button_eliminar.grid(row=7, column=5, pady=10)

    def filtrar_input(self):
        self.tabla.delete(*self.tabla.get_children())
        funciones = self.funcion.obtener_funciones(self.bdd)
        ids = []

        for func in funciones:
            self.tabla.insert('', 'end', text=f'{func[0]}', values=(func[1], func[2], func[3], func[4]))
            ids.append(func[0])
        
        self.input_editar.config(values=ids)
        self.input_eliminar.config(values=ids)

    def editar(self):
        func = self.input_editar.get()
        if len(func) > 0:
            self.input_editar.set('')
            self.ventana_padre.withdraw()
            ventana = EditFuncion(self.ventana_padre, int(func), self.bdd)
            ventana.mainloop()
        else:
            messagebox.showerror('Error', 'Debe seleccionar una función!')
            
    def agregar(self):
        self.ventana_padre.withdraw()
        ventana = FormularioFuncion(self.ventana_padre, self.bdd)
        ventana.mainloop()

    def eliminar(self):
        func = self.input_eliminar.get()
        if len(func) > 0:
            self.funcion.eliminar_funcion(self.bdd, int(func))
            self.filtrar_input()
            self.input_eliminar.set('')
            messagebox.showinfo('Aviso', 'Funcion eliminada exitosamente!')
        else:
            messagebox.showerror('Error', 'Debe seleccionar una función!')